def comb(n, k):
    if k == 0 or k == n:
        c = 1
    else:
        c = comb(n - 1, k) + comb(n - 1, k - 1)
    return c


def comb2(n, k):
    a = [[0] * (n + 1) for i in range(n + 1)]
    print_arr(a)
    for i in range(n + 1):
        a[i][0] = 1
        a[i][i] = 1
        for j in range(1, i):
            a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
    print_arr(a)
    return a[n][k]


def print_arr(arr):
    print('--------------------------')
    for a in arr:
        print(a)


if __name__ == '__main__':
    print(comb(5, 3))
    print(comb2(5, 3))
