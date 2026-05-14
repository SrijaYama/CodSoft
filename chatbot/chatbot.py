print("AI CHATBOT")

while True:

    user = input("You: ").lower()

    if "hi" in user or "hello" in user or "hey" in user:
        print("Bot: Hello Friend")

    elif "how are you" in user:
        print("Bot: I am fine")

    elif "your name" in user:
        print("Bot: My name is AI Bot")

    elif "python" in user:
        print("Bot: Python is easy to learn")

    elif "java" in user:
        print("Bot: Java is a programming language")

    elif "help" in user:
        print("Bot: I can answer simple questions")

    elif "time" in user:
        import time
        print("Bot:", time.strftime("%H:%M:%S"))

    elif "date" in user:
        import datetime
        print("Bot:", datetime.date.today())

    elif "+" in user:

        data = user.split("+")

        a = int(data[0])
        b = int(data[1])

        print("Bot:", a + b)

    elif "-" in user:

        data = user.split("-")

        a = int(data[0])
        b = int(data[1])

        print("Bot:", a - b)

    elif "*" in user:

        data = user.split("*")

        a = int(data[0])
        b = int(data[1])

        print("Bot:", a * b)

    elif "/" in user:

        data = user.split("/")

        a = int(data[0])
        b = int(data[1])

        if b != 0:
            print("Bot:", a / b)

        else:
            print("Bot: Cannot divide by zero")

    elif "good morning" in user:
        print("Bot: Good Morning")

    elif "good night" in user:
        print("Bot: Good Night")

    elif "thank you" in user:
        print("Bot: Welcome")

    elif "bye" in user:
        print("Exit")
        break

    else:
        print("Bot: That's interesting. Tell me more.")