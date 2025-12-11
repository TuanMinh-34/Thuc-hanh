
def bubble_sort(nlist):
    loop = len(nlist)
    for i in range(loop):
        swapped = False
        for j in range(0, loop - i - 1):
            if nlist[j] > nlist[j+1]:
                # Tráo đổi các phần tử
                nlist[j], nlist[j+1] = nlist[j+1], nlist[j]
                swapped = True
        # Nếu không có phần tử nào được tráo đổi, mảng đã được sắp xếp
        if not swapped:
            break
    return nlist
