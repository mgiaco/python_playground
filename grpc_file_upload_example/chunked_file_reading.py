# chunked file reading
# based on https://gist.github.com/richardasaurus/21d4b970a202d2fffa9c
from __future__ import division

import os


def get_chunks(file_size, chunk_size):
    chunk_start = 0
    #    chunk_size = 1000  # 131072 bytes, default max ssl buffer size
    while chunk_start + chunk_size < file_size:
        yield (chunk_start, chunk_size)
        chunk_start += chunk_size

    final_chunk_size = file_size - chunk_start
    yield (chunk_start, final_chunk_size)


def read_file_chunked(file_path):
    with open(file_path) as file_:
        file_size = os.path.getsize(file_path)

        print('File size: {}'.format(file_size))

        progress = 0

        for chunk_start, chunk_size in get_chunks(file_size, 1000):
            file_chunk = file_.read(chunk_size)

            # do something with the chunk, encrypt it, write to another file...

            progress += chunk_size
            print('{0} of {1} bytes read ({2}%)'.format(progress, file_size, int(progress / file_size * 100)))


if __name__ == '__main__':
    read_file_chunked('file.log')

# sample output:
# File size: 698837
# 131072 of 698837 bytes read (18%)
# 262144 of 698837 bytes read (37%)
# 393216 of 698837 bytes read (56%)
# 524288 of 698837 bytes read (75%)
# 655360 of 698837 bytes read (93%)
# 698837 of 698837 bytes read (100%)
