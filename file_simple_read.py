def file_read(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        print(file.read())
