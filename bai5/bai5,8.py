# mymodule.py

def Sequential_Search(dlist, item):
    """
    Hàm tìm kiếm tuyến tính.
    Trả về (True, vị trí) nếu tìm thấy item trong dlist,
    ngược lại trả về (False, -1).
    """
    for i in range(len(dlist)):
        if dlist[i] == item:
            return (True, i)
    return (False, -1)
