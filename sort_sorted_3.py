subject_marks = [('English', 88), ('Science', 90), ('Maths', 88),
                 ('Physics', 93), ('History', 78), ('French', 78),
                 ('Art', 78), ('Chemistry', 88), ('Programming', 91)]
s = sorted(subject_marks, key=lambda pare: (-pare[1], pare[0]))
for i in s:
    print(i[0], i[1])
