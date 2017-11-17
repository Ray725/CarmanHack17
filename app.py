from guizero import App, Text, TextBox, PushButton, Combo
from random import *

def generateEasy():
    first = randint(0, 10)
    second = randint(0, 10)
    op = randint(0, 1)
    if op == 0:
        op = "+"
        solution = first + second
    else:
        op = "-"
        solution = first - second
    return ["{} {} {}".format(first, op, second), str(solution)]

def generateMedium():
    first = randint(0, 10)
    second = randint(0, 10)
    op = randint(0, 2)
    solution = 0
    if op == 0:
        op = "+"
        solution = first + second
    elif op == 1:
        op = "-"
        solution = first - second
    else:
        op = "x"
        solution = first * second
    return ["{} {} {}".format(first, op, second), str(solution)]

def generateHard():
    first = randint(0, 50)
    second = randint(1, 50)
    op = randint(0, 3)
    if op == 0:
        solution = first + second
        return ["{} + {}".format(first, second), str(solution)]
    elif op == 1:
        solution = first - second
        return ["{} - {}".format(first, second), str(solution)]
    elif op == 2:
        solution = first * second
        return ["{} x {}".format(first, second), str(solution)]
    else:
        op = "/"
        final = first * second
        return ["{} / {}".format(final, second), str(first)]

def submit():
    global answer
    global score
    global totalQuestions
    totalQuestions += 1
    if (answer == my_response.get()):
        my_response.clear()
        score += 1
        text.set("CORRECT! Score: {}/{}".format(score, totalQuestions))
        if (difficulty_combo.get() == "Easy"):
            question = generateEasy()
            next_ques.set(question[0])
            answer = question[1]
        elif (difficulty_combo.get() == "Medium"):
            question = generateMedium()
            next_ques.set(question[0])
            answer = question[1]
        else:
            question = generateHard()
            next_ques.set(question[0])
            answer = question[1]
    else:
        my_response.clear()
        text.set("INCORRECT. Score: {}/{}".format(score, totalQuestions))
        if (difficulty_combo.get() == "Easy"):
            question = generateEasy()
            next_ques.set(question[0])
            answer = question[1]
        elif (difficulty_combo.get() == "Medium"):
            question = generateMedium()
            next_ques.set(question[0])
            answer = question[1]
        else:
            question = generateHard()
            next_ques.set(question[0])
            answer = question[1]

def start():
    start.disable()
    submit.enable()
    global answer
    if (difficulty_combo.get() == "Easy"):
        question = generateEasy()
        text.set(question[0])
        answer = question[1]
    elif (difficulty_combo.get() == "Medium"):
        question = generateMedium()
        text.set(question[0])
        answer = question[1]
    else:
        question = generateHard()
        text.set(question[0])
        answer = question[1]

def change_text_size(slider_value):
    text.font_size(slider_value)

# main app loop
totalQuestions = 0
score = 0
app = App(title = "Math Math Triple Dash")
text = Text(app, text="Welcome to Math Math Triple Dash", size=22, font="Times New Roman", color="blue")
next_ques = Text(app, text="", size=22, font="Times New Roman", color="blue")
my_response = TextBox(app)
start = PushButton(app, command=start, text="Start")
submit = PushButton(app, command=submit, text="Submit")
submit.disable()
difficulty_combo = Combo(app, options=["Easy", "Medium", "Hard"])

app.display()
