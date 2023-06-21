a=int(input('ixtiyoriy yil kiriting: '))
if a%400==0:{
	print('shu yili kabisa yili bolgan')
}
elif a%100==0: {
	print('kabisa yili emas')
}
elif a%4==0: {
	print('shu yili kabisa yili bolgan')
}
else: {
	print('kabisa yili emas')
}