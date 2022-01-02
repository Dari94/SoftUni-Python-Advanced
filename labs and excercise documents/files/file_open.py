file_path = './files/File Opener/text.txt'
try:
    text_file = open(file_path, 'r')
    print("File found")
except FileNotFoundError:
    print("File not found")
