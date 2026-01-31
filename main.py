#Roll The Dice

# loop
# take input form the user as Y/N
# print the input
# if user enters Y 
#    generate random number between 1 to 6

# elif user enters N 
#    print Thank You for coming 

# else
#    invalid choice 


import random

while True:
 choice = input("Roll the dice? (y/n): ").lower()
 print(choice)

 if choice == 'y':
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print(die1, die2)

 elif choice == 'n':
    print("ThankYou for coming")   
    break 

 else:
    print("Invalid choice")    
