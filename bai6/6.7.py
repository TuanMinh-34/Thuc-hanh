
print("############################")
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Sử dụng
radius = float(input("Nhập bán kính hình tròn: "))
circle = Circle(radius)

print("Diện tích hình tròn là:", circle.area())
print("Chu vi hình tròn là:", circle.perimeter())
