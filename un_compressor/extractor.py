import zipfile


def extract_archive(input, output):
    with zipfile.ZipFile(input, 'r') as zip:
        zip.extractall(output)


if __name__ == "__main__":
    i = r"C:\Users\steve\PycharmProjects\20\un_compressor\zipped.zip"
    o = r"C:\Users\steve\PycharmProjects\20\un_compressor"
    extract_archive(i, o)
