
print("##################################")

input_string = input("nhap chuoi so tu tieng anh:")
#tach chuoi thanh danh sach cac tu
words = input_string.split()

#sap xep danh sach cac tu theo thu tu tu dien
sorted_words = sorted(words)

#in danh sach cac tu da sap xep
for word in sorted_words:
    print(word)
