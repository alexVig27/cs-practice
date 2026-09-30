max_gradusi = float(input())
n = int(input())
cnt_error = 0
cnt_excess = 0
mx = -10000
sum_elem = 0

for i in range(n):
    s = input()
    if s == 'error':
        cnt_error += 1
    else:
        if float(s) > max_gradusi:
            cnt_excess += 1
        if float(s) > mx:
            mx = float(s)
        sum_elem += float(s)


print(f'Количество записей = {n}')
print(f'Количество ошибок = {cnt_error}')
print(f'Количество превышений = {cnt_excess}')
print(f'максимальное показание = {mx:.1f}')
print(f'среднее показание = {(sum_elem / (n-cnt_error)):.1f}')