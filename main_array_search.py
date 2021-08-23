def arr_search(arr: list, n: int, var: int):
    """"
    Осуществляет поиск чилса var в массиве arr.
    От 0 до n-1 индекса включительно.
    Возвращает индекс элемента var в массиве arr.
    Или -1, если элемент отсутсвует.
    Если в массиве несколько одинаковых элементов
    равных x, то вернуть индекс первого элемента по счету.
    """

    for i in range(n):
        if arr[i] == var:
            return i

    return -1


def test_array_search():
    arr1 = [1, 2, 3, 4, 5]
    m = arr_search(arr1, 5, 8)

    if m == -1:
        print('test1 - ok')
    else:
        print('test1 - fail')

    arr2 = [-1, -2, -3, -4, -5]
    m = arr_search(arr2, 5, -3)

    if m == 2:
        print('test2 - ok')
    else:
        print('test2 - fail')

    arr2 = [10, 20, 30, 40, 20]
    m = arr_search(arr2, 5, 20)

    if m == 1:
        print('test3 - ok')
    else:
        print('test3 - fail')


test_array_search()
