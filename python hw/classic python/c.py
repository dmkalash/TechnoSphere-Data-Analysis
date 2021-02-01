pars = [1000, 500, 200, 100, 50, 10, 5, 1]

n1, n2 = list(map(int, input().split('.')))
n = n1 * 100 + n2

for par in pars:
    if n == 0:
        break
    if n // par != 0:
        print('{:5.2f}\t{}'.format(par / 100, n // par))
        n %= par
