def sieve_of_eratosthenes(arr: list):
    n = arr.__len__()

    arr = [True] * n
    arr[0] = arr[1] = False

    for i in range(2, n):
        if arr[i]:
            for j in range(2 * i, n, i):
                arr[j] = False

    for i in range(n):
        print(i, "-", 'простое' if arr[i] else 'составное')


sieve_of_eratosthenes([2, 34, 123, 546, 767, 32432])
