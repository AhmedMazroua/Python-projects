def main(temp=int, scale=""):
    if (temp == int and scale == "F"):
        # Convert Fahrenheit to Celsius
        temp =  (temp - 32) * 5.0 / 9.0 
        print("Thats " + str(temp) + " degrees Celsius!")
    elif (temp == int and scale == "C"):
        temp = (temp * 9.0 / 5.0) + 32
        # Convert Celsius to Fahrenheit
        print("Thats " + str(temp)+ " degrees Fahrenheit!")
    # Handles any string other than C or F
    else:
        print('Please enter a valid Scale "F" or "C" and or integer inputs')
#function is called 
main(temp="Integer temp here", scale='"F" or "C" here')
