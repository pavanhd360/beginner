import random
emojis = {'r':'🪨','p':'📃','s':'✂️'}
choices = ['r','p','s']
def get_user_choice():
    while True:
         user_choice=input("rock,paper,scissors?(r/p/s):").lower()
         print(f"DEBUG: You typed:'{user_choice}")
         if user_choice in ['rock', r]:
            return 'r'
         elif user_choice in ['paper', p]:
            return 'p'
         elif user_choice in ['scissors',s]:
            return 's'
         else:
              print('Invalid choices')
def display_choices(user_choice, computer_choice):
    print(f'you chose   {emojis[user_choice]}')
    print(f'computer chose  {emojis[computer_choice]}')
def determine_winner(user_choice, computer_choice):
      print(f"DEBUG: Comparing user = '{user_choice}' vs computer_choice='{computer_choice}'")
      if user_choice == computer_choice:
        print('Tie')
      elif (user_choice == 'r' and computer_choice == 's') or(user_choice == 's' and computer_choice == 'p') or(user_choice == 'p' and computer_choice == 'r'):
        print('you win')
      else :
        print('YOU lose') 
def play_games():
    while True:   
        user_choice = get_user_choice()     
        computer_choice =random.choice(choices)
        display_choices(user_choice, computer_choice)
        determine_winner(user_choice, computer_choice)
    
        shd_continue= input('continue? (y/n)').lower()
        if shd_continue == 'n' :
            break
play_games()
        