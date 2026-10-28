print("Welcome to Career Compass!")

print("What brings you here today?")
print("Tell me a little about what you're hoping to accomplish.\n")

print("1. Explore careers")
print("2. Find a new job")
print("3. Build new skills")
print("4. Something else")

choice = input("\nEnter your choice (1-4): ")

if choice == "1":
    print("\nGreat! Let's explore careers.")

elif choice == "2":
    print("\nAwesome! Let's find a new job.")

elif choice == "3":
    print("\nLet's build new skills.")

elif choice == "4":
    print("\nTell me more about what brings you here today.")

else:
    print("\nPlease select a valid option.")
