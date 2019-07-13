file_passwd = open("C:/Users/ziyi/Desktop" + "/7k7k-1.txt", encoding='utf-8')

for i in range(1, 11):
    file = open("C:/Users/ziyi/Desktop" + '/score' + str(i) + '.txt', 'w', encoding='utf-8')

    for j in range(0, 100000):
        file.write(file_passwd.readline())

    file.close()
