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

elif choice == "2":
    print("What would advancing your career look like for you?")
    print("1. Earning more money")
    print("2. Getting promoted")
    print("3. Moving into leadership")
    print("4. Learning new skills")
    print("5. Changing departments")
    print("6. I'm not sure")
    answer = input("> ")

elif choice == "3":
    print("What best describes your current situation?")
    print("1. Recently unemployed")
    print("2. Looking for my first job")
    print("3. Employed but looking elsewhere")
    print("4. Returning to the workforce")
    print("5. Contract ending soon")
    answer = input("> ")

elif choice == "4":
    print("What is your primary goal for your resume?")
    print("1. Get more interviews")
    print("2. Change careers")
    print("3. Apply for promotions")
    print("4. Enter a new field")
    print("5. Create my first professional resume")
    answer = input("> ")

elif choice == "5":
    print("What stage are you currently in?")
    print("1. I haven't applied yet")
    print("2. I have applications submitted")
    print("3. I have an upcoming interview")
    print("4. I've interviewed before but struggle with them")
    answer = input("> ")

elif choice == "6":
    print("What are you hoping education will help you accomplish?")
    print("1. Qualify for a new career")
    print("2. Advance my current career")
    print("3. Increase my income")
    print("4. Gain specialized skills")
    print("5. Complete a degree")
    print("6. Explore my interests")
    answer = input("> ")

elif choice == "7":
    print("Which statement sounds most like you?")
    print("1. I feel stuck")
    print("2. I need better income")
    print("3. I don't know what careers fit me")
    print("4. I'm unhappy in my current job")
    print("5. I want direction")
    print("6. I'm exploring possibilities")
    answer = input("> ")

else:
    print("Sorry, I didn't understand that choice.")
    answer = None

print()
print("Thank you for sharing.")
