def insert_sort(a):
    """
    Сортировка списка А вставками
    """
    n = len(a)
    for top in range(1, n):
        k = top
        while k > 0 and a[k - 1] > a[k]:
            a[k], a[k - 1] = a[k - 1], a[k]
            k -= 1


def choise_sort(a):
    """
    Сортировка списка А выбором
    """
    n = len(a)
    for pos in range(0, n - 1):
        for k in range(pos + 1, n):
            if a[k] < a[pos]:
                a[k], a[pos] = a[pos], a[k]


def bubble_sort(a):
    """
    Сортировка списка А методом пузырька
    """
    n = len(a)
    for bypass in range(1, n):
        for k in range(0, n - bypass):
            if a[k] > a[k + 1]:
                a[k], a[k + 1] = a[k + 1], a[k]


def test_sort(sort_algorithm):
    print("Тестируем: ", sort_algorithm.__doc__)
    print("test #1: ", end="")
    a = [4, 2, 5, 1, 3]
    a_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(a)

    print("OK" if a == a_sorted else "fail")

    print("test #2: ", end="")
    a = list(range(10, 20)) + list(range(0, 10))
    a_sorted = list(range(20))
    sort_algorithm(a)

    print("OK" if a == a_sorted else "fail")

    print("test #3: ", end="")
    a = [4, 2, 4, 2, 3]
    a_sorted = [2, 2, 3, 4, 4]
    sort_algorithm(a)

    print("OK" if a == a_sorted else "fail")


if __name__ == "__main__":
    test_sort(insert_sort)
    test_sort(choise_sort)
    test_sort(bubble_sort)


# Counting sort in Python programming

def counting_sort(array):
    size = len(array)
    output = [0] * size

    # Initialize count array
    count = [0] * 10

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]


data = [4, 2, 2, 8, 3, 3, 1, 9, 8, 7, 5, 6, 4, 7, 5, 6, 2, 1, 4, 9, 5]
counting_sort(data)
print("Sorted Array in Ascending Order: ")
print(data)
