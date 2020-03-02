 
# #odev 1 turkce karekterleri ingilizceye cevirme
#
# cumle="pijamalı hasta yağız şoföre çabucak güvendi"
# print (cumle)
# cumle=list(cumle)
# tr=["ğ","ü","ş","ç","ö","ı","İ"]
# en=["g","u","s","c","o","i","I"]
#
# for i in cumle:
#     for j in tr:
#         if i==j:
#             turkce=cumle.index(i)
#             ingilizce=tr.index(j)
#             cumle[turkce]=en[ingilizce]
# son=""
# for k in cumle:
#     son=son+k
#
# print(son)

# belirli yükseklikten atılan toopun sekme sayısı
#
# yukseklik=100
# dusus=6.5
# min=10
# say=0
# sonuc=yukseklik
# while True:
#     sonuc=sonuc-(yukseklik*dusus/100)
#     if sonuc<min:
#         print("top {} metreden {} kez sekti {}  altına düştü ve düştüğü sonuc {} ".format(yukseklik,say,min,sonuc))
#         break
#     else:
#         say+=1
#
# #yıldızlardan kare oluşturan python kodu
# for satir in range(1,10):
#     for sutun in range(1,10):
#         print("*", end=" ")
#     print()


# 3 kez parola hatasında kızan program
# hata=0
# kul="admin"
# parola="0"
#
# while hata<3:
#     a = input("kullanıcı adını giriniz: ")
#     b = input("parola giriniz: ")
#     if kul!=a or parola!=b:
#         print("hatalı giriş")
#         hata+=1
#     else:
#         print("Sizi tekrar görmek güzel {}".format(kul))
#         break
#
# print("bye")

#carpım tablosu
# for i in range(1,11):
#     for j in range(1,11):
#         print("{} x {} = {}".format(i,j,i*j))

#çarpım tablosu yapan program
say=0
don=1
while don<10:
    say += 1
    print("\n","---"*10)
    for i in range(1,11):
        print(i*say,sep=" ", end="|")
    don+=1

#mükemmel sayı bulma
