harf=input('istalgan o`zbek tiling lotin alifbo harflaridan birini kiriting: ')

if harf.isalpha() and len(harf)== 1 :
	print("siz bitta harf kiritdingiz. Harfning unli yoki undoshligini aniqlaymiz! ")
	if harf=='a' or harf=='o' or harf=='o`' or harf=='u' or harf=='i' or harf=='e': 
		print("siz kiritgan harf -- unli harf -- ")
	elif harf=='b' or harf=='d' or harf=='f' or harf=='g' or harf=='h' or harf=='k' or harf=='l' or harf=='m' or harf=='n' or harf=='p' or harf=='q' or harf=='r' or harf=='s' or harf=='t' or harf=='v' or harf=='x' or harf=='y' or harf=='z' : 	
		print("siz kiritgan harf -- undosh harf -- ")
	else:
		print("lotin alifbosida bunday harf yo`q")
elif harf.isalpha() and len(harf)== 2 and harf=='g`' or harf=='sh' or harf=='ch' or harf=='ng':
	print("siz kiritgan harf -- undosh harf -- ")
else:
	print("siz harf kiritmadigiz! qayta urinib ko'ring")



