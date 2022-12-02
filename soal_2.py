def cetakHuruf(str):
    strLength = len(str)
    if strLength % 2 == 0 :
        return str[0] + str[1] + str[2] + ' dan ' + str[-3] + str[-2] + str[-1]
    else :
        tengah = int(strLength / 2)
        return str[tengah - 1] + str[tengah] + str[tengah+1]

kata = input("Masukkan kata : ")
res = cetakHuruf(kata)
print("Huruf yang diambil pada kata " + kata + " adalah " + res)