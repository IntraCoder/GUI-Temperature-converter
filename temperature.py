from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x500")
root.title("Your Temperature Converter")
root.config(bg="cyan")
root.resizable(width=False, height=False)


def convert(unit):
    temp = 0
    if unit == "cel":
        if combo.get() == "Celcius":
            pass
        elif combo.get() == "Kelvin":
            temp = temp_var.get() - 273.15
        elif combo.get() == "Fahrenheit":
            temp = (temp_var.get() - 32) * (5 / 9)
        temp = str(temp) + " C"
    elif unit == "kel":
        if combo.get() == "Celsius":
            temp = temp_var.get() + 273.15
        elif combo.get() == "Kelvin":
            pass
        elif combo.get() == "Fahrenheit":
            temp = (temp_var.get() - 32) * (5 / 9) + 273.15
        temp = str(temp) + " K"
    elif unit == "fer":
        if combo.get() == "Celsius":
            temp = temp_var.get() * (9 / 5) + 32
        elif combo.get() == "Kelvin":
            temp = (temp_var.get() - 273.15) * (9 / 5) + 32
        elif combo.get() == "Fahrenheit":
            temp = (temp_var.get() - 32) * (5 / 9)
        temp = str(temp) + " F"
    lab["text"] = temp


Label(root, text="Temperature -", bg="cyan", font="None 20").place(x=30, y=100)
Label(root, text="Converted =", bg="cyan", font="None 20").place(x=30, y=180)
lab = Label(root, text=0, bg="cyan", font="None 20")

combo = ttk.Combobox(root, values=["Celsius", "Kelvin", "Fahrenheit"], font="None 15", width=10, state="readonly")
combo.set("Celsius")

temp_var = IntVar()
Entry(root, textvariable=temp_var, width=10, font="None 20").place(x=220, y=100)

Button(root, text="Convert To Celsius", bg="yellow", font="None 20", command=lambda: convert("cel")).place(x=150, y=250)
Button(root, text="Convert To Kelvin", bg="yellow", font="None 20", command=lambda: convert("kel")).place(x=150, y=320)
Button(root, text="Convert To Fahreinet", bg="yellow", font="None 20", command=lambda: convert("fer")).place(x=150,
                                                                                                             y=400)
lab.place(x=180, y=180)
combo.place(x=220, y=140)

root.mainloop()
