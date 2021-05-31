import re


def longest_word_in_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        my_re = re.findall(r'\s*(\w+)\s*', file.read())
        len_list = [len(i) for i in my_re]
        for i in range(-1, -len(len_list) - 1, -1):
            if len_list[i] == max(len_list):
                return my_re[i]


print(longest_word_in_file('text.txt'))
