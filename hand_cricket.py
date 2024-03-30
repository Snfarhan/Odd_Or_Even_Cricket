import random

def game_start(computer_choice):
    print("Start Match! (⁠≧⁠▽⁠≦⁠)")
    
    if computer_choice == "bat":
        comp_score = 0
        user_score = 0
        #Computer will bat first
        while True:
            comp_toss = random.randint(0,6)
            user_toss = int(input("Toss the ball: "))
            print("Computer batted:",comp_toss)
            if comp_toss == user_toss:
                comp_score += 1
                print("User has to score ",comp_score," to win")
                break
            elif user_toss >6 or user_toss <0:
                print("Oops out of range ,toss again (⁠｡⁠ŏ⁠﹏⁠ŏ⁠) ")
                continue
            else:
                comp_score += comp_toss
        #User will now bat        
        while user_score < comp_score:
            comp_toss = random.randint(0,6)
            user_toss = int(input("Bat: "))
            print("Computer tossed ball:",comp_toss)
            if comp_toss == user_toss:
                score_diff = comp_score - user_score
                print("Oh no looks like you lost the match by",score_diff,"runs (⁠｡⁠ŏ⁠﹏⁠ŏ⁠)")
                quit()
            elif user_toss >6 or user_toss <0:
                print("Oops out of range ,toss again (⁠｡⁠ŏ⁠﹏⁠ŏ⁠) ")
                continue
            else:
                user_score += user_toss
        if user_score == comp_score:
            print("Looks like you tied with the computer (⁠｡⁠ŏ⁠﹏⁠ŏ⁠)")
            quit()
        else:
            score_diff = user_score - comp_score
            print("Yay You won the match by",score_diff,"runs (⁠≧⁠▽⁠≦⁠)")
            quit()

    elif computer_choice == "ball":
        comp_score = 0
        user_score = 0
        #Computer will ball first
        while True:
            comp_toss = random.randint(0,6)
            user_toss = int(input("Bat: "))
            print("Computer tossed ball:",comp_toss)
            if comp_toss == user_toss:
                user_score += 1
                print("Computer has to score ",comp_score," to win")
                break
            elif user_toss >6 or user_toss <0:
                print("Oops out of range ,toss again (⁠｡⁠ŏ⁠﹏⁠ŏ⁠) ")
                continue
            else:
                user_score += user_toss
        #User will now ball        
        while comp_score < user_score:
            comp_toss = random.randint(0,6)
            user_toss = int(input("Toss the ball: "))
            print("Computer batted:",comp_toss)
            if comp_toss == user_toss:
                score_diff = user_score - comp_score
                print("Yay you won the match  by",score_diff,"runs (⁠≧⁠▽⁠≦⁠)")
                quit()
            elif user_toss >6 or user_toss <0:
                print("Oops out of range ,toss again (⁠｡⁠ŏ⁠﹏⁠ŏ⁠) ")
                continue
            else:
                user_score += user_toss
        if user_score == comp_score:
            print("Looks like you tied with the computer (⁠｡⁠ŏ⁠﹏⁠ŏ⁠)")
            quit()
        else:
            score_diff = comp_score - user_score
            print("Oh no looks like you lost the match by",score_diff,"runs (⁠⁠｡⁠ŏ⁠﹏⁠ŏ⁠)")
            quit()            
                                 



print("Lets play some hand cricket! (⁠≧⁠▽⁠≦⁠)")
odd_or_even = input("Lets choose who will be odd or even!(odd/even/quit): ").lower()

if odd_or_even != "odd" and odd_or_even != "even":
    print("Oops it seems youve entered wrong choice! (⁠｡⁠ŏ⁠﹏⁠ŏ⁠)")

elif odd_or_even == "quit":
    print("Thank you for playing hand cricket hope you had fun (⁠≧⁠▽⁠≦⁠)")
    quit()    

print("Lets choose who will bat or ball first!")
range_toss = random.randint(0,6)

try:
    user_toss = int(input("Toss a number to decide who will bat or ball first(0-6): "))
except ValueError:
    try:
        user_toss = int(input("Invalid input please enter a number(0-6): "))
    except ValueError:
        print("Oh no looks like you didnt toss a number, you lost (⁠｡⁠ŏ⁠﹏⁠ŏ⁠)")

if user_toss > 6 or user_toss < 0:
    print("Oh no looks like you tossed an invalid number, you lost (⁠｡⁠ŏ⁠﹏⁠ŏ⁠)")
    quit()

else: 
        print("Computer tossed: ",range_toss)
        total_toss = user_toss+range_toss    
        print("The total of the toss is:",total_toss)

        if (total_toss%2) == 0 and odd_or_even == "even":
            bat_or_ball = input("Choose wether you will bat or ball: ").lower()
            if bat_or_ball == "bat":
                print("You chose to bat!")
                computer_choice = "ball"
            elif bat_or_ball == "ball":
                print("You chose to ball")
                computer_choice = "bat"
            else:
                print("Invalid choice you lost (⁠｡⁠ŏ⁠﹏⁠ŏ⁠)")
                quit()        

        elif (total_toss%2) != 0 and odd_or_even == "odd":
            bat_or_ball = input("Choose wether you will bat or ball: ").lower()
            
            if bat_or_ball == "bat":
                print("You chose to bat!")
                computer_choice = "ball"
            elif bat_or_ball == "ball":
                print("You chose to ball")
                computer_choice = "bat"
            else:
                print("Invalid choice you lost (⁠｡⁠ŏ⁠﹏⁠ŏ⁠)")
                quit()  

        else:
            
            random_bat_ball = random.randint(0,1)
            if random_bat_ball == 0:
                computer_choice = "bat"
                print("Computer chooses to bat first!")
            elif random_bat_ball == 1:
                computer_choice = "ball"
                print("Computer chooses to ball first!")

        game_start(computer_choice)                    

