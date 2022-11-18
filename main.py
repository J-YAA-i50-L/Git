s = [int(i) for i in input().split()]
h, b = max(s) + 1, len(s) + 2
s = [h - i for i in s]

for i in range(h + 1):
    if i == 0:
        [print('*', end='') for _ in range(b)]
        print()
    else:
        print('*', end='')
        for j in range(b - 2):
            if s[j] > 0:
                print(' ', end='')
            else:
                print('*', end='')
            s[j] = s[j] - 1
        print('*', end='')
        print()

