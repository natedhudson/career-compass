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
print("So, what brings you here today?")
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
        
        print("Making a meaningful contribution appears to be an important to you.")
        print()
        print("Let's explore opportunities that align with the impact you'd like to have.")
        
    elif answer == "4":
        user_profile["Job_security"] += 5

        print("Feeling secure about your future can provide confidence and peace of mind.")
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
    print("2. I'd finally have a better balance between work and personal life")
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
        print("Let's look at opportunities that could make a meaningful difference in your financial future.")

    elif answer == "2":
        user_profile["Work_life_balance"] += 5

        print("Work is important, but so is everything waiting for you outside of it.")
        print()
        print("Let's get you in a job that gives you the best of both worlds.")

    elif answer == "3":
        user_profile["Purpose"] += 5

        print("It sounds like the work itself matters just as much as the paycheck.")
        print()
        print("Let's target the job that'll fulfill your sense of purpose.")

    elif answer == "4":
        user_profile["Job_security"] += 5

        print("It sounds like you're looking for something you can build on, not just something to get you by.")
        print()
        print("Let's track down companies that offer the security your future can depend on.")

    elif answer == "5":
        user_profile["Growth"] += 5

        print("New challenges often lead to new possibilities.")
        print()
        print("With energy like that, you have nowhere to go but up! Let's find a job that can help you grow and thrive.")


    elif answer == "6":
        user_profile["Well-being"] += 5

        print("Feeling happier and less stressed is a goal worth taking seriously.")
        print()
        print("Let's venture down a path that results in a healthier future.")
    
elif choice == "4":
    print("Imagine a hiring manager is looking at your resume right now.")
    print()
    print("What are you hoping they see?")
    print()
    print("1. Ambition and potential")
    print("2. Maturity and a healthy perspective on work")
    print("3. Purpose and enthusiasm")
    print("4. Reliability and commitment")
    print("5. Curiosity and a desire to grow")
    print("6. Self-awareness and healthy priorities")
    print()

    answer = input("> ").strip()

    while answer not in ["1", "2", "3", "4", "5", "6"]:
        print("Please enter a valid option (1-6).")
        answer = input("> ").strip()
    print()

    if answer == "1":
        user_profile["Income"] += 5

        print("Many people have more potential than their resume currently shows.")
        print()
        print("That's an important thing to keep in mind moving forward.")

    elif answer == "2":
        user_profile["Work_life_balance"] += 5

        print("Work is only one part of a well-lived life.")
        print()
        print("That's a valuable perspective to bring into a job search.")

    elif answer == "3":
        user_profile["Purpose"] += 5

        print("It's not just about finding a job.")
        print()
        print("Finding work that matters to you, keeps you engaged.")

    elif answer == "4":
        user_profile["Job_security"] += 5

        print("It sounds like you're thinking beyond your next job and focusing on your future.")
        print()
        print("That's an important consideration.")

    elif answer == "5":
        user_profile["Growth"] += 5

        print("Growth often begins with curiosity.")
        print()
        print("That's a valuable trait to carry into any opportunity.")

    elif answer == "6":
        user_profile["Well-being"] += 5

        print("A career should support life, not compete with it.")
        print()
        print("I'm glad you called that out!")

elif choice == "5":
    print("As you prepare for this interview, what outcome matters most to you?")
    print()
    print("1. An opportunity that could improve my financial future")
    print("2. A position that would better fit my life outside of work")
    print("3. The chance to do work I can genuinely feel good about")
    print("4. A position I can see myself in years from now")
    print("5. An opportunity to continue learning and  growing")
    print("6. A role that supports the life I want to build")
    print()

    answer = input("> ").strip()

    while answer not in ["1", "2", "3", "4", "5", "6"]:
        print("Please enter a valid option (1-6).")
        answer = input("> ").strip()
    print()

    if answer == "1":
       user_profile["Income"] += 5

       print("A stronger financial future can create opportunities in many areas of life")
       print()
       print("That's an important goal to keep in mind.")

    elif answer == "2":
        user_profile["Work_life_balance"] += 5

        print("The best opportunities don't just fit your career goals.")
        print()
        print("They fit your life as well.")

    elif answer == "3":
        user_profile["Purpose"] += 5

        print("Doing work you genuinely believe in can make a big difference in day-to -day satisfaction.")
        print()
        print("That's worth paying attention to.")

    elif answer == "4":
        user_profile["Job_security"] += 5

        print("It sounds like you're thinking about the long game, not just the next step.")
        print()
        print("That's a valuable perspective to have.")

    elif answer == "5":
        user_profile["Growth"] += 5

        print("You seem motivated by progress and the chance to keep moving forward.")
        print()
        print("That's a powerful mindset to bring into any opportunity.")

    elif answer == "6":
        user_profile["Well-being"] += 5

        print("A career should support the life you're trying to build.")
        print()
        print("I'm glad you called that out.")

