import random

objects = ["Rock", "Paper", "Scissors"]

computer_score = 0
player_score = 0
count = 0

round_ask = int(input("How many rounds would you like? "))


def win():
    global player_score
    global count
    if player_ans == "Rock" and computer_ans == "Scissors":
        print("Well done you won that round, computer chose: " + computer_ans)
        player_score += 1
        count += 1
    if player_ans == "Paper" and computer_ans == "Rock":
        print("Well done you won that round, computer chose: " + computer_ans)
        player_score += 1
        count += 1
    if player_ans == "Scissors" and computer_ans == "Paper":
        print("Well done you won that round, computer chose: " + computer_ans)
        player_score += 1
        count += 1


def lose():
    global computer_score
    global count
    if player_ans == "Rock" and computer_ans == "Paper":
        print("Unlucky, you lost that round, computer chose: " + computer_ans)
        computer_score += 1
        count += 1
    if player_ans == "Paper" and computer_ans == "Scissors":
        print("Unlucky, you lost that round, computer chose: " + computer_ans)
        computer_score += 1
        count += 1
    if player_ans == "Scissors" and computer_ans == "Rock":
        print("Unlucky, you lost that round, computer chose: " + computer_ans)
        computer_score += 1
        count += 1


def draw():
    global count
    if player_ans == computer_ans:
        print("Draw, next round")
        count += 1


while count < round_ask:
    player_ans = input("Rock, Paper or Scissors? ").capitalize()
    computer_ans = random.choice(objects)
    win()
    lose()
    draw()
    if count == round_ask:
        print("End of game, your score:", player_score, ", computers score:", computer_score)
    if player_ans not in objects:
        print("Make sure you typed that correctly!")
