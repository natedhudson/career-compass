
print("Welcome to Career Compass!")
print()
print("What brings you here today?")
print()
print("1. Explore a new career")
print("2. Advance my career")
print("3. Find a job")
print("4. Improve my resume")
print("5. Prepare for interviews")
print("6. Further my education")
print("7. I'm not sure")
print()

choice = input("> ")

print()

if choice == "1":
    print("What is motivating you to explore a new career?")
    print("1. Better income")
    print("2. Better work-life balance")
    print("3. More meaningful work")
    print("4. Greater job security")
    print("5. A new challenge")
    print("6. Burnout in my current field")

    answer = input("> ")

    print()
    print("Thank you for sharing.")
    print()

    if answer == "1":
        print("Higher income is a common reason people explore new careers.")
        print("Let's look at careers with strong earning potential.")
    
    elif answer == "2":
        print("Work-life balance can have a huge impact on quality of life.")
        print("Let's explore careers known for flexibility.")

    elif answer == "3":
        print("Many people want work that feels purposeful and rewarding.")
        print("Let's explore careers that align with your values.")

    elif answer == "4":
        print("Job security is important in an uncertain economy.")
        print("Let's look at stable and growing industries.")

    elif answer == "5":
        print("A new challenge can be an exciting opportunity for growth.")
        print("Let's explore careers that offer variety and advancement.")

    elif answer == "6":
        print("Burnout is a sign that something may need to change.")
        print("Let's explore careers that may be a better long-term fit.")

elif choice == "2":
    print("What would advancing your career look like for you?")
    print("1. Earning more money")
    print("2. Getting promoted")
    print("3. Moving into leadership")
    print("4. Learning new skills")
    print("5. Changing departments")
    print("6. I'm not sure")

    answer = input("> ")

    print()
    print("Thank you for sharing.")
    print()

    if answer == "1":
        print("Increasing your income often begins with developing valuable skills.")

    elif answer == "2":
        print("Promotions usually come from demonstrating impact and leadership.")

    elif answer == "3":
        print("Leadership roles often require both technical and people skills.")

    elif answer == "4":
        print("Learning new skills can create opportunities for advancement.")

    elif answer == "5":
        print("Changing departments can help you find work that suits your strengths.")

    elif answer == "6":
        print("That's okay. Let's continue exploring your options.")

else:
    print("This section is still under construction.")
