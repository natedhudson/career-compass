import random

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

choice = input("> ").strip()

while choice not in ["1", "2", "3", "4", "5", "6", "7"]:
    print("Please enter a valid option (1-7).")
    choice = input("> ").strip()

print()

if choice == "1":
    print("What is motivating you to explore a new career?")
    print("1. Better income")
    print("2. Better work-life balance")
    print("3. More meaningful work")
    print("4. Greater job security")
    print("5. A new challenge")
    print("6. Burnout in my current field")

    answer = input("> ").strip()

    while answer not in ["1", "2", "3", "4", "5", "6"]:
        print("Please enter a valid option (1-6).")
        answer = input("> ").strip()

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

    answer = input("> ").strip()

    while answer not in ["1", "2", "3", "4", "5", "6"]:
        print("Please enter a valid option (1-6).")
        answer = input("> ").strip()

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

print()
print("How much additional education are you willing to pursue?")
print()
print("1. None")
print("2. Certification")
print("3. Associate Degree")
print("4. Bachelor's Degree")
print("5. Master's Degree")

education = input("> ").strip()

while education not in ["1", "2", "3", "4", "5"]:
    print("Please enter a valid option (1-5).")
    education = input("> ").strip()

print()
print("Which type of work sounds most appealing to you?")
print()
print("1. Solving problems")
print("2. Helping people")
print("3. Leading and organizing")
print("4. Building or repairing things")
print("5. Analyzing information")
print("6. Creating or designing")
print("7. I'm not sure")

work_type = input("> ").strip()

while work_type not in ["1", "2", "3", "4", "5", "6", "7"]:
    print("Please enter a valid option (1-7).")
    work_type = input("> ").strip()

print()
print("Imagine it's Monday morning and you're actually looking forward to work.")
print()
print("Which of these sounds most like the reason?")
print()
print("Select all that apply.")
print("Separate multiple answers with commas.")
print()
print("1. There's a challenge waiting for me")
print("2. I get to help people")
print("3. I get to work with good people")
print("4. I'll learn something new")
print("5. I'll build or create something real")
print("6. Every day is a little different")
print("7. I'm not sure")

reason = input("> ").strip()

valid_reasons = ["1", "2", "3", "4", "5", "6", "7"]

reason_list = [item.strip() for item in reason.split(",")]

duplicate_messages = [
    "Looks like you selected option {} more than once. I'll assume you're extra enthusiastic about that one.",
    "I noticed you picked option {} twice. I'm not counting it twice, but I admire the commitment.",
    "Option {} seems to have made quite an impression.",
    "I'll only count option {} once, but I appreciate the passion.",
    "Career Compass noticed option {} showed up more than once. Good choice."
]

duplicates = []

for item in reason_list:
    if reason_list.count(item) > 1 and item not in duplicates:
        duplicates.append(item)

for duplicate in duplicates:
    print()
    print(random.choice(duplicate_messages).format(duplicate))

reason_list = list(dict.fromkeys(reason_list))


while not all(item in valid_reasons for item in reason_list):
    print("Select all that apply, separated by commas.")
    print("Example: 1,4,5")
    reason = input("> ").strip()
    reason_list = [item.strip() for item in reason.split(",")]

print()
print("Thanks. I'm starting to get a better sense of what you're looking for.")
