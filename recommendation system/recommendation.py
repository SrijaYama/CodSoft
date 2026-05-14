print("BOOK RECOMMENDATION SYSTEM")

books = {
    "story": ["Wings of Fire", "Harry Potter", "The Alchemist"],
    "science": ["Brief History of Time", "Physics Basics", "Space Science"],
    "programming": ["Python Basics", "Java Programming", "C Programming"],
    "motivation": ["Think Positive", "Rich Dad Poor Dad", "Atomic Habits"]
}

while True:

    print("\nChoose Category")
    print("1. Story Books")
    print("2. Science Books")
    print("3. Programming Books")
    print("4. Motivation Books")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Recommended Books:")
        for i in books["story"]:
            print("-", i)

    elif choice == "2":
        print("Recommended Books:")
        for i in books["science"]:
            print("-", i)

    elif choice == "3":
        print("Recommended Books:")
        for i in books["programming"]:
            print("-", i)

    elif choice == "4":
        print("Recommended Books:")
        for i in books["motivation"]:
            print("-", i)

    elif choice == "5":
        print("Thank You")
        break

    else:
        print("Invalid Choice")