subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93), ('History', 82)]
s = sorted(subject_marks, key=lambda pare: pare[1])
for i in s:
    print(i[0], i[1])
