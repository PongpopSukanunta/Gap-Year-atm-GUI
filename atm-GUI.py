from tkinter import *
from tkinter import ttk, messagebox

money = 0

FONT = ('Angsana New', 20)

def balance_check():
	balance = f'ยอดเงินคงเหลือ: {money:,.2f} บาท'
	messagebox.showinfo(title='Balance', message=balance)


def deposit():
	def check_deposit():
		global money
		amount = deposit_amount.get()
		money = money + amount
		messagebox.showinfo('ฝากสำเร็จ', f'คงเหลือ {money:,.2f} บาท')
	GUI2 = Toplevel()
	GUI2.title('Withdraw')
	GUI2.geometry('300x300')

	deposit_amount = IntVar()

	l1 = ttk.Label(GUI2, text='กรุณากรอกจำนวนเงิน', font=FONT)
	E1 = ttk.Entry(GUI2, textvariable=deposit_amount, font=FONT)
	B1 = ttk.Button(GUI2, text='ยืนยัน', command=check_deposit)

	l1.pack(pady=15)
	E1.pack()
	B1.pack(pady=15)

	GUI2.mainloop()


def withdraw():
	def check_withdraw():
		global money

		amount = withdraw_amount.get()
		if amount <= money:
			money = money - amount
			messagebox.showinfo('กรุณารับเงิน', f'คงเหลือ: {money:,.2f}')
		else:
			messagebox.showerror('เกิดข้อผิดพลาด', 'ยอดเงินในบัญชีไม่พอจ่าย กรุณาใส่จำนวนเงินอีกครั้ง')

	GUI2 = Toplevel()
	GUI2.title('Withdraw')
	GUI2.geometry('300x300')

	withdraw_amount = IntVar()

	l1 = ttk.Label(GUI2, text='กรุณากรอกจำนวนเงิน', font=FONT)
	E1 = ttk.Entry(GUI2, textvariable=withdraw_amount, font=FONT)
	B1 = ttk.Button(GUI2, text='ยืนยัน', command=check_withdraw)

	l1.pack(pady=15)
	E1.pack()
	B1.pack(pady=15)

	GUI2.mainloop()

GUI = Tk()
GUI.title('ATM')
GUI.geometry('500x300')

frame = Frame(GUI)

heading = ttk.Label(frame, text='กรุณาเลือกรายการ', font=FONT)

B1 = ttk.Button(frame, text='ถอนเงิน', command=withdraw)
B2 = ttk.Button(frame, text='เช็คยอดเงิน', command=balance_check)
B3 = ttk.Button(frame, text='ออก', command=GUI.quit)
B4 = ttk.Button(frame, text='ฝากเงิน', command=deposit)

frame.pack()
heading.grid(row=0, column=0, columnspan=3, pady=40)
B1.grid(row=1, column=0, padx=20, ipadx=5, ipady=5)
B4.grid(row=1, column=1, padx=20, ipadx=5, ipady=5)
B2.grid(row=1, column=2, padx=20, ipadx=5, ipady=5)
B3.grid(row=2, column=0, columnspan=3, pady=40, ipadx=5, ipady=5)


GUI.mainloop()