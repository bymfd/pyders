# # %%
# # var1 = "asgfjsfhlskg sdlkh hklijr"
# # print(len(var1))
# # print (var1[1])
# # print (var1[0])
# # print (var1[24])
#
# # %%
# # List
#
# list_pazar = ["domates","biber","mandalina","nar","aa","ab","bb","bac"]
# print(list_pazar)
#
# print(list_pazar[2])
# list_pazar.append("portakal")
# print(list_pazar)
# list_pazar.remove("portakal")
# print(list_pazar)
#
# list1 = [1,2,3,4,5,6,7,8]
# list2 = [3,4,6,8,9,0,1,2,5,7]
#
# a = list1.pop(5)
# print(list1)
# print(a)
# list1.append(a)
# print(list1)
# list1.sort()
# print(list1)
# list1.reverse()
# print(list1)
#
#
# list_pazar.sort()
# print(list_pazar)
#
# list3 = ["a",1,1.3,"deneme"]
# print(list3)
# list3.sort()
# print(list3)
# ## %%
# # Döngüler
# # For

# for i in range(1,11):
#     print(i)
# print(i)

# list_pazar = ["domates","biber","mandalina","nar",]
#
# for j in list_pazar:
#     print(j)
# print(j)
#
# for i in "bolu esiyor":
#     print(i)
# for i in "bolu esiyor".split():
#     i += 1
#     print(i)
#
# list1 = [5,9,6,4,5,3,7,8]
#
# for d in list1:
#     d +=1
#     print(d)

# sayac = 0
# liste = [1,4,5,6,8,3,3,4,67]
# for i in liste:
#     sayac = sayac + i
#     print(sayac)



# liste = []
# for i in range(1,11):
#     a = int(input("sayı giriniz: "))
#     liste.append(a)
# print(liste)


# liste = []
# for i in range(1,11):
#     a = int(input("sayı giriniz: "))
#     liste.append(a)
# for j in liste:
#     toplam=toplam+j
# print (toplam)


# # mfd-pc
# K73QgVor

# liste = [500,23,451,67,77]
# mini = liste[0]
# max = liste[0]
#
# for i in liste:
#    if i < mini:
#        mini = i
#    elif i > max:
#        max = i
#    else:
#        pass
# print(mini)
# print(max)

# %%

# while loop

# a = 1
# while a == 1:
#     print("naber")
#     a = int(input("sayı gir 1 den farklı olsun:)(: "))

    # Kullanıcıdan negatif bir tam sayı girene kadar döngü

#
#
# b = 1
# while b==1:
#    gir= int(input("Sayı giriniz: "))
#    if gir <0:
#        b=0
#    else:
#        pass
#
#

# yol 2 ---------

#
# c = 1
# while c >= 0:
#    c= int(input("Sayı giriniz: "))
#

# say = 1
#
# while say == 1:
#     girin = int(input("sayı giriniz"))
#     if girin % 2 == 0:
#         print("bye")
#         break

# kullanıcıdan girilen 6 sayının tek ve çiftlerini ayrı ayrı toplayan
# program

# topc=0
# topt=0
# say=0
# while say<6 :
#     girin = int(input("sayı giriniz"))
#     if girin % 2 == 0:
#         topc=topc+girin
#     else:
#         topt=topt+girin
#     say+=1
#
# print("tek= ",topt,"çift= ",topc)

# %%