import os

import grpc

import chunked_file_reading
import file_upload_pb2
import file_upload_pb2_grpc


def get_data(file_path):
    with open(file_path) as file_:
        file_size = os.path.getsize(file_path)
        progress = 0

        for chunk_start, chunk_size in chunked_file_reading.get_chunks(file_size, 1024):
            file_chunk = file_.read(chunk_size)
            progress += chunk_size
            yield file_upload_pb2.DataChunks(data=file_chunk.encode('utf-8'))


def run():
    channel = grpc.insecure_channel('localhost:50051')

    stub = file_upload_pb2_grpc.UploadStub(channel)

    data_iterator = get_data('file.log')

    #    for d in data_iterator:
    #        print(d)

    response = stub.Upload(data_iterator)

    print(response)


if __name__ == '__main__':
    run()
