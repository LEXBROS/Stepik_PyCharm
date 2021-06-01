subject_marks = [('English', 88), ('Science', 90), ('Maths', 97),
                 ('Physics', 93), ('History', 82), ('French', 78),
                 ('Art', 58), ('Chemistry', 76), ('Programming', 91)]
s = sorted(subject_marks, key=lambda pare: -pare[1])
for i in s:
    print(i[0], i[1])
