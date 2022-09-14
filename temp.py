def marge(lst):
    if len(lst) > 1:
        left_lst = lst[:len(lst) // 2]
        right_lst = lst[len(lst) // 2:]

        marge(left_lst)
        marge(right_lst)

        i = j = k = 0
        while i < len(left_lst) and j < len(right_lst):
            if left_lst[i] < right_lst[j]:
                lst[k] = left_lst[i]
                i += 1
            else:
                lst[k] = right_lst[j]
                j += 1
            k += 1
        while i < len(left_lst):
            lst[k] = left_lst[i]
            i += 1
            k += 1
        while j < len(right_lst):
            lst[k] = right_lst[j]
            j += 1
            k += 1


arr = [1, 3, 0, 5, 0, 4, 5, 0, 7]
marge(arr)
print(arr)
