def check_password(pw: str):
    conditions = {'digits': 0,
                  'upper': 0,
                  'symbols': 0
                  }
    for i in pw:
        if i.isdigit():
            conditions['digits'] += 1
        elif i == i.upper() and i.isalpha():
            conditions['upper'] += 1
        elif i in '!@#$%*':
            conditions['symbols'] += 1
    perfect = len(pw) >= 10 and conditions['digits'] >= 3 and conditions['upper'] >= 1 and conditions['symbols'] >= 1
    print('Perfect password' if perfect is True else 'Easy peasy')
