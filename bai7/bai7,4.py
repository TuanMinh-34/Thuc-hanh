import itertools

def file_read_from_head(fname, nlines):
    with open(fname, 'r') as f:
        for line in itertools.islice(f, nlines):
            print(line.strip())

print("--- Đọc 2 dòng đầu tiên của 'test.txt' ---")
file_read_from_head('test.txt', 2)
