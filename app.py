from guizero import App, Text, TextBox, PushButton, Combo
from random import randint


def generateEasy():
    first = randint(0, 10)
    second = randint(0, 10)
    op = randint(0, 1)
    solution = 0
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
    first = random.randint(50, 100)
    second = random.randint(50, 100)
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
    if (answer == my_response.get()):
        text.set("CORRECT")
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
        text.set("INCORRECT")
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

# main app loop
app = App(title = "Math Math Triple Dash")

text = Text(app, text="Welcome to Math Math Triple Dash", size=22, font="Times New Roman", color="blue")
next_ques = Text(app, text="", size=22, font="Times New Roman", color="blue")
my_response = TextBox(app)
start = PushButton(app, command=start, text="Start")
submit = PushButton(app, command=submit, text="Submit")
difficulty_combo = Combo(app, options=["Easy", "Medium", "Hard"])

app.display()
