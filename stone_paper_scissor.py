
import random

print('Welcome to Stone-Paper-Scissor game')

print('\nWinning rules of the game STONE PAPER SCISSOR are :\n\n'
      + "Stone vs Paper -> Paper wins \n"
      + "Stone vs Scissor -> Stone wins \n"
      + "Paper vs Scissor -> Scissor wins \n")

print('You have 3 choices and 5 rounds')

while True:
    round=1
    dict1={'user_points':0,'computer_points':0}
    Invalid_choice_count=0

    print('\nYour choices are: \n1 - Stone\n2 - Paper\n3 - Scissor')

    while round<=5:
        print('\nRound',round,'-')
        user_choice=int(input('Enter your choice:'))

        while user_choice>=0 or user_choice<0:
            if user_choice==1:
                user_choice_name = 'Stone'
                break
            elif user_choice==2:
                user_choice_name = 'Paper'
                break
            elif user_choice==3:
                user_choice_name = 'Scissor'
                break
            else :
                user_choice=int(input('Enter a valid choice:'))
                if user_choice==1 or user_choice==2 or user_choice==3:
                    continue
                Invalid_choice_count+=1
                if Invalid_choice_count==1:
                    user_choice_name='Invalid choice'
                    break

        print('Your choice is',user_choice_name)

        if user_choice_name=='Invalid choice':
            break

        computer_choice=random.randint(1,3)

        if computer_choice==1:
            comp_choice_name = 'Stone'
        elif computer_choice==2:
            comp_choice_name = 'Paper'
        else:
            comp_choice_name = 'Scissor'

        print("Computer choice is ", comp_choice_name)

        if user_choice==computer_choice:
            print('\n-->Its a Draw')
            round+=1

        elif user_choice==1 and computer_choice==2:  # 1- stone    2- paper
            dict1['computer_points']+=10
            computer_points=dict1['computer_points']
            print(f'Paper wins')
            print(f"\n-->Computer player wins.Computer player gets {computer_points} points.")
            round+=1

        elif user_choice==1 and computer_choice==3:  # 1 -stone   3-scissor
            dict1['user_points']+=10
            user_points=dict1['user_points']
            print('Stone wins')
            print(f"\n-->You win. You get {user_points} points.")
            round+=1

        elif user_choice==2 and computer_choice==1:   # 2- paper    1 stone
            dict1['user_points']+=10
            user_points=dict1['user_points']
            print('Paper wins')
            print(f"\n-->You win. You get {user_points} points.")
            round+=1

        elif user_choice==2 and computer_choice==3:    # 2-paper   3 -scissor
            dict1['computer_points']+=10
            computer_points=dict1['computer_points']
            print('Scissor wins')
            print(f"\n-->Computer player wins. Computer player gets {computer_points} points.")
            round+=1

        elif user_choice==3 and computer_choice==1:    # 3 - scissor 1 -stone
            dict1['computer_points']+=10
            computer_points=dict1['computer_points']
            print('Stone wins')
            print(f"\n-->Computer player wins. Computer player gets {computer_points} points.")
            round+=1

        elif user_choice==3 and computer_choice==2:
            dict1['user_points'] += 10
            user_points=dict1['user_points']
            print('Scissor wins')
            print(f"\n-->You win. You get {user_points} points.")
            round+=1

    total_user_points=dict1['user_points']
    total_computer_points=dict1['computer_points']

    print(f"\n----------------------------")
    if user_choice_name=='Invalid choice':
        print('You have entered invalid choice 2 times. Better luck next time.')
    elif total_user_points>total_computer_points:
        print(f"\nCongratulations. You won the game with {total_user_points} points.")
    elif total_user_points==total_computer_points:
        print(f"\nGame tied. You and Computer player got {total_user_points} points each")
    else:
        print(f"\nSorry.You lost. Computer player won the game with {total_computer_points} points. Better luck next time.")


    a=input('\nDo you want to play again? y/n?')
    a.lower()
    if a=='n':
        print('\nThanks for playing')
        break
    elif a=='y':
        print('\nWelcome back to Stone Paper Scissor Game')
    else:
        print('\nError. Try again')
        break