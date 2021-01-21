b = input(" okul numaranızı giriniz ")
liste = list(b)

adim = 0

def reclen(arr):

    if not arr:
        global adim
        print("listenin eleman sayısı: {}".format(adim))
        return 0

    arr.pop()
    adim += 1
    return reclen(arr)


def sum(mut):
    toplam = 0
    for i in range(len(mut) - 2, -1, -1):
        toplam += int(mut[i])
    print(toplam)


sum(liste)
reclen(liste)
