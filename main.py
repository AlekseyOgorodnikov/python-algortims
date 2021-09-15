# Факториал
def func(n: int):
    assert n >= 0, 'Факториал отрицательного числа не определен'
    if n == 0:
        return 1
    return func(n-1)*n


print(func(3))

# Алгоритм Евклида
