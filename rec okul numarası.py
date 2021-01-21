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

"""burda adım sayısı  aslında sizin gösteridğiniz örnekteki 1 + fonk. çağrısına eşdeğer"""
def sum(mut):
    toplam = 0
    for i in range(len(mut) - 2, -1, -1):
        toplam += int(mut[i])
    print(toplam)


sum(liste)
reclen(liste)


"""func([a,b,c,d,e,f])                                          6         
    1 + func([b,c,d,e,f])                                      5
        1 + func([c,d,e,f])                                   4
            1 + func([d,e,f])                                3
                1 + func([e,f])                             2
                    1 + func([f])                          1     
                        1 + 0             sıfırı bulduktan sonra yukarı doğru toplayarak çıkar  

eğer kodu denemek isterseniz github hesabımda olacaktır """