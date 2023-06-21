harf = input("Istalgan o'zbek tiling lotin alifbo harflaridan birini kiriting: ")

if harf.isalpha() and len(harf) == 1:
    print("Siz bitta harf kiritdingiz. Harfning unli yoki undoshligini aniqlaymiz!")
    if harf == 'a' or harf == 'o' or harf == 'o`' or harf == 'u' or harf == 'i' or harf == 'e':
        print("Siz kiritgan harf -- unli harf")
    elif harf == 'b' or harf == 'd' or harf == 'f' or harf == 'g' or harf == 'h' or harf == 'k' or harf == 'l' or harf == 'm' or harf == 'n' or harf == 'p' or harf == 'q' or harf == 'r' or harf == 's' or harf == 't' or harf == 'v' or harf == 'x' or harf == 'y' or harf == 'z':
        print("Siz kiritgan harf -- undosh harf")
    else:
        print("Lotin alifbosida bunday harf yo'q")
elif harf.isalpha() and len(harf)==2 and {harf == 'g`' or harf == 'sh' or harf == 'ch' or harf == 'ng'}:
    print("Siz kiritgan harf -- undosh harf")
else:
    print("Kiritgan ma'lumotingiz bitta harfdan yoki u harf bo'masligi mumkin! Yana qayta urinib ko'ring")
