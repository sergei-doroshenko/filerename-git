from filerename.dynamic.combinations import print_arr


def solve(a):
    n = len(a)
    m = len(a[0])
    b = [[0] * m for _ in range(n)]
    b[m - 1][0] = a[m - 1][0]
    for i in range(n - 2, -1, -1):
        b[i][0] = b[i + 1][0] + a[i][0]
    for j in range(1, m):
        b[m - 1][j] = b[m - 1][j - 1] + a[m - 1][j]
    for i in range(n - 2, -1, -1):
        for j in range(1, m):
            b[i][j] = max(b[i + 1][j], b[i][j - 1]) + a[i][j]
    print_arr(b)
    return b[0][m - 1]
    #result = way(0, 3, a, b, res=[])
    #print(result)


def way(i, j, a, b, res):
    res.append((i, j))
    if i == len(a[0]) - 1 and j == 0:
        print(res)
        return res
    elif i == len(a[0]) - 1 and j > 0:  # bottom line
        way(i, j - 1, a, b, res)
    elif i < len(a[0]) - 1 and j == 0:  # left line
        way(i + 1, j, a, b, res)
    elif b[i][j] - a[i][j] == b[i + 1][j]:
        way(i + 1, j, a, b, res)
    elif b[i][j] - a[i][j] == b[i][j - 1]:
        way(i, j - 1, a, b, res)


if __name__ == '__main__':
    a = [
        [9, 8, 6, 2],
        [10, 11, 13, 11],
        [3, 7, 12, 8],
        [5, 9, 13, 9],
    ]
    solve(a)
