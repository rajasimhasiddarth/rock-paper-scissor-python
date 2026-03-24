import random

x = ["rock", "paper", "scissor"]

user_score = 0
computer_score = 0
while True:
    k = input("Ready rock, paper, scissors! (or exit): ").lower()
    if k == "exit":
        break
    if k not in x:
        print("Try again")
        continue
    y = random.choice(x)
    print(f"Computer: {y}  You: {k}")
    if k == y:
        print("Equal")
    elif (k == "rock" and y == "scissor") or \
         (k == "paper" and y == "rock") or \
         (k == "scissor" and y == "paper"):
        print("You win")
        user_score += 1
    else:
        print("Computer wins")
        computer_score += 1
      
    print(f"Score: user-{user_score} computer-{computer_score}")
  
print(f"Final Score: user-{user_score} computer-{computer_score}")
