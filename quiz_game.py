print("Welcome to Python Quiz Game! \n This is a simple program made by me to help me study Python tracking a score wich I can use to improve my skills. \n")

playing = input("Are you ready? (y/n) ")
level = input("Choose your level: \n 1) easy, \n 2) medium, \n 3) hard \n")

if playing.lower() != 'y':
    print("Ok, take your time")
    quit()
    
    

score = 0

questions = [
    ("What is the output of print(2 ** 3)?", "8"),
    ("Which of the following is a Python data type? \n 1) list \n 2) array \n 3) function", "1", "list"),
    ("How do you insert comments in Python code?", "#"),
    ("Which keyword is used to define a function in Python?", "def"),
    ("How do you create a variable with the floating number 2.8? use x", "x = 2.8"),
    ("What is the correct file extension for Python files?", ".py"),
    ("How do you create a list in Python? use 1,2,3", "[1, 2, 3]", "list"),
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

questionsMedium = [
    ("What is the output of print('Python'[1])?", "y"),
    ("How do you access the last element of a list 'lst'?", "lst[-1]"),
    ("Which method can be used to convert a string to all uppercase in Python?", "upper"),
    ("What is the result of the expression '5 + 2 * 3' in Python?", "11"),
    ("How do you check if a key exists in a dictionary 'd'?", "'key' in d"),
    ("What does the 'break' statement do in a loop?", "exits the loop", "terminates the loop"),
    ("What does the 'continue' statement do in a loop?", "skips to the next iteration", "skips the rest of the code inside the loop for the current iteration"),
    ("How do you import a specific function 'func' from a module 'mod'?", "from mod import func"),
    ("What is a lambda function in Python?", "anonymous function", "a function defined with the lambda keyword"),
    ("How do you handle multiple exceptions in a single 'except' block?", "by using a tuple of exceptions"),
    ("What is the purpose of the 'global' keyword in Python?", "to declare a global variable inside a function"),
    ("How do you create a virtual environment in Python?", "python -m venv env"),
    ("What is a decorator in Python?", "a function that modifies the behavior of another function"),
    ("What is the output of print('a' * 3)?", "aaa"),
    ("How do you merge two dictionaries 'dict1' and 'dict2' in Python 3.9+?", "{**dict1, **dict2}"),
    ("What is the purpose of the 'nonlocal' keyword in Python?", "to modify a variable in the nearest enclosing scope"),
    ("How do you read a file line by line in Python?", "with open('file.txt') as f: for line in f:"),
    ("What is the difference between '==' and 'is' in Python?", "'==' checks for value equality, 'is' checks for identity"),
    ("How do you create a set comprehension in Python?", "{x for x in range(10)}"),
    ("What is the purpose of the '__init__.py' file in a Python package?", "to mark a directory as a Python package"),
    ("What is the output of print(list(map(str, [1, 2, 3])))?", "['1', '2', '3']"),
    ("How do you convert a list of tuples '[(1, 2), (3, 4)]' to a dictionary?", "dict([(1, 2), (3, 4)])"),
    ("What is the purpose of the 'yield' keyword in Python?", "to create a generator"),
    ("How do you define a class method in Python?", "with the @classmethod decorator"),
    ("What is the output of print(bool('False'))?", "True"),
    ("How do you reverse a list 'lst' in Python?", "lst[::-1]", "lst.reverse()"),
    ("How do you check the type of an object 'obj' in Python?", "type(obj)"),
    ("What is the purpose of the 'self' keyword in a class?", "to refer to the instance of the class"),
    ("How do you catch multiple exceptions in a single 'except' block?", "except (Exception1, Exception2):"),
    ("What is the output of print(','.join(['a', 'b', 'c']))?", "a,b,c"),
    ("What is the purpose of the 'with' statement in Python?", "to wrap the execution of a block with methods defined by a context manager")
]

questionsHard = [
    ("What is the purpose of the '__call__' method in a Python class?", "to make an instance callable"),
    ("What is the output of print([i for i in range(5)])?", "[0, 1, 2, 3, 4]"),
    ("What does the '@staticmethod' decorator do in Python?", "defines a static method"),
    ("How do you perform matrix multiplication using NumPy?", "numpy.dot(a, b)", "a @ b"),
    ("What is the output of print({1, 2, 3} & {2, 3, 4})?", "{2, 3}"),
    ("How do you remove duplicates from a list 'lst'?", "list(set(lst))"),
    ("What is the output of print(sorted([3, 1, 2]))?", "[1, 2, 3]"),
    ("How do you define an abstract base class in Python?", "with the abc module", "using ABCMeta as metaclass"),
    ("What is the difference between 'deepcopy' and 'copy'?", "'deepcopy' copies everything, 'copy' creates shallow copies"),
    ("How do you create a property in a class?", "with the @property decorator"),
    ("What is the purpose of the '__str__' method in a class?", "to define the string representation of an object"),
    ("What is the output of print(0.1 + 0.2 == 0.3)?", "False"),
    ("How do you install packages using pip?", "pip install package_name"),
    ("What is the purpose of the '__slots__' declaration in a class?", "to declare data members", "to prevent the creation of instance dictionaries"),
    ("How do you serialize an object in Python?", "using the pickle module", "pickle.dump()"),
    ("What is a context manager in Python?", "an object that defines the runtime context to be established when executing a 'with' statement"),
    ("What is the output of print('{:.2f}'.format(3.14159))?", "3.14"),
    ("How do you create a coroutine in Python?", "using the async def keyword"),
    ("What is the purpose of the '__enter__' and '__exit__' methods in a class?", "to define the behavior of a context manager"),
    ("What is a metaclass in Python?", "a class of a class that defines how a class behaves"),
    ("What is the purpose of the 'assert' statement?", "to test if a condition is true"),
    ("How do you measure the execution time of a code block?", "using the time module", "time.time()"),
    ("What is the output of print(3 < 5 < 7)?", "True"),
    ("How do you read and write to a binary file?", "using 'rb' and 'wb' modes in open()"),
    ("What is the purpose of the '__getitem__' method in a class?", "to define behavior for when an item is accessed"),
    ("What is the difference between 'old-style' and 'new-style' classes in Python?", "new-style classes inherit from 'object'"),
    ("How do you convert an iterator to a list?", "list(iterator)"),
    ("What is the purpose of the '__name__' variable?", "to determine if the module is being run as the main program"),
    ("How do you perform floor division?", "//"),
    ("What is the output of print(repr('Hello'))?", "'Hello'"),
    ("How do you catch all exceptions in Python?", "except Exception:")
]


if level == "easy" or level == "1" :
    print("Ok, let's start!")
    for question, *correct_answers in questions:
        user_answer = input(question + "\n").lower()
    if user_answer in [ans.lower() for ans in correct_answers]:
        print("Correct!")
        score += 1
    else:
        print("Wrong")
elif level == "medium" or level == "2":
    print("Ok, let's start!")
    for question, *correct_answers in questionsMedium:
        user_answer = input(question + "\n").lower()
        if user_answer in [ans.lower() for ans in correct_answers]:
            print("Correct!")
            score += 1
        else:
            print("Wrong")
elif level == "hard" or level == "3":
    print("Ok, let's start!")
    for question, *correct_answers in questionsHard:
        user_answer = input(question + "\n").lower()
        if user_answer in [ans.lower() for ans in correct_answers]:
            print("Correct!")
            score += 1
        else:
            print("Wrong")
else:
    print("Invalid level")  
    quit()
    
    print("Your score is {score}/{len(questionsMedium)}")
print("Your final score is {score}/{len(questions)}")
if score < 10:
    print("Too bad, you need to study more!")
elif 10 < score <= 20:
    print("Congratulations, you passed the test! But you can do better.")
else:
    print("Great job, you passed the test!")