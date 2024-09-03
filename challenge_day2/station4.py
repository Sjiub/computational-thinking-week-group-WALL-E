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

"""
def solution_station_4(number):
    if number <= 1:
        print('F')
    else:
        for n in range(2, number):
            if number % n == 0:
                print('F')
                break
        else:
            print('T')
