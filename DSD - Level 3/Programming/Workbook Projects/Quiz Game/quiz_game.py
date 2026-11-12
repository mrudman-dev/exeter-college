# Variables
score = 0

#Introduction

print("Hello there, welcome to the Gamer Quiz. May I have your name?")
plr_name = input("Your name: ")
print(f"Nice, let's get this started. Good Luck {plr_name}!")

# Test question

hobby = input("\n First for all, what is your hobby: ")
print(f"That's a good hobby!  {hobby} sounds fun!")

# Instructions
def quiz_instructions():
    print("===== HOW TO PLAY THE QUIZ =====")
    print("This is a 5 questions quiz based on different variety subtopics in gaming.")
    print("Each question contains 4 choices (ABCD) and each one correct answer is 1 point.")
    print("You may use an internet to assist you if you are stuck.")
    print("Ideally, this quiz is based on gamer knowledge and years of experience.. it is recommended to have some experience before doing this quiz")
    print("\n You may now begin the quiz.")

# End Quiz Function
def display_results():
    print(f"End of the quiz | Final Score: {score}/5!")

    if score == 5:
        print(f"What an outstanding score {plr_name}! You're so smart!")
    elif score >= 3:
        print(f"Nice try {plr_name}!")
    else:
        print(f"Better luck next time, {plr_name}!")

    percentage = (score / 5) * 100
    print(f"ANSWER ACCURACY: {percentage}%")


# Checking if user definitely is playing
print(f"=== REQUIRED INPUT ===")
start = input("Please type either 'yes' or 'no' if you would like to start: ")

quiz_instructions()

while start != "yes":
    print("Invalid input, please use either 'yes' or 'no' ")
    start = input("Please type either 'yes' or 'no' if you would like to start: ")
    if start == "no": 
        exit()

# Start of the quiz
print("\n [Q1] | What is the term used to describe someone sweating over a game?")

print("=== CHOICES ===")
print("[A] - Grass Toucher")
print("[B] - Nerd")
print("[C] - John Doe")
print("[D] - Sweat")

response = input("\n My choice (A/B/C/D): ").upper()
if response == "D":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The answer was 'Sweat'")


print("\n [Q2] | Can PC gamers cheat on games?")

print("=== CHOICES ===")
print("[A] - No")
print("[B] - Yes")
print("[C] - Only if they are not touching grass")
print("[D] - Never")

response = input("\n My choice (A/B/C/D): ").upper()

if response == "B":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The answer was 'yes'")


print("\n [Q3] | Which is better, Fortnite or Minecraft?")

print("=== CHOICES ===")
print("[A] - Minecraft")
print("[B] - Clash of Clans")
print("[C] - Fortnite")
print("[D] - Neither")

response = input("\n My choice (A/B/C/D): ").upper()

if response == "C":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The answer was 'fortnite'")

print("\n [Q4] | What's the main character in minecraft?")

print("=== CHOICES ===")
print("[A] - Steve ")
print("[B] - Bobmaster123")
print("[C] - Man")
print("[D] - Alex")

response = input("\n My choice (A/B/C/D): ").upper()

if response == "A":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The answer was 'Steve'")

print("\n [Q5] | Who won the Fortnite World Cup in 2019 with £3 million?")

print("=== CHOICES ===")
print("[A] - Me!! ")
print("[B] - Bugha")
print("[C] - Your parents")
print("[D] - Fornite World cup didn't even happen")

response = input("\n My choice (A/B/C/D): ").upper()


if response == "B":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The answer was 'Bugha'")


# End of the quiz
display_results()