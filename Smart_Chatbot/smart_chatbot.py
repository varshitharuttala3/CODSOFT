import random

def welcome():
    print("\n✨ Hey Rockstar! Welcome to YouthBot 2.0 ✨")
    print("“Dream big. Start small. Act now.” 🚀")
    print("Let’s vibe productively today!\n")

def choose_theme():
    print("Choose your theme:")
    print("1. Light Mode ☀️")
    print("2. Dark Mode 🌙")
    choice = input("Enter choice (1/2): ")
    
    if choice == "1":
        print("\n☀️ Light Mode Activated! Bright ideas incoming!\n")
    else:
        print("\n🌙 Dark Mode Activated! Cool mode ON.\n")

def main_menu():
    print("\nWhat’s your vibe today?")
    print("1. Research Help 📚")
    print("2. Project Help 💻")
    print("3. Chill With Me 😎")
    print("4. Play Games 🎮")
    return input("Choose an option (1-4): ")

def research_help():
    print("\n📚 Research Mode Activated!")
    topic = input("Tell me your topic: ")
    print(f"\nNice choice! '{topic}' sounds interesting.")
    print("Tip: Break your research into Introduction, Methods, Results, Conclusion.")
    print("Stay curious. Stay unstoppable. 🔥")

def project_help():
    print("\n💻 Project Genius Mode!")
    idea = input("What project are you working on? ")
    print(f"\nAwesome! '{idea}' can be structured like this:")
    print("1. Problem Statement")
    print("2. Solution Approach")
    print("3. Implementation")
    print("4. Results")
    print("Go build something legendary 🚀")

def chill_mode():
    jokes = [
        "Why did the developer go broke? Because he used up all his cache! 😂",
        "AI won’t take your job… but someone using AI might 😉",
        "Trust the process. Even WiFi reconnects automatically!"
    ]
    print("\n😎 Chill Mode Activated!")
    print(random.choice(jokes))

def number_guess_game():
    print("\n🎯 Guess the Number (1-10)")
    number = random.randint(1,10)
    guess = int(input("Your guess: "))
    if guess == number:
        print("Boom! You nailed it! 🔥")
    else:
        print(f"Close one! It was {number}. Try again later 😉")

def npat_game():
    print("\n📝 Name-Place-Animal-Thing Game")
    letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    print(f"Your letter is: {letter}")
    input("Enter a Name: ")
    input("Enter a Place: ")
    input("Enter an Animal: ")
    input("Enter a Thing: ")
    print("Nice creativity! Brain cells activated 🧠✨")

def tic_tac_toe():
    print("\n🎮 Mini Tic-Tac-Toe (Basic Version)")
    print("Board positions:")
    print("0 | 1 | 2")
    print("3 | 4 | 5")
    print("6 | 7 | 8")
    print("This is a demo mini version 😉")

def games_menu():
    print("\n🎮 Game Zone!")
    print("1. Guess The Number")
    print("2. Name-Place-Animal-Thing")
    print("3. Tic-Tac-Toe Demo")
    choice = input("Choose a game (1-3): ")

    if choice == "1":
        number_guess_game()
    elif choice == "2":
        npat_game()
    elif choice == "3":
        tic_tac_toe()
    else:
        print("Oops! Wrong choice.")

# MAIN PROGRAM
welcome()
choose_theme()

while True:
    choice = main_menu()

    if choice == "1":
        research_help()
    elif choice == "2":
        project_help()
    elif choice == "3":
        chill_mode()
    elif choice == "4":
        games_menu()
    else:
        print("Hmm... that wasn’t on the list 😅")

    again = input("\nDo you want to continue? (yes/no): ").lower()
    if again != "yes":
        print("\nStay productive. Stay awesome. Bye Rockstar! ✨")
        break
