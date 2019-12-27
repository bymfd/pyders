"""print(4/2)
print(4%2)
birinci= 5
birinci +=1
ikinci = 2
sonuc = birinci / ikinci
print (sonuc)
print (birinci % ikinci)
"""


#2,147,483647----2,147,483647
"""
a =2
b= "25"
c = 10.2
d='1'
#print (a+b)
print (type(a))
print (type(b))
print (type(c))

print (int(b)+a)
print (float(a)+0.41)

print (type(str(a)))
"""

# a= input("bana birinci sayıyı söyle  : ")
# b= input("bana ikinci sayıyı söyle  : ")
# print (int(a)+int(b))
# c = int(input("sayı gir: "))
# print(type(c))
#

# b = eval(a)
# print(b)

# vize = int(input("Vize: "))
# final = int (input("Final: "))
#
# hesap = vize * 0.4
# hesap = hesap + final *0.6
# if hesap >= 60:
#     print("Geçti")
#     print(hesap)
# else:
#     print("kaldı")

#
# sayı = int(input("sayı: "))
#
# if sayı < 10:
#     print("""sayı {} 10 dan {} küçük sayı =  {}""".format(sayı,1,2))
# print("dsvvkjsdbg")
# # if sayı <0:
# #     print("sayı 0 dan küçüktür")

k_adı = "admin"
psw = "admin"
kullanıcı_adı = input("Kullanıcı adı giriniz: ")
parola = input("Parolanızı giriniz: ")

if kullanıcı_adı == k_adı and parola == psw:
    print("giriş başarılı hoşgeldiniz {}".format(k_adı))
elif kullanıcı_adı != k_adı or parola != psw:
    print("kullanıcı adı veya parola hatalı ")
else:
    print("işlemde bir hata oluştu")

# elif kullanıcı_adı != k_adı and parola == psw:
#     print("kullanıcı adı hatalı")
# else :
#     print("daha sonra tekrar deneyin :)")