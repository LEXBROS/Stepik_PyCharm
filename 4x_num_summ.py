summ_in = 0
summ_out = 0
for i in range(1000, 10000):
    for j in str(i):
        summ_in += int(j)
    if summ_in == 20:
        summ_out += i
    summ_in = 0
print(summ_out)
