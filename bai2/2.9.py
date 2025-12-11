
#chuong trinh dem so ki tu trong mot ki tu
str= input("Enter a string:")
dict = {}
for n in str:
    keys = dict.keys()
    if n in jeys:
        dict[n] +=1
    else:
        dict[n] = 11
print(dict)
