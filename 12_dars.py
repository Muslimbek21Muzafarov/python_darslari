
import pygal

line_chart = pygal.Line()
line_chart.title = 'Social Stats'
line_chart.x_labels = ['March', 'April', 'May']
i=0
for _ in range(3):
# Ma'lumotlarni foydalanuvchidan input orqali olish
	series_name = input("ijtimoiy tarmoq nomini kiriting: ")
	data = input("Ma'lumotlarni kiriting (bir qatordan iborat, vergul bilan ajratilgan): ").split(',')

	# Ma'lumotlarni sonlarga o'tkazish
	data = [float(x.strip()) for x in data]

	line_chart.add(series_name, data)
	i+=1

line_chart.render_in_browser()

