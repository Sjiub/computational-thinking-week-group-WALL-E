# Boolean prime number stuff
""" 
input          output
87             F
37             T
98             F
26             F
78             F
0              F
7              T
"""

#Check whether the number is a prime number or not
def solution_station_4(number):
    if number <= 1: 
        print('F') #return False for numbers that are 1 or 0 because they aren't prime numbers
    else:
        for n in range(2, number):
            if number % n == 0: 
                print('F') #if a divisor is found, the number is not prime 
                break
        else:
            print('T') #else if a divisor is not found, it's prime 
