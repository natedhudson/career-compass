import random

print("Welcome to Career Compass! Your next adventure starts here.")
print()
print("Pick an area for us to look at together. You can always come back and explore other areas later.")
print()
print("1. See what careers might be a good fit for me")
print("2. Take my career to the next level")
print("3. Trying to find a job")
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
    print("Now we're talking! Let's explore what careers might be a good fit for you.")

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


    print()

    if answer == "1":
        print("Higher income is a common reason people explore new careers.")
        print("Let's look at careers with strong earning potential.")
        print("We'll also explore ways to increase your earning potential in your current field.")
        print("Are you looking to further your education to increase your earning potential?")

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

elif choice == "3":
    print("What part of the job search is most challenging right now?")
    print()
    print("1. Finding positions to apply for")
    print("2. Getting interviews")
    print("3. Not having enough experience")
    print("4. Knowing what jobs fit me")
    print("5. Staying motivated")
    print("6. I'm not sure")

    answer = input("> ").strip()

    while answer not in ["1", "2", "3", "4", "5", "6"]:
        print("Please enter a valid option (1-6).")
        answer = input("> ").strip()

    print()
    print("Thank you for sharing.")
    print()

    if answer == "1":
        print("Finding opportunities is often the first hurdle.")
        print("Let's identify industries and roles that match your interests.")

    elif answer == "2":
        print("Getting interviews often comes down to resume quality and targeting.")
        print("Let's explore ways to increase your response rate.")

    elif answer == "3":
        print("Many employers value skills and potential as much as experience.")
        print("Let's look at ways to build credibility and confidence.")

    elif answer == "4":
        print("That's exactly what Career Compass is designed to help with.")
        print("Let's continue exploring your strengths and interests.")

    elif answer == "5":
        print("Job searching can be exhausting.")
        print("Let's break the process into manageable steps.")

    elif answer == "6":
        print("That's okay.")
        print("We'll keep exploring until a clearer direction emerges.")
    
elif choice == "4":
    print("When it comes to your resume, what's the biggest challenge you're facing?")
    print()
    print("1. I don't have enough experience")
    print("2. I don't know if it's written well")
    print("3. I'm not getting interviews")
    print("4. I'm changing careers")
    print("5. I have gaps in my work history")
    print("6. I'm not sure")

    answer = input("> ").strip()

while answer not in ["1", "2", "3", "4", "5", "6"]:
    print("Please enter a valid option (1-6).")
    answer = input("> ").strip()

if answer == "1":
    print("Many people underestimate how much value their existing experience provides.")
    print("Let's identify skills and accomplishments you may be overlooking.")

elif answer == "2":
    print("A strong resume is more than a list of jobs.")
    print("Let's look at how your experience is being presented.")

elif answer == "3":
    print("If applications aren't leading to interviews, there may be opportunities to improve targeting and presentation.")
    print("Let's explore that further.")

elif answer == "4":
    print("Career transitions can be challenging.")
    print("Let's identify transferable skills that can help tell your story.")

elif answer == "5":
    print("Employment gaps are more common than many people realize.")
    print("Let's focus on presenting your experience with confidence.")

elif answer == "6":
    print("That's okay.")
    print("We'll work together to identify what may be holding your resume back.")

elif choice == "5":
    print("What concerns you most about interviewing?")
    print()
    print("1. I get nervous during interviews")
    print("2. I don't know how to answer difficult questions")
    print("3. I struggle talking about myself")
    print("4. I'm not sure how to talk about my experience")
    print("5. I don't know what employers are looking for")
    print("6. I'm not sure")

    answer = input("> ").strip()

while answer not in ["1", "2", "3", "4", "5", "6"]:
    print("Please enter a valid option (1-6).")
    answer = input("> ").strip()

if answer == "1":
    print("Interview nerves are more common than you might think.")
    print("Let's explore ways to help you feel more prepared and confident.")

elif answer == "2":
    print("Difficult questions can feel intimidating.")
    print("Let's look at strategies that can help you answer with confidence.")

elif answer == "3":
    print("Many people find it uncomfortable to talk about themselves.")
    print("Let's identify strengths and accomplishments that are worth highlighting.")

elif answer == "4":
    print("You likely have more relevant experience than you realize.")
    print("Let's explore ways to communicate your skills and accomplishments clearly.")

elif answer == "5":
    print("Understanding what employers value can make interviews feel much less overwhelming.")
    print("Let's take a closer look at what hiring managers are often looking for.")

elif answer == "6":
    print("That's okay.")
    print("We'll work together to identify areas where you can build confidence.")

elif choice == "6":
    print("What type of education are you interested in pursuing?")
    print()
    print("1. Short-term courses or certifications")
    print("2. Trade or technical school")
    print("3. College degree (Associate, Bachelor's, or higher)")
    print("4. professional development or continuing education")
    print("5. I'm exploring my options")
    print("6. I'm not sure")

    education_choice = input("> ").strip()

if education_choice == "1":
    print("Short-term training can be a great way to develop valuable skills quickly.")
    print("Let's explore options that can help you reach your goals without a long-term commitment.")

elif education_choice == "2":
    print("Trade and technical careers often provide hands-on learning and strong job opportunities.")
    print("Let's explore paths that match your interests and strengths.")

elif education_choice == "3":
    print("A college degree can open doors to many career opportunities.")
    print("Let's explore educational paths that align with your long-term goals.")

elif education_choice == "4":
    print("Continuing education can help you stay competitive and grow professionally.")
    print("Let's explore areas where you may want to develop new skills.")

elif education_choice == "5":
    print("That's perfectly okay.")
    print("Many people begin by exploring different educational opportunities before choosing a direction.")

elif education_choice == "6":
    print("That's okay.")
    print("We'll work together to identify educational options that may fit your goals and interests.")

elif choice == "7":
    print("That's okay. Many people come to Career Compass because they're looking for clarity.")
    print()
    print("Which of these sounds most like what you're looking for?")
    print()
    print("1. A clearer sense of direction")
    print("2. A career that's a better fit")
    print("3. More opportunities to grow")
    print("4. A better understanding of my strengths")
    print("5. Possibilities I haven't considered")
    print("6. I'm not sure")
    
    
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

while not all(item in valid_reasons for item in reason_list):
    print("Select all that apply, separated by commas.")
    print("Example: 1,4,5")
    reason = input("> ").strip()
    reason_list = [item.strip() for item in reason.split(",")]

duplicates = []

duplicate_messages = [
    "Looks like you selected option {} more than once. I'll assume you're extra enthusiastic about that one.",
    "I noticed you picked option {} twice. I'm not counting it twice, but I admire the commitment.",
    "Option {} seems to have made quite an impression.",
    "I'll only count option {} once, but I appreciate the passion.",
    "Career Compass noticed option {} showed up more than once. Good choice."
]

for item in reason_list:
    if reason_list.count(item) > 1 and item not in duplicates:
        duplicates.append(item)

for duplicate in duplicates:
    print()
    print(random.choice(duplicate_messages).format(duplicate))

reason_list = list(dict.fromkeys(reason_list))

print()
print("Thanks. I'm starting to get a better sense of what you're looking for.")
