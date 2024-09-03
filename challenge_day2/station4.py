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
        return False
    else:
        for n in range(2, number):
            if number % n == 0: 
                return False #if a divisor is found, the number is not prime 
                break
        else:
            return True #else if a divisor is not found, it's prime 
