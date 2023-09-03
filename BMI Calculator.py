from tkinter import *


def calculate_bmi():
    weight = float(entry1.get())
    height = float(entry2.get()) / 100
    bmi = weight / (height ** 2)
    label3.config(text=f"BMI: {bmi:.2f}")
    if bmi <= 18.4:
        label4.config(text="underweight")
    elif  18.5 <= bmi <=24.9:
        label4.config(text="normal")
    elif 25 <= bmi <= 39.9:
        label4.config(text="overweight")
    elif bmi >= 40:
        label4.config(text="obese")
















#window
window=Tk()
window.title("BMI Calculator")
window.wm_minsize(width=250,height=200)



label1=Label(text="Weight")
label1.pack()
label2=Label(text="Height")
label2.place(x=105,y=100)
label3=Label(text="")
label3.pack()
label4=Label(text="")
label4.pack()

entry1=Entry(width=15)
entry1.pack()
entry2=Entry(width=15)
entry2.place(x=80,y=125)



button=Button(text="Calculate",pady=15,command=calculate_bmi)
button.place(x=100,y=150)




















window.mainloop()




