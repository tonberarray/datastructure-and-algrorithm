# coding = utf-8
# 数组定位排序


def rearrangeByPivot(array, begin, end, pivot, checkequal):
    if end <= begin:
        return
    while begin < end:
        # 如果checkequal为True，互换条件为大于等于，
        # 为False则互换条件为大于
        if (checkequal is True and array[begin] >= pivot) \
                or (checkequal is False and array[begin] > pivot):
            temp = array[begin]
            array[begin] = array[end]
            array[end] = temp
            end -= 1
        else:
            begin += 1
    return array


def rearrangeArray(array, i):
    if (len(array) <= 1):
        return array
    pivot = array[i]
    # 先执行第一步，将数组分为两部分，
    # 第一部分小于pivot，第二部分大于等于pivot
    array = rearrangeByPivot(array, 0,
                             len(array) - 1, pivot, True)
    # 找到第一部分和第二部分分界点
    for j in range(len(array)):
        if array[j] >= pivot:
            break
    # 执行第二步
    array = rearrangeByPivot(array, j,
                             len(array) - 1, pivot, False)
    return array


S = [6, 5, 5, 7, 9, 4, 3, 3, 4, 6, 8, 4, 7, 9, 2, 1]
i = 5
S = rearrangeArray(S, i)
print(S)
