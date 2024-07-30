import random, sys

# P - Paper
# R - Rock
# S - Scissors

def generate_random_number():
    random_number = random.randint(0,2)
    return random_number

def check_move(random_number):
    if random_number == 0:
        return "P"
    elif random_number == 1:
        return "R"
    else:
       return "S"

pc_cont = 0
player_cont = 0    

#print(move) just to see the movement of the pc
print("""Let's play one famous game Jankenpo, read in README the rules of this mini game
          to exit type 'exit'""")
print('''type:
          P - Paper
          R - Rock
          S - Scissors''')

for i in range(3):
    random_number = generate_random_number()
    move = check_move(random_number)
    #print(move)
    choice = input().upper()

    if choice not in ["R","P","S"]:
        print('Type a valid value pls')
        continue
    
    if choice == "P" and move == "P":
        print("It's a tie")
    elif choice == "P" and move == "R":
        print("You win, Paper wraps rock")
        player_cont += 1
    elif choice == "P" and move == "S":
        print("You loose, Scissors cut paper")
        pc_cont +=1
    elif choice == "R" and move == "P":
        print("You loose, Paper wraps rock")
        pc_cont +=1
    elif choice == "R" and move == "R":
        print("It's a tie")
    elif choice == "R" and move == "S":
        print("You win, rock breack scissor")
    elif choice == "S" and move == "P":
        print("You win, scissor cut paper")
    elif choice == "S" and move == "S":
        print("it's a tie")
    else:
        print("You loose, rock break scissors")

if player_cont > pc_cont:
    print("You won this mini-game, your prize is to get a free pizza rodizio")
elif player_cont == pc_cont:
    print("It's a tie, try again to receive your prize")
else:
    print("You loose, try in the next time")