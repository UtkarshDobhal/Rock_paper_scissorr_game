import random

print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "🪨 Rock vs 📄 Paper -> Paper wins \n"
      + "🪨 Rock vs ✂️ Scissors -> Rock wins \n"
      + "📄 Paper vs ✂️ Scissors -> Scissors wins \n")


user_score = 0
computer_score = 0

while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    choice = int(input("Enter your choice :"))

    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice please '))

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    print('User choice is \n', choice_name)
    print('🖥️ Now it\'s Computer\'s Turn....')

    comp_choice = random.randint(1, 3)

    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    print("🖥️ Computer choice is \n", comp_choice_name)
    print(choice_name, 'Vs', comp_choice_name)

    if choice == comp_choice:
        print('🖥️ It\'s a Draw', end="")
        result = "DRAW"
    else:
        if (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1):
            print('🖥️ Paper wins =>', end="")
            result = 'Paper'
            computer_score += 1
        elif (choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
            print('🖥️ Rock wins =>\n', end="")
            result = 'Rock'
            user_score += 1
        elif (choice == 2 and comp_choice == 3) or (choice == 3 and comp_choice == 2):
            print('🖥️ Scissors wins =>', end="")
            result = 'Scissors'
            computer_score += 1

    if result == 'DRAW':
        print("<== 🖥️ It's a tie ==>")
    elif result == choice_name:
        print("<== 🎉 User wins ==>")
    else:
        print("<== 🖥️ Computer wins ==>")

    print(f"Score: User - {user_score}, Computer - {computer_score}")

    if user_score == 5:
        print("<== 🎉 User wins the game! ==>")
        break
    elif computer_score == 5:
        print("<== 🖥️ Computer wins the game! ==>")
        break

    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break

print("🖥️ Thanks for playing!")
