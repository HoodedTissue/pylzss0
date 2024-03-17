import lzss

def compress_file(input_file, output_file):
    with open(input_file, 'rb') as file:
        data = file.read()

    compressed_data = lzss.compress(data)

    with open(output_file, 'wb') as file:
        file.write(compressed_data)

input_filename = 'test.txt'
output_filename = 'test.bin'

compress_file(input_filename, output_filename)
