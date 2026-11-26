import random

def get_valid_input(valid_options, error_message):
    answer = input("> ").strip()

    while answer not in valid_options:
        print(error_message)
        answer = input("> ").strip()

    return answer

user_profile = {
    "Income": 0,
    "Work_life_balance": 0,
    "Purpose": 0,
    "Job_security": 0,
    "Growth": 0,
    "Well-being": 0,
}

user_needs = {}


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

choice = get_valid_input(
    ["1", "2", "3", "4", "5", "6", "7"],
    "Please enter a valid option (1-7)."
)

print()

if choice == "1":
    print("There are plenty of options out there!")
    print()
    print("Let's explore what careers might be a good fit for you.")
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

answer = get_valid_input(
    ["1", "2", "3", "4", "5", "6"],
    "Please enter a valid option (1-6)."
)

print()

if answer == "1":
    user_profile["Income"] += 5

    print("""

Income appears to be a key motivator for you right now.

That helps us better understand what you're hoping to achieve in your career change.

Now let's look at what's making that goal harder to reach.

What's the biggest thing standing between you and earning more today?

1. I don't know what careers pay more
2. I don't have the right skills
3. I don't know what opportunities are available
4. I feel stuck in my current path
5. I don't know where to start
6. I haven't figured that out yet

""")

    need = get_valid_input(
    ["1", "2", "3", "4", "5", "6"],
    "Please enter a valid option (1-6)."
)

    print()

    if need == "1":
        user_needs["Income"] = "career_information"

        print("""

That's completely understandable.

Many people know they want to earn more but aren't sure which careers offer strong earning potential.

""")
        
    elif need == "2":
        user_needs["Income"] = "skills_gap"

        print("""

That's a common concern when considering a career change.
    
Many higher-paying opportunities become more accessible as people build new skills and experience.
    
    """)

    elif need == "3":
        user_needs["Income"] = "opportunity_awareness"

        print("""

That's completely understandable.
                    
There may be more opportunities available than you realize.
    
Sometimes the challenge isn't a lack of options, but knowing where to look.
    
    """)

    elif need == "4":
        user_needs["Income"] = "career_stagnation"

        print("""
        
Feeling stuck can make it difficult to see what comes next.
    
The good news is that many skills and experiences can transfer into new career paths.
    
    """)

    elif need == "5":
        user_needs["Income"] = "starting_point"

        print("""
        
Starting can often be the hardest part.
    
Breaking a large goal into smaller steps can make the path forward much clearer.

""")

    elif need == "6":
        user_needs["Income"] = "unclear"

        print("""
        
That's completely okay.

Many people know they want something different before they've figured out exactly what's standing in their way.

""")
        
elif answer == "2":
    user_profile["Work_life_balance"] += 5

    print("Work-life balance appears to be a key motivator for you right now.")
    print()
    print("That helps us better understand what you're hoping to improve in you career.")
    print()
    print("Now let's look at what would improve your work-life balance the most.")
    print("""
    
1. More time for family and friends
2. More time to rest and recharge
3. Less stress outside of work
4. More flexibility in my schedule
5. Better alignment between work and personal life
6. I'm not sure

""")
answer = get_valid_input(
    ["1", "2", "3", "4", "5", "6"],
    "Please enter a valid option (1-6)."
)

print()