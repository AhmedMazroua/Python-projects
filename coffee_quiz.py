 """
    This is a simple quiz on coffee coded in python

    To run application simply type 'python3 coffee_quiz'
    
    """

def coffeeQuiz():
    #initialized variables for score, question number, and result
    score, questNum,= 0, 5

    #greeting
    print("welcome to my 'Coffee' quiz! ")

    #start prompt
    playing = input("Do you want to play?: ")

    if playing !=  "yes":
        quit()
    else:
        print("\nAwesome lets play!")

        #question I
        answer = input("\nLatte's are made with milk and shots of '_____' ?: ")
        #answer check
        if answer.casefold() == "espresso":
            score +=1
            print("correct!")
        else:
            print("Incorrect :(")

        #question II
        answer = input("\nThe method of brewing espresso originates from what country?: ")
        #answer check
        if answer.casefold() == "italy":
            score +=1
            print("correct!")
        else:
            print("Incorrect :(")

        #question III
        answer = input("\nCoffee House's in the 17th century were known as?: ")
        #answer check
        if answer.casefold() == "penny universities":
            score +=1
            print("correct!")
        else:
            print("Incorrect :(")

        #question IV
        answer = input("\nAre coffee beans really beans?: ")
        #answer check
        if answer.casefold() == "no":
            score +=1
            print("correct!")
        else:
            print("Incorrect :(") 

        #question V
        answer = input("\nTrue or False, coffee is the most popular beverage in the world?: ")
        #answer check
        if answer.casefold() == "False":
            score +=1
            print("correct!")
        else:
            print("Incorrect :(") 

    
    print(f"\nYou scored {score}/{questNum}!")


coffeeQuiz()
