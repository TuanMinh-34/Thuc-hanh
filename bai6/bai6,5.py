class py_solution:
    def reverse_words(self, s):
        # Tách chuỗi thành danh sách các từ, đảo ngược, rồi nối lại
        return ' '.join(reversed(s.split()))

# Tạo đối tượng và gọi hàm
print(py_solution().reverse_words('hello .py'))
