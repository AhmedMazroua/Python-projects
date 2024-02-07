import random

def magic8Ball():
    responses = ["I think you know the answer", "Maybe", "The truth is in the present", "its possible", "possibly not"]
    choice = random.randint(0,4)

    start = input("welcome to magic 8 ball, type yes to play: ")
    if start.lower() != "yes":
        print("All good take care!")
        quit()

    while True:
        ask = input("press q to quit at any time, what is your question?...: ")      
        if ask.lower() != "q":
            print(responses[choice])

        else:

            print("Take care, comeback soon!")
            break

magic8Ball()