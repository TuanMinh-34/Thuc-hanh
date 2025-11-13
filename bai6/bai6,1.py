class Circle(object):
    # Hàm khởi tạo (constructor) nhận vào bán kính r
    def __init__(self, r):
        self.radius = r  # Gán giá trị bán kính cho thuộc tính radius

    # Phương thức tính diện tích hình tròn
    def area(self):
        return self.radius ** 2 * 3.14  # Công thức: S = π * r²


# Tạo đối tượng Circle với bán kính 2
aCircle = Circle(2)

# In ra diện tích hình tròn
print(aCircle.area())
