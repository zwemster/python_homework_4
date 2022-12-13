def rle_compression(data):
    compress_count = 1
    compress_result = ''
    for i in range(len(data) - 1):
        if data[i] == data[i + 1]:
            compress_count += 1
        else:
            compress_result += f'{compress_count}{data[i]}'
            compress_count = 1
    print(compress_result + f'{compress_count}{data[i]}')


def rle_decompression(data):
    decompress_count = ''
    decompress_result = ''
    for i in range(len(data) - 1):
        if data[i].isdigit():
            decompress_count += data[i]
        else:
            decompress_result += f'{int(decompress_count) * data[i]}'
            decompress_count = ''
    print(decompress_result + f'{int(decompress_count) * data[i + 1]}')


data_to_compress = input('Пиши, чё там надо сжать: ')
rle_compression(data_to_compress)
data_to_decompress = input('А чё расжимать будем? ')
rle_decompression(data_to_decompress)