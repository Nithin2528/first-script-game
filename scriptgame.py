print("Welcome to my first game")

name = input("Enter your name?: ")

age = int(input('Enter your age: '))

health = 10

print("Hello" ,name ,"you are" , age , "years old.")

if age >=18:
    print("You are old enough to play!")
    
    want_to_play = input("Do you want to play! ").lower()
    if want_to_play == "yes":
        print("You are starting with", health , "health")
        print("Let's Play! ")

        left_or_right = input("First Choice..........Do you wanna go Left or Right(left/right)? ")
        if left_or_right == "left":
            ans = input("Nice your following the right path and reached the lake......Do you want to swim across or go around(across/around)? ")
            if ans == "across":
                print("You managed to cross the lake but got bitten by a crocodile and lost 5 health")
                health -= 5
            elif ans == "around":
                print("You went around and reached the other side of the lake....")

            ans = input("You see a house and a river. Do you to go to the river or the house...(house/river)")
            if ans == "house":
                    print("You went to the house and the owner greeted you......OOPs....you weren't liked by the owner and got killed by the owner..and YOU LOSE")
                    print("BETTER LUCK NEXT TIME")
            elif ans == "river":
                    print("You fell into the river and Lost.....")
            else:
                print("YOU LOST.....")
        else:
            print("You were killed and lost . You NOOB")    
    else:
        print("Cya.........")
else:
    print("You are not old enough to play.....!")
