# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""The Python implementation of the GRPC helloworld.Greeter server."""

import time
from concurrent import futures

import grpc

import file_upload_pb2
import file_upload_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class UploadServicer(file_upload_pb2_grpc.UploadServicer):

    def Upload(self, request_iterator, context):
        for data_chunks in request_iterator:
            print(data_chunks)

        return file_upload_pb2.UploadStatus(status='ok')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    file_upload_pb2_grpc.add_UploadServicer_to_server(UploadServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
