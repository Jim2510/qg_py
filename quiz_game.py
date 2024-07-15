print("Welcome to Python Quiz Game! \n This is a simple program made by me to help me study Python tracking a score wich I can use to improve my skills. \n")

playing = input("Are you ready? (y/n) ")

if playing.lower() != 'y':
    print("Ok, take your time")
    quit()
    
    
print("Ok, let's start!")
score = 0

questions = [
    ("What is the output of print(2 ** 3)?", "8"),
    ("Which of the following is a Python data type? \n 1) list \n 2) array \n 3) function", "1", "list"),
    ("How do you insert comments in Python code?", "#"),
    ("Which keyword is used to define a function in Python?", "def"),
    ("How do you create a variable with the floating number 2.8?", "x = 2.8"),
    ("What is the correct file extension for Python files?", ".py"),
    ("How do you create a list in Python?", "[1, 2, 3]", "list"),
    ("What is the output of print(len('Python'))?", "6"),
    ("Which method can be used to remove any whitespace from both the beginning and the end of a string?", "strip"),
    ("How do you start a for loop in Python?", "for"),
    ("Which of the following is a valid variable name in Python? \n 1) 1variable \n 2) variable1 \n 3) var-iable", "2", "variable1"),
    ("How do you start a while loop in Python?", "while"),
    ("How do you write an if statement in Python?", "if"),
    ("What is the output of print(10 // 3)?", "3"),
    ("Which of the following is used to define a block of code in Python? \n 1) { } \n 2) indentation \n 3) ( )", "2", "indentation"),
    ("How do you create a dictionary in Python?", "{'key': 'value'}", "dictionary"),
    ("How do you create a tuple in Python?", "(1, 2, 3)", "tuple"),
    ("What is the output of print(10 % 3)?", "1"),
    ("Which keyword is used to create a class in Python?", "class"),
    ("Which of the following is used to handle exceptions in Python? \n 1) try/except \n 2) catch/throw \n 3) do/while", "1", "try/except"),
    ("What is the output of print(3 == 3)?", "True"),
    ("Which of the following is not a keyword in Python? \n 1) pass \n 2) eval \n 3) assert", "2", "eval"),
    ("Which function is used to get the length of a list in Python?", "len"),
    ("What is the output of print('Hello' + ' ' + 'World')?", "Hello World"),
    ("How do you convert a string to an integer in Python?", "int()"),
    ("Which function is used to read input from the user in Python?", "input"),
    ("What is the output of print(type([]))?", "<class 'list'>"),
    ("How do you create a set in Python?", "{1, 2, 3}", "set"),
    ("Which operator is used for exponentiation in Python?", "**"),
    ("How do you create a lambda function in Python?", "lambda")
]


for question, *correct_answers in questions:
    user_answer = input(question + "\n").lower()
    if user_answer in [ans.lower() for ans in correct_answers]:
        print("Correct!")
        score += 1
    else:
        print("Wrong")
        
    print(f"Your score is {score}/{len(questions)}")

print(f"Your final score is {score}/{len(questions)}")