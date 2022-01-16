#intro
print('''
**********************************
**********************************
**\t  ICT Group Project\t**
**\tAtif\t\t(016)\t**
**\tAli Abbas\t(039)\t**
**\tAbubakr Saddeeq\t(046)\t**
**********************************
**********************************
''')



import time

# users and passwords
users = {'haris7': '1122',
         'ayesha48': '1234',
         'Ahmad69': '7218',
         'faizan_': '4690',
         'umar._': '1111'}

names = {'haris7': "Haris",
         'ayesha48': "Ayesha",
         'Ahmad69': 'Ahmad',
         'faizan_': 'Faizan',
         "umar._": 'Umar'}
global name

print("\t\t**Welcome to Arcades**")
print()


def play_again():
    print("1. Back to main menu \n2. Exit")
    while True:
        choose = input("Enter your choice: ")
        if choose == '1':
            print()
            print("---")
            print()
            game_run()
        elif choose == '2':
            print("Thank you for playing. Have a good day.")
            exit()
        else:
            print("Please enter '1' or '2'")


def scoreboard(player1_win, player2_win, won):
    def check():
        if won == '1':
            return 1
        if won == '2':
            return 2
        else:
            return 0

    check()
    if check() == 1:
        player1_win += 0
    elif check() == 2:
        player2_win += 0
    if check() == 1 or check() == 2:
        print(name + "\t" + "|" + "\t" + 'Computer')
        print("\t\t" + "|" + "\t\t")
        print(" " + str(player1_win) + "\t\t" + "|" + "\t\t" + str(player2_win))


def hangman(name):
    import random

    random_words = ['laptop', 'pen', "write", "that", "program", "man", "chocolate", "ice", "water"]
    word = random.choice(random_words)
    list_of_secret_word = list(word)
    to_be_guessed = []
    already_guessed_alphabets = []
    chances = 0
    total_chances = 6
    print("Hello", name, "let's play a word guessing game, hangman!")
    time.sleep(0.5)
    print("Start guessing: ")
    for i in list_of_secret_word:
        i = '_'
        to_be_guessed.append(i)
    while chances < total_chances:
        for anonymous in to_be_guessed:
            print(anonymous, end='')
        print()
        guess = input("Enter guessed character: ")
        if guess.lower() in list_of_secret_word:
            if guess.lower() in already_guessed_alphabets:
                print(guess, 'has already been used!')
                continue
            for alphabet_index in range(0, len(list_of_secret_word)):
                if guess.lower() == list_of_secret_word[alphabet_index]:
                    to_be_guessed[alphabet_index] = guess.lower()
                    already_guessed_alphabets.append(guess)
            if to_be_guessed == list_of_secret_word:
                print(word)
                print(f'You guessed correctly! The word was"{word}"')
                break
        else:
            print("Wrong guess")
            chances += 1
            if chances == 5:
                print("1 chance remaining")
            elif chances == 6:
                print("NO CHANCES REMAINING")
            else:
                print(total_chances - chances, "chances remaining")
            if chances == 1:
                print('''+---+
|   |
O   |
    |
    |
    |
=========''')
            elif chances == 2:
                print('''+---+
|   |
O   |
|   |
    |
    |
=========''')
            elif chances == 3:
                print('''+---+
 |   |
 O   |
/|   |
     |
     |
=========''')
            elif chances == 4:
                print('''+---+
 |   |
 O   |
/|\  |
     |
     |
=========''')
            elif chances == 5:
                print('''+---+
 |   |
 O   |
/|\  |
/    |
     |
=========''')

            else:
                print('''+---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''')
                print(f'Secret word was "{word}"')
    print("Do you want to play Hangman again?")
    while True:
        choose = input("Yes/No:")
        print()
        if choose.lower() == 'yes':
            hangman(name)
        elif choose.lower() == 'no':
            play_again()
        else:
            print("Please type 'yes' or 'no'")
            time.sleep(1)


def tictactoe(name):
    import random

    print("* Tic Tac Toe *\n")
    time.sleep(0.5)
    print("......Lets start......\n")
    time.sleep(0.5)
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")

    player_choice = input("1. Multiplayer \n2. Computer \nEnter '1' or '2': ")

    if player_choice == '1':
        player_2 = input("Enter player 2 name: ")
    else:
        player_2 = "Computer"

    def game(player1_win, player2_win):
        board = {
            '1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '
        }

        def check():
            # checking for player 1

            if board['1'] == 'X' and board['2'] == 'X' and board['3'] == 'X':
                return 1

            if board['4'] == 'X' and board['5'] == 'X' and board['6'] == 'X':
                return 1

            if board['7'] == 'X' and board['8'] == 'X' and board['9'] == 'X':
                return 1

            if board['1'] == 'X' and board['5'] == 'X' and board['9'] == 'X':
                return 1

            if board['3'] == 'X' and board['5'] == 'X' and board['7'] == 'X':
                return 1

            if board['1'] == 'X' and board['4'] == 'X' and board['7'] == 'X':
                return 1

            if board['2'] == 'X' and board['5'] == 'X' and board['8'] == 'X':
                return 1

            if board['3'] == 'X' and board['6'] == 'X' and board['9'] == 'X':
                return 1

            # checking for player 2

            if board['1'] == 'O' and board['2'] == 'O' and board['3'] == 'O':
                return 2

            if board['4'] == 'O' and board['5'] == 'O' and board['6'] == 'O':
                return 2

            if board['7'] == 'O' and board['8'] == 'O' and board['9'] == 'O':
                return 2

            if board['1'] == 'O' and board['5'] == 'O' and board['9'] == 'O':
                return 2

            if board['3'] == 'O' and board['5'] == 'O' and board['7'] == '0':
                return 2

            if board['1'] == 'O' and board['4'] == 'O' and board['7'] == 'O':
                return 2

            if board['2'] == 'O' and board['5'] == 'O' and board['8'] == 'O':
                return 2

            if board['3'] == 'O' and board['6'] == 'O' and board['9'] == 'O':
                return 2

        print('1|2|3')
        print('- +- +-')
        print('4|5|6')
        print('- +- +-')
        print('7|8|9')
        print('*')
        moves = 0
        n = 1
        while True:
            print(board['1'] + '|' + board['2'] + '|' + board['3'])
            print('-+-+-')
            print(board['4'] + '|' + board['5'] + '|' + board['6'])
            print('-+-+-')
            print(board['7'] + '|' + board['8'] + '|' + board['9'])
            print('''
===============================
===============================
                    ''')
            check()
            if check() == 1:
                print(name, ' Won!!')
                player1_win += 1
            elif check() == 2:
                print(player_2, ' Won!!')
                player2_win += 1
            if check() == 1 or check() == 2:
                print(name + "\t" + "|" + "\t" + player_2)
                print("\t\t" + "|" + "\t\t")
                print(" " + str(player1_win) + "\t\t" + "|" + "\t\t" + str(player2_win))

                print()
                choice = input("Do you want to play tic-tac-toe again?(Yes or No): ")
                if choice.lower() == "yes":
                    break
                else:
                    play_again()
            if moves == 9:
                print("its a tie")
                choice = input("Do you want to play tic-tac-toe again?(Yes / No): ")
                print()
                if choice.lower() == "yes":
                    break
                else:
                    play_again()

            while True:
                if n == 1:
                    p1 = input(f"{name}'s turn \n choose a slot from 1 to 9:")
                    if p1 in board and board[p1] == ' ':
                        board[p1] = 'X'
                        n = 2  # player2 turn
                        break
                    else:
                        print('Invalid input, please try again')
                        continue
                else:
                    if player_choice == '1':
                        p2 = input(f"{player_2}'s turn \n choose a slot from 1 to 9:")
                    else:
                        p2 = random.randint(1, 10)
                        p2 = str(p2)
                    if p2 in board and board[p2] == ' ':
                        board[p2] = 'O'
                        n = 1  # player1 turn
                        break
                    else:
                        if player_choice == '1':
                            print('Invalid input, please try again')
                            time.sleep(1)
                            continue
                        else:
                            continue
            moves += 1
        if player1_win == 0 and player2_win == 0:
            pass
        else:
            game(player1_win, player2_win)

    game(0, 0)


def rockpaperscissors():
    import random
    player1_win = 0
    player2_win = 0
    print("The one to win 3 times first will win the series.")
    while True:
        random_number = random.randint(1, 3)
        random_number = str(random_number)
        print()
        try:
            user = int(input("Enter a number from 1,2,3 for scissors,rock and paper respectively: "))
        except ValueError:
            print("Please enter a number between '1','2' or '3'")
            time.sleep(1)
            print()
            continue
        if user <= 3:
            time.sleep(0.5)
            if random_number == '1':
                print("Computer chose scissors")
            if random_number == '2':
                print("Computer chose rock")
            if random_number == '3':
                print("Computer chose paper")
        time.sleep(1)
        if user == 1 and random_number == '1':
            print(f"{name} chose scissors")
            print("It's a draw")
            won = ''
        elif user == 1 and random_number == '2':
            print(f"{name} chose scissors")
            print("Computer wins! ")
            player2_win += 1
            won = '2'
        elif user == 1 and random_number == '3':
            print(f"{name} chose scissors")
            print(f"{name} wins!")
            player1_win += 1
            won = '1'
        elif user == 2 and random_number == '1':
            print(f"{name} chose rock")
            print(f"{name} wins!")
            player1_win += 1
            won = '1'
        elif user == 2 and random_number == '2':
            print(f"{name} chose rock")
            print("It's a tie")
            won = ''
        elif user == 2 and random_number == '3':
            print(f"{name} chose rock")
            print("Computer wins!")
            player2_win += 1
            won = '2'
        elif user == 3 and random_number == '1':
            print(f"{name} chose paper")
            print("Computer wins!")
            player2_win += 1
            won = '1'
        elif user == 3 and random_number == '2':
            print(f"{name} chose paper")
            print(f"{name} won!")
            player1_win += 1
            won = '1'
        elif user == 3 and random_number == '3':
            print(f"{name} chose paper")
            print("It's a tie!")
            won = ''
        else:
            print("Please enter a number from 1,2,3")
            time.sleep(1)
            print()
        del random_number
        scoreboard(player1_win, player2_win, won)
        if player1_win <= 2 and player2_win <= 2:
            time.sleep(1)
            continue
        else:
            if player1_win > player2_win:
                print(f'{name} won the series!')
            else:
                print()
                print('Computer won the series!')
                time.sleep(1)
            print("Do you want to play Rock Paper Scissors again?")
            while True:
                choose = input("Yes/No:")
                print()
                if choose.lower() == 'yes':
                    rockpaperscissors()
                elif choose.lower() == 'no':
                    play_again()
                else:
                    print("Please enter 'Yes' or 'No'")


def game_run():
    while True:
        print('''1. Hangman
2. Tic-Tac-Toe
3. Rock Paper Scissors
4. Exit''')
        choice = input("Which game do you wanna play?: ")
        choice = choice.lower()
        if choice == "1" or choice == "hangman":
            hangman(name)
        elif choice == '2' or choice == "tic-tac-toe" or choice == 'tic tac toe':
            tictactoe(name)
        elif choice == '3' or choice == 'rock paper scissors':
            rockpaperscissors()
        elif choice == '4':
            print("Have a good day, Bye!")
            exit()
        else:
            print("Please enter number of the game or its name")
            time.sleep(1)
            print()


def signup():
    print("Please Enter following credentials: ")
    while True:
        global name
        name = input("Name: ")
        name = name.title()
        if name == '' or name == ' ':
            print("Name can't be empty, enter the name again.")
            continue
        elif name.isnumeric():
            print("Name can't be a numeric value")
            continue
        else:
            break
    while True:
        mobile_number = input("Mobile No: ")
        if len(mobile_number) == 11:
            pass
        elif len(mobile_number) > 11 or len(mobile_number) < 11:
            print("Please enter 11 digit mobile number.")
            continue
        if mobile_number[0] == "0" and mobile_number[1] == "3":
            break
        else:
            print("Please enter a phone number starting from 03")
    while True:
        username = input("Select a username: ")
        print("Please wait while we check the validity of your username", end='')
        for k in range(4):
            print(".", end='')
            time.sleep(0.4)
        for i in users:
            if username == i:
                print()
                print(f'The username "{username}" is not available. Please try another one.')
                break
        if username == i:
            continue
        else:
            break
    print()
    password = input("Type a password: ")
    print("Dear user! You have successfully signed up.")
    users[username] = password
    names[username] = name
    print()
    print("---")
    print()
    login_menu()


def login():
    a = 0
    while True:
        user_name = input("Enter your username: ")
        for i in users:
            if user_name == i:
                a += 1
                break
        global name
        name = names[i]

        if a == 0:
            print('New user? Press enter to signup instantly! or Enter "No" to re-type your username')
            new = input("")
            if new == '' or new == ' ':
                signup()
            elif new.lower() == 'no':
                print(f'Please enter a username that is already registered.')
                continue

            continue
        else:
            print(f'Hello {name.title()}! Please enter your password.')
            while True:
                p = 0
                pass_word = input(f"Password: ")
                for j in users:
                    if pass_word == users[user_name]:
                        p += 1
                        break
                if p == 1:
                    break
                else:
                    print("Wrong password, Please enter the password again.")
        if p == 1:
            break


def login_menu():

    while True:
        print("1. Login \n2. Signup")
        user_choice = input("Enter your choice: ")
        if user_choice == "1" or user_choice.lower() == 'login':
            login()
        elif user_choice == "2" or user_choice.lower() == "signup":
            signup()
        else:
            print("Invalid choice, please enter the choice again..")
            continue
        break

    print("Please wait while we log you in", end='')
    for k in range(4):
        print('.', end='')
        time.sleep(0.4)
    print()
    print("---")
    print()

    print(f'Hello {name}! Welcome to Vortex  Gaming Zone!')

    game_run()


login_menu()
