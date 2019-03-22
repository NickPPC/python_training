def odd_result_multiplication(n):

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            x = i * j
            if x % 2 == 1:
                print('{} x {} = {}'.format(i, j, x))


if __name__ == '__main__':
    odd_result_multiplication(10)