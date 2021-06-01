days = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve']
len_four = list(filter(lambda x: len(x) == 4 or x[0] == 'S', days))
print(*sorted(len_four), sep='\n')
