from math import floor
from datetime import timedelta, datetime
from tkinter import *
from tkinter import filedialog

def tytul_czas():
	now = datetime.now()
	return "tytul" + now.strftime("%Y%m%d%H%M%S")

def timedelta_conv(prob, prob_sek):
	prob = int(prob)
	prob_sek = int(prob_sek)
	wynik = prob/prob_sek
	minuty = int(wynik / 60)
	sekundy = int(wynik % 60)
	milisekundy = floor(wynik * 25) % 25 * 40
	return [timedelta(minutes=minuty, seconds=sekundy, milliseconds=milisekundy), floor(wynik * 25)]


def convert():
	text_out.delete('1.0', END)
	temp_in = text_in.get("1.0", END).strip().splitlines()
	all_time = timedelta()

	for index, i in enumerate(temp_in):
		temp_in[index] = temp_in[index].split("|")
		temp_in[index].append(timedelta_conv(temp_in[index][3], temp_in[index][0]))
		all_time += temp_in[index][5][0]

	text_out.insert(END, "[0" + str(all_time)[:-7] + "]\n")

	licznik = timedelta()
	for index, i in enumerate(temp_in):
		if index == 0:
			text_out.insert(END, temp_in[index][4] + "\n")
		else:
			text_out.insert(END, temp_in[index][4] + " (0" + str(licznik)[:-7] + ")\n")
		licznik += temp_in[index][5][0]

	text_out.insert(END, "\nTSMuxer\n")

	licznik2 = timedelta()
	for index, i in enumerate(temp_in):
		if index == 0:
			text_out.insert(END, "00:00:00.000\n")
		else:
			text_out.insert(END, "0" + str(licznik2)[:-3] + "\n")
		licznik2 += temp_in[index][5][0]

	text_out.insert(END, "\nsekund\n" + str(all_time.seconds) + "\n\nMuxman\n")

	licznik3 = temp_in[0][5][1]
	for index, i in enumerate(temp_in, 1):
		text_out.insert(END, str(licznik3) + "\n")
		licznik3 += temp_in[index][5][1]

def SaveFile():
	filename = filedialog.asksaveasfilename(initialfile=tytul_czas() ,filetypes=(("txt files", "*.txt"), ("all files", "*.*")), defaultextension = "*.txt")

	if filename:
		with open(filename, "w", -1, "utf-8") as file:
			file.write(text_out.get("1.0", END).strip())

root = Tk()
root.title("Converter")

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Save As...", command=SaveFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

text_in = Text(root, width=100, height=50)
text_in.grid(row=0, column=0)

b_convert = Button(root, text="->", command=convert)
b_convert.grid(row=0, column=1)

text_out = Text(root, width=100, height=50)
text_out.grid(row=0, column=2)

root.mainloop()
