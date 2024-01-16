# Задание
#
# Написать программу в любой парадигме для бинарного поиска.
# На вход подаётся целочисленный массив и число.
# На выходе - индекс элемента или -1, в случае если искомого элемента нет в массиве.


def binary_search(arr, num, range=None):
    if range is None:
        range = (0, len(arr))
    i = range[0] + ((range[1] - range[0]) >> 1)
    if arr[i] < num:
        range = (i + 1, range[1])
    elif arr[i] > num:
        range = (range[0], i - 1)
    else:
        return i
    if range[0] > range[1]:
        return -1
    return binary_search(arr, num, range)


print(binary_search([1, 2, 4, 5, 7, 9], 5))


# Программа написана в императивной парадигме, т.к. она наиболее подходит для решения данной задачи.
