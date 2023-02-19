import tkinter as tk

window = tk.Tk()
window.title("Encoder V1.0")
window.geometry('225x250')

rotCount = tk.StringVar()
uinput = ""
uinput2 = 0

def encode(s, rot):
	r = ""
	d = 0
	lett = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
	        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
	for i in range(len(s)):
		if s[i].isalpha() == True:
			d = 0
			for j in range(26):
				if s[i] == lett[j]:
					d = j
			for k in range(rot):
				if d < 25:
					d += 1
				elif d == 25:
					d = 0
			r += lett[d]
		else:
			r += s[i]
	
	return r

def callback(event):

	uinput = inputBox.get("1.0", "end")

	try:
		uinput2 = int(inputBox2.get())
	except:
		resultBox.delete("1.0","end")
		resultBox.insert("1.0", "ERROR")
		return False

	if uinput != "":
		resultBox.delete("1.0","end")
		resultBox.insert("1.0", encode(uinput, uinput2))
		return True
		

window.bind('<Return>', callback)

greeting = tk.Label(window, text = "Encode")
greeting.grid(row = 0, column = 1)

inputBox = tk.Text(window, bd = 3, relief = "raised", height = 5, width = 20)
inputBox.grid(row = 1, column = 1)

rotation = tk.Label(window, text = "ROT")
rotation.grid(row = 2, column = 0)

inputBox2 = tk.Entry(window, bd = 3, relief = "sunken", width = 10, textvariable = rotCount)
inputBox2.grid(row = 2, column = 1)

resultBox = tk.Text(window, bd = 3, relief = "raised", height = 5, width = 20)
resultBox.grid(row = 3, column = 1)

window.mainloop()