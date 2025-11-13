class Hinhchunhat:
    # Hàm khởi tạo (constructor)
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    # Phương thức tính diện tích
    def dientich(self):
        return self.dai * self.rong


# Tạo đối tượng và thử nghiệm
hcn = Hinhchunhat(5, 3)
print("Diện tích hình chữ nhật là:", hcn.dientich())
