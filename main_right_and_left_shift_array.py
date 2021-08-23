def left_shift_array(arr: list):
    """
    Алгоритм сдвига массива влево.
    :param arr: массив чисел.
    tmp временная переменная
    """
    n = arr.__len__()

    tmp = arr[0]

    for i in range(n - 1):  # start, stop, step
        arr[i] = arr[i + 1]

    arr[n - 1] = tmp

    print(arr)


left_shift_array([0, 1, 2, 3, 4, 5, 6])


def right_shift_array(arr: list):
    """
    Алгоритм сдвига массива вправо.
    :param arr: массив чисел.
    tmp временная переменная
    """
    n = arr.__len__()

    tmp = arr[n - 1]

    for i in range(n - 2, -1, -1):  # start, stop, step
        arr[i + 1] = arr[i]

    arr[0] = tmp

    print(arr)


right_shift_array([0, 1, 2, 3, 4, 5, 6])
