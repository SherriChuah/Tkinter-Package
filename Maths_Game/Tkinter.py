from tkinter import Tk, IntVar, Label, PhotoImage, Radiobutton, Button
from random import randint, shuffle

def configure_window():
	window.geometry("800x600")
	window.configure(background='#b3ffff')
	window.title("M A T H   Q U I Z")

def calculate_answer(num1, num2, operator):
	if operator == 0:
		return num1+num2
	elif operator == 1:
		return num1-num2
	else:
		return num1*num2

def add_incorrect_answers(answer):
	answers = []
	answers.append(answer)
	for i in range(4):
		while True:
			r = randint(-6,6)
			ans = answer + r
			if ans not in answers:
				answers.append(ans)
				break
	return answers

def create_ans_radiobutton(answers):
	ans = []
	for i in range(len(answers)):
		ans.append(Radiobutton(window, text=answers[i], 
										value=answers[i], 
										font=("Arial Bold", 50), 
										indicatoron=0, 
										variable=user_answer, 
										bg="#ffcccc", 
										selectcolor="#99ff99", 
										width=4))
		
		padding = Label(window, text=" ", font=("Monospace", 25), background="#b3ffff")
		padding.grid(column=1, row=3)
		shuffle(ans)
		for i in range(len(ans)):
			ans[i].grid(column=i+2, row=3)
		padding.grid(column=1, row=4)

def clicked(answer):
	if (user_answer.get() == answer):
		btn.configure(text=" Correct ")
		ans_label = Label(window, image=correct)
		global current_score
		current_score += 10
		score.config(text="Score: " + str(current_score))
	else:
		ans_label = Label(window, image=incorrect)
		btn.configure(text=" Incorrect ")
	ans_label.grid(column=1, row=8, columnspan=2)
	window.after(1000, game_loop)

def create_ans_button(answer):
	global btn
	btn = Button(window, text="Check Answer", command=lambda:clicked(answer), background='#ffff4d', font=("Monospace",50))
	btn.grid(column=0, row=5, columnspan=7)

def game_loop():
	num1 = randint(1,20)
	num2 = randint(1,20)
	operator = randint(0,2)
	display_question(num1, num2, operator)
	answer = calculate_answer(num1, num2, operator)
	answers = add_incorrect_answers(answer)
	create_ans_radiobutton(answers)
	create_ans_button(answer)

def display_question(num1, num2, operator):
	operators = ["+", "x", "-"]
	question = str(num1) + " " + operators[operator] + " " + str(num2) + " ="
	question = Label(window, text=question, font=("Monospace", 50), background="#b3ffff")
	question.grid(column=1, row=1, columnspan=6, sticky="W")

window = Tk()
configure_window()

user_answer = IntVar()
btn = None
current_score = 0

score = Label(window, text="Score: 0", font=("Monospace",50), background="#b3ffff")
score.grid(column=2, row=8, columnspan=4, sticky='E')

correct = PhotoImage(file="correct.png")
incorrect = PhotoImage(file="incorrect.png")

game_loop()

window.mainloop()

print("hello there")
