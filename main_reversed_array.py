def inverse_array(arr: list, n: int):
    """"
    Обращение массива (задом - наперед)
    в рамках индекса от 0 до n-1
    """
    for i in range(n//2):
        arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]
    return arr

    # arr.reverse()
    # return arr

    # a = arr
    # first = 0
    # last = n - 1
    # while first < last:
    #     holder = a[first]
    #     a[first] = a[last]
    #     a[last] = holder
    #     first += 1
    #     last -= 1
    # return a


def test_inverse_array():
    arr1 = [1, 2, 3, 4, 5]

    print(arr1)
    inverse_array(arr1, 5)
    print(arr1)

    if arr1 == [5, 4, 3, 2, 1]:
        print('test1 - ok')
    else:
        print('test1 - fail')

    arr2 = [0, 0, 0, 0, 0, 0, 0, 10]
    print(arr2)
    inverse_array(arr2, 8)
    print(arr2)
    if arr2 == [10, 0, 0, 0, 0, 0, 0, 0]:
        print('test2- ok')
    else:
        print('test2 - fail')


test_inverse_array()

inverse_array([22,45,12,324,2342,123124,54535,123,3242,23423],10)