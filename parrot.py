#a parrot function that will repeat what is typed
def parrot():
    message = "Type something and I'll repeat it: "

    active = True
    while active:
        prompt = input(message)
        
        if prompt == "quit":
            break
        else: 
            print(prompt)
parrot()