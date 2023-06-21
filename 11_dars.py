from turtle import Turtle, Screen
oyna = Screen()
oyna.title("mening oynam")
chiziq = Turtle()
chiziq.color('red')
chiziq.pensize(5)
chiziq.speed(0.1)
chiziq.hideturtle()
chiziq.up()
chiziq.goto(200,200)
chiziq.down()
chiziq.goto(200,-200)
chiziq.goto(-200,-200)
chiziq.goto(-200,200)
chiziq.goto(200,200)

koptok = Turtle()
koptok.shape('circle')
koptok.up()
koptok.goto(0,0)
                                     
darvoza=Turtle()
darvoza.pensize(5)
darvoza.hideturtle()
darvoza.speed(0.2)
darvoza.color('green')
darvoza.up()
darvoza.goto(-50,-150)
darvoza.down()
darvoza.goto(-50,-200)
darvoza.goto(-150,-200)
darvoza.goto(-150,-150)
darvoza.goto(-50,-150)


tezx=3
tezy=6
while True:
	x,y=koptok.position()
	koptok.goto(x+tezx,y+tezy)
	if x+tezx>=200 or x+tezx<=-200:
		tezx=-tezx
	if y+tezy>=200 or y+tezy<=-200:
		tezy=-tezy
	if -150<=x+tezx<=-50 and -200<=y+tezy<=-150:
		break


oyna.mainloop()