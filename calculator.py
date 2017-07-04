from tkinter import*

#function that takes in numbers and 
#store them in a global variable operator and display them on the input screen by setting text input
def btnClick(numbers):
	global operator
	operator=operator+str(numbers)
	text_Input.set(operator)

#function that set the text input empty using an empty global variable operator
def btnClearDisplay():
	global operator
	operator=""
	text_Input.set("")

#function that actually calculates the output desired
#sets it to text input
#update operator to 0 at the end of each operation
def btnEqualsInput():
	global operator
	sumUp=str(eval(operator))
	text_Input.set(sumUp)
	operator=""

#name of the app
cal=Tk()

#title
cal.title("My Calculator")

#operator that is going to be displayed and the text input
operator=""
text_Input=StringVar()

#the lay out of the text input
txtDisplay=Entry(cal,font=('arial',30,'bold'),textvariable=text_Input, bd=20, 
				insertwidth=4, bg="black",fg="white", justify='right').grid(columnspan=4)
 
#buttons required for a basic calculator using the hidden function lambda
btn7=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',25,'bold'),
			text="7",command=lambda:btnClick(7)).grid(row=2,column=0)
btn8=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',25,'bold'),
			text="8",command=lambda:btnClick(8)).grid(row=2,column=1)
btn9=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',25,'bold'),
			text="9",command=lambda:btnClick(9)).grid(row=2,column=2)
btnAdd=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',25,'bold'),
			text="+",command=lambda:btnClick("+")).grid(row=2,column=3)
btnMinus=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',25,'bold'),
			text="-",command=lambda:btnClick("-")).grid(row=3,column=3)
btnMultiply=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',25,'bold'),
			text="*",command=lambda:btnClick("*")).grid(row=4,column=3)
btnDivide=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',25,'bold'),
			text="/",command=lambda:btnClick("/")).grid(row=5,column=2)
btn4=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',25,'bold'),
			text="4",command=lambda:btnClick(4)).grid(row=3,column=0)
btn5=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',25,'bold'),
			text="5",command=lambda:btnClick(5)).grid(row=3,column=1)
btn6=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',25,'bold'),
			text="6",command=lambda:btnClick(6)).grid(row=3,column=2)
btn1=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',25,'bold'),
			text="1",command=lambda:btnClick(1)).grid(row=4,column=0)
btn2=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',25,'bold'),
			text="2",command=lambda:btnClick(2)).grid(row=4,column=1)
btn3=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',25,'bold'),
			text="3",command=lambda:btnClick(3)).grid(row=4,column=2)
btn0=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',25,'bold'),
			text="0",command=lambda:btnClick(0)).grid(row=5,column=0)
btnClear=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',25,'bold'),
			text="C",command=btnClearDisplay).grid(row=1,column=2)
btnEquals=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',25,'bold'),
			text="=",command=btnEqualsInput).grid(row=5,column=3)
btnMod=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',25,'bold'),
			text="%",command=lambda:btnClick("%")).grid(row=1,column=3)
btnDot=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',25,'bold'),
			text=".",command=lambda:btnClick(".")).grid(row=5,column=1)
btnBracket=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',25,'bold'),
			text="(",command=lambda:btnClick("(")).grid(row=1,column=0)
btnBracket=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',25,'bold'),
			text=")",command=lambda:btnClick(")")).grid(row=1,column=1)


#block/run the program
cal.mainloop()

