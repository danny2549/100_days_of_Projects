secret_number = 89
guess_counter = 0
guess_limit = 3
guess = ""
game_over = False

while guess != secret_number and not(game_over):
    if guess_counter < guess_limit:
        guess = int(input("Please enter a number "))
        guess_counter += 1
    else: 
        game_over = True

    if guess < secret_number:
        print("guess too low")
    elif guess > secret_number:
        print("guess too high")
    else:
        print("Please enter only a number")

if game_over: 
    print("Loser!")
else:
    print("Winner!")
