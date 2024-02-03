'''
finds first number greater than x
'''

def num(x, rray):
    array = sorted(rray)
    for i in range(len(array)):
        if x < array[i]:
            print(f"{array[i]} is the largest number after {x} and its index is {i}")  
            break
            
num()