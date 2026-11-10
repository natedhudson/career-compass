import random
user_profile = {
    "Income": 0,
    "Work_life_balance": 0,
    "Purpose": 0,
    "Job_security": 0,
    "Growth": 0,
    "Well-being": 0,
}


print("Welcome to Career Compass! Your next adventure starts here.")
print()
print("Pick an area for us to look at together. You can always come back and explore other areas later.")
print()

options = [
    "1. See what careers might be a good fit for me",
    "2. Take my career to the next level",
    "3. Trying to find a job",
    "4. Improve my resume",
    "5. Prepare for interviews",
    "6. Further my education",
    "7. I'm not sure"
]

for option in options:
    print(option)

print()

choice = input("> ").strip()

while choice not in ["1", "2", "3", "4", "5", "6", "7"]:
    print("Please enter a valid option (1-7).")
    choice = input("> ").strip()

print()

if choice == "1":
    print("There are plenty of options out there! Let's explore what careers might be a good fit for you.")
    print()
    print("What is motivating you to explore a new career?")
    print()
    print("1. I know I'm capable of more and want to earn more")
    print("2. Better work-life balance")
    print("3. My current work isn't meaningful to me")
    print("4. Greater job security")
    print("5. I've outgrown my current role and want a new challenge")
    print("6. My current work is negatively affecting my well-being")
    print()

answer = input("> ").strip()

while answer not in ["1", "2", "3", "4", "5", "6"]:
    print("Please enter a valid option (1-6).")
    answer = input("> ").strip()

print()

if answer == "1":
    user_profile["Income"] += 5

    print("""
Income appears to be a key motivator for you right now.

That helps us better understand what you're hoping to achieve in your career change.
    """)

elif answer == "2":
    user_profile["Work_life_balance"] += 5

    print("Work-life balance can have a huge impact on quality of life.")
    print()
    print("Let's explore careers known for flexibility.")

elif answer == "3":
    user_profile["Purpose"] += 5

    print("Meaningful work appears to be an important factor in your career search.")
    print()
    print("That's valuable to know as we continue exploring what a good career looks like for you.")

elif answer == "4":
    user_profile["Job_security"] += 5

    print("Job security is important in an uncertain economy.")
    print()
    print("Let's explore careers known for stability.")

elif answer == "5":
    user_profile["Growth"] += 5

    print("A new challenge can be an exciting opportunity for growth.")
    print()
    print("Let's explore careers that offer variety and advancement.")

elif answer == "6":
    user_profile["Well-being"] += 5

    print("When work begins affecting your well-being, it may be a sign that something needs to change.")
    print()
    print("Let's explore careers that may be a healthier long-term fit.") 

elif choice == "2":
    print("Now we're talking! Let's see what we can do to get you to the next level.")
    print()
    print("What would make you feel most successful one year from now?")
    print()
    print("1. Earning significantly more than I do today")
    print("2. Having more time and energy outside of work")
    print("3. Feeling that my work makes a meaningful difference")
    print("4. Feeling secure in my job and career path")
    print("5. Taking on new challenges and responsibilities")
    print("6. Feeling healthier and less stressed overall")
    print()

    answer = input("> ").strip()

    while answer not in ["1", "2", "3", "4", "5", "6"]:
        print("Please enter a valid option (1-6).")
        answer = input("> ").strip()

    print()

    if answer == "1":
        user_profile["Income"] += 5

        print("Improving your financial situation appears to be an important part of your definition of success.")
        print()
        print("Let's explore opportunities that can help increase your earning potential.")

    elif answer == "2":
        user_profile["Work_life_balance"] += 5

        print("Having more time and energy outside of work can have a meaningful impact on overall quality of life.")
        print()
        print("Let's explore opportunities that may provide greater balance and flexibility.")

    elif answer == "3":
        user_profile["Purpose"] += 5
        
        print("Making a meaningful contribution appeats to be an important to you.")
        print()
        print("Let's explore opportunities that align with the impact you'd like to have.")
        
    elif answer == "4":
        user_profile["Job_security"] += 5

        print("Feeling secure about your fuuture can provide confidence and peace of mind.")
        print()
        print("Let's explore opportunities that may provide greater stability and security.")
    
    elif answer == "5":
        user_profile["Growth"] += 5

        print("Continued growth and new challenges can be energizing and rewarding.")
        print()
        print("Let's explore opportunities that may provide new challenges and responsibilities.")
    
    elif answer == "6":
        user_profile["Well-being"] += 5

        print("Prioritizing your health and well-being is important for long-term success.")
        print()
        print("Let's explore opportunities that may provide a healthier work environment and reduce stress.")

elif choice == "3":
    print("Imagine you receive a job offer tomorrow.")
    print()
    print("What's the biggest reason you're smiling on the drive home?")
    print()
    print("1. The pay would open up new possibilities for me")
    print("2. I'd finally have a better balance between work and peronal life")
    print("3. The work feels like something I'd be proud to be part of")
    print("4. It feels like a secure step forward for my future")
    print("5. I'd have room to learn and grow and challenge myself")
    print("6. I think I'd be happier there")
    print()
    
    answer = input("> ").strip()

    while answer not in ["1", "2", "3", "4", "5", "6"]:
        print("Please enter a valid option (1-6).")
        answer = input("> ").strip()
    print()

    if answer == "1":
        user_profile["Income"] += 5

        print("It's easy to understand why that would put a smile on your face.")
        print()
        print("Let's look at opportunities that could make a meaningful difference in your finacial future.")

    elif answer == "2":
        user_profile["Work_life_balance"] += 5

        print("Work is important, but so is everthing waiting for you outside of it.")
        print()
        print("Let's get you in a job that gives you the best of both worlds.")

    elif answer == "3":
        user_profile["Purpose"] += 5

        print("It sounds like the work itself matters just as much as the paycheck.")
        print()
        print("Let's target that job that'll fulfill your sense of purpose.")

    elif answer == "4":
        user_profile["Job_security"] += 5

        print("It sounds like you're looking for something you can build on, not just something to get you by.")
        print()
        print("Let's track down companies that offer the security your future can depend on.")

    elif answer == "5":
        user_profile["Growth"] += 5

        print("New challenges often lead to new possibilities.")
        print()
        print("With energy like that, you have nowhere to go but up. Let's find a job that can help you grow and thrive.")


    elif answer == "6":
        user_profile["Well-being"] += 5

        print("Feeling happier and less stressed is a goal worth taking seriously.")
        print()
        print("Let's venture down a path that results in a healthier future.")
    
