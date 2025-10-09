import math

pos = [0, 0]  # vị trí ban đầu (x, y)

while True:
    s = input()  # nhận dòng nhập từ người dùng
    if not s:  # nếu người dùng nhập dòng trống, kết thúc vòng lặp
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])

    if direction == "UP":
        pos[1] += steps  # đi lên tăng tọa độ y
    elif direction == "DOWN":
        pos[1] -= steps  # đi xuống giảm tọa độ y
    elif direction == "LEFT":
        pos[0] -= steps  # đi trái giảm tọa độ x
    elif direction == "RIGHT":
        pos[0] += steps  # đi phải tăng tọa độ x
    else:
        pass  # nếu không phải 4 hướng trên thì không làm gì

# Tính khoảng cách từ vị trí hiện tại về gốc (0, 0)
distance = math.sqrt(pos[0]**2 + pos[1]**2)

# In ra khoảng cách làm tròn gần nhất
print(int(round(distance)))
