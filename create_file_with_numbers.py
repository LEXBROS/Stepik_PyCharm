def create_file_with_numbers(n):
    suffix = str(n)
    with open('range_' + suffix + '.txt', 'w', encoding='utf-8') as file:
        for i in range(1, n + 1):
            file.write(str(i) + '\n')


create_file_with_numbers(5)