elif choice == "4":
    print("When it comes to your resume, what's the biggest challenge you're facing?")
    print()
    print("1. I don't have enough experience")
    print("2. I don't know if it's written well")
    print("3. I'm not getting interviews")
    print("4. I'm changing careers")
    print("5. I have gaps in my work history")
    print("6. I'm not sure")
    print()

    answer = input("> ").strip()

    while answer not in ["1", "2", "3", "4", "5", "6"]:
        print("Please enter a valid option (1-6).")
        answer = input("> ").strip()
    print()

    if answer == "1":
        print("Many people underestimate how much value their existing experience provides.")
        print()
        print("Let's identify skills and accomplishments you may be overlooking.")

    elif answer == "2":
        print("A strong resume is more than a list of jobs.")
        print()
        print("Let's look at how your experience is being presented.")

    elif answer == "3":
        print("If applications aren't leading to interviews, there may be opportunities to improve targeting and presentation.")
        print()
        print("Let's explore that further.")

    elif answer == "4":
        print("Career transitions can be challenging.")
        print()
        print("Let's identify transferable skills that can help tell your story.")

    elif answer == "5":
        print("Employment gaps are more common than many people realize.")
        print()
        print("Let's focus on presenting your experience with confidence.")

    elif answer == "6":
        print("That's okay.")
        print()
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
    print()

    answer = input("> ").strip()

    while answer not in ["1", "2", "3", "4", "5", "6"]:
        print("Please enter a valid option (1-6).")
        answer = input("> ").strip()
    print()

    if answer == "1":
        print("Interview nerves are more common than you might think.")
        print()
        print("Let's explore ways to help you feel more prepared and confident.")

    elif answer == "2":
        print("Difficult questions can feel intimidating.")
        print()
        print("Let's look at strategies that can help you answer with confidence.")

    elif answer == "3":
        print("Many people find it uncomfortable to talk about themselves.")
        print()
        print("Let's identify strengths and accomplishments that are worth highlighting.")

    elif answer == "4":
        print("You likely have more relevant experience than you realize.")
        print()
        print("Let's explore ways to communicate your skills and accomplishments clearly.")

    elif answer == "5":
        print("Understanding what employers value can make interviews feel much less overwhelming.")
        print()
        print("Let's take a closer look at what hiring managers are often looking for.")

    elif answer == "6":
        print("That's okay.")
        print()
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
    print()
    
    education_choice = input("> ").strip()

    while education_choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Please enter a valid option (1-6).")
        education_choice = input("> ").strip()
    print()

    if education_choice == "1":
        print("Short-term training can be a great way to develop valuable skills quickly.")
        print()
        print("Let's explore options that can help you reach your goals without a long-term commitment.")

    elif education_choice == "2":
        print("Trade and technical careers often provide hands-on learning and strong job opportunities.")
        print()
        print("Let's explore paths that match your interests and strengths.")

    elif education_choice == "3":
        print("A college degree can open doors to many career opportunities.")
        print()
        print("Let's explore educational paths that align with your long-term goals.")

    elif education_choice == "4":
        print("Continuing education can help you stay competitive and grow professionally.")
        print()
        print("Let's explore areas where you may want to develop new skills.")

    elif education_choice == "5":
        print("That's perfectly okay.")
        print()
        print("Many people begin by exploring different educational opportunities before choosing a direction.")

    elif education_choice == "6":
        print("That's okay.")
        print()
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
    print()

    answer = input("> ").strip()

    while answer not in ["1", "2", "3", "4", "5", "6"]:
        print("Please enter a valid option (1-6).")
        answer = input("> ").strip()
    print()

    if answer == "1":
        print("Finding a clear direction is exactly what Career Compass was designed to help with.")
        print()
        print("Let's explore your interests, strengths, and goals.")
    
    elif answer == "2":
        print("A better career fit can lead to greater satisfaction and long-term success.")
        print()
        print("Let's identify the type of work that aligns with who you are.")
        
    elif answer == "3":
        print("Growth often begins with understanding where you want to go next.")
        print()
        print("Let's explore opportunities that can help you move forward.")
        
    elif answer == "4":
        print("Your strengths can provide valuable clues about which careers may fit you best.")
        print()
        print("Let's uncover some of those strengths together.")
        
    elif answer == "5":
        print("Some of the best career opportunities are the ones we haven't considered yet.")
        print()
        print("Let's explore a few possibilities together.")
    
    elif answer == "6":
        print("That's completely okay.")
        print()
        print("Many people start with uncertainty, and clarity develops one step at a time.")

print()
print()
print()    
print()    
print("This section is still under construction.")
print()
print()
print()
print()

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
print()
print()
print()
print("User Profile")
print("------------")

for trait, score in user_profile.items():
    print(f"{trait}: {score}")
    print()
    print()

