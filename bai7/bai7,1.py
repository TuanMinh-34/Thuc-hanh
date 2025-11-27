input_file = open('D:/a.txt', 'r')

for line in input_file:
    line = line.rstrip('\n')
    l = len(line)
    s = ''
    while l > 0:
        s = s + line[l-1]
        l = l - 1
    print(s)

input_file.close()