elif choice == "6":
    print("As you think about furthering your education, what's the biggest reward you are looking for?")
    print()
    print("1. New financial opportunities")
    print("2. More freedom and flexibility")
    print("3. Work that feels meaningful")
    print("4. Greater stability and security")
    print("5. Personal and personal growth")
    print("6. A healthier and more fulfilling life")
    print()
    
    education_choice = input("> ").strip()

    while education_choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Please enter a valid option (1-6).")
        education_choice = input("> ").strip()
    print()

    if education_choice == "1":
        user_profile["Income"] += 5

        print("Education is often an investment in future opportunities.")
        print()
        print("It's helpful to know that financial growth is an important goal for you.")

    elif education_choice == "2":
        user_profile["Work_life_balance"] += 5

        print("Success isn't only measured by what you earn.")
        print()
        print("Having more freedom and flexibility can be just as valuable.")

    elif education_choice == "3":
        user_profile["Purpose"] += 5

        print("Feeling like work has purpose matters to a lot of people.")
        print()
        print("It sounds like it matters to you as well.")

    elif education_choice == "4":
        user_profile["Job_security"] += 5

        print("Many people pursue education because they're think about the future.")
        print()
        print("Stability and security are powerful motivators.")

    elif education_choice == "5":
        user_profile["Growth"] += 5

        print("You seem motivated be the opportunity to keep learning and developing.")
        print()
        print("That's a valuable mindset to carry forward.")

    elif education_choice == "6":
        user_profile["Well-being"] += 5

        print("A good career should support the life you're trying to build.")
        print()
        print("That's worth keeping in mind.")

elif choice == "7":
    print("That's okay. Many people come to Career Compass because they're looking for clarity.")
    print()
    print("Which of these sounds most like what you're looking for?")
    print()
    print("1. A clearer picture of how to improve my financial future")
    print("2. More balance between work and the rest of my life")
    print("3. Work that feels purposeful and worthwhile")
    print("4. More confidence about my future")
    print("5. Opportunities to learn and grow")
    print("6. A career that feels like a better fit overall")
    print()

    answer = input("> ").strip()

    while answer not in ["1", "2", "3", "4", "5", "6"]:
        print("Please enter a valid option (1-6).")
        answer = input("> ").strip()
    print()

    if answer == "1":
        user_profile["Income"] += 5

        print("A stronger financial future can open the door to new possibilities.")
        print()
        print("It's helpful to know that's important to you.")
    
    elif answer == "2":
        user_profile["Work_life_balance"] += 5

        print("Finding balance can have a huge impact on overall quality of life.")
        print()
        print("It's helpful to know that's what you're looking for.")
        
    elif answer == "3":
        user_profile["Purpose"] += 5

        print("Meaningful work can make a big difference in long-term satisfaction.")
        print()
        print("That's a valuable thing to understand about yourself.")
        
    elif answer == "4":
        user_profile["Job_security"] += 5

        print("Wanting more confidence about the future is completely understandable.")
        print()
        print("We'll keep that in mind as we continue.")
        
    elif answer == "5":
        user_profile["Growth"] += 5

        print("It sounds like you're motivated by learning and continuous improvement.")
        print()
        print("That's a valuable quality to build on.")
    
    elif answer == "6":
        user_profile["Well-being"] += 5

        print("Finding a career that feels like a better fit can positively affect many areas of life.")
        print()
        print("Sounds like you have an understanding of what you need to be the best you!")

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

