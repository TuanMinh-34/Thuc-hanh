class Nguoi(object):
    def getGender(self):
        return "Unknown"

class Nam(Nguoi):
    def getGender(self):
        return "Nam"

class Nu(Nguoi):
    def getGender(self):
        return "Nữ"


# Tạo đối tượng từ các lớp con
aNam = Nam()
aNu = Nu()

print(aNam.getGender())
print(aNu.getGender())
