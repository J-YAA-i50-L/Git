s = [int(i) for i in input().split()]
h, b = max(s) + 1, len(s) + 2
s = [h - i for i in s]

for i in range(h + 1):
    if i == 0:
        [print('*', end='') for _ in range(b)]
        print()
    else:
        print('*', end='')
        [print(' ', end='') if s[j] > 0 else print('*', end='') for j in range(b - 2)]
        s = [s[j] - 1 for j in range(b - 2)]
        print('*', end='')
        print()
