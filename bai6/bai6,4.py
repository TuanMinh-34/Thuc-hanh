class py_solution:
    """
    Class chuyển đổi số La Mã thành số nguyên.
    """
    def roman_to_int(self, s):
        """
        Phương thức chuyển đổi số La Mã 's' thành số nguyên.

        Args:
            s (str): Chuỗi số La Mã.

        Returns:
            int: Số nguyên tương ứng.
        """
        # Ánh xạ các ký hiệu La Mã với giá trị số nguyên của chúng
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0  # Khởi tạo giá trị số nguyên

        # Lặp qua chuỗi số La Mã
        for i in range(len(s)):
            # Kiểm tra trường hợp đặc biệt (như IV = 4, IX = 9, v.v.)
            # Điều kiện:
            # 1. i > 0 (không phải ký tự đầu tiên)
            # 2. Giá trị của ký tự hiện tại > giá trị của ký tự trước đó
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                # Nếu là trường hợp đặc biệt:
                # int_val đã được cộng giá trị của ký tự trước (rom_val[s[i - 1]])
                # => Cần trừ đi 2 lần giá trị đó, rồi cộng giá trị của ký tự hiện tại
                # Tương đương: int_val = int_val - rom_val[s[i-1]] - rom_val[s[i-1]] + rom_val[s[i]]
                # Hay: int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
                
                # Đây là một cách viết hơi 'lắt léo' theo lưu đồ.
                # Cách dễ hiểu hơn:
                # Lấy giá trị hiện tại (rom_val[s[i]])
                # Trừ đi 2 lần giá trị đã cộng nhầm của ký tự trước đó (2 * rom_val[s[i - 1]])
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                # Trường hợp thông thường (giá trị ký tự hiện tại <= giá trị ký tự trước đó)
                int_val += rom_val[s[i]]

        return int_val

# --- Phần kiểm tra và chạy chương trình ---
# Khởi tạo đối tượng từ class
solution = py_solution()

# Kiểm tra với các giá trị theo ví dụ trong lưu đồ
print(f"MMMCMLXXXIV -> {solution.roman_to_int('MMMCMLXXXIV')}") # 3984
print(f"MMMM -> {solution.roman_to_int('MMMM')}") # 4000
print(f"C -> {solution.roman_to_int('C')}") # 100
