file_path = 'D:/a.txt'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

print(content)
