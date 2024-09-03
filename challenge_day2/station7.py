def solution_station_7():
    # define the variable values
    a = 3
    b = -1
    c = 4
    d = 7
    e = 0.5
    
    # ask the user for three equations
    for i in range(1, 4):
        equation = input(f"Enter equation {i}: ")
        try:
            # evaluate the equation with the given variables
            result = eval(equation)
            print(f"Result of equation {i}: {result}")
        except Exception as ex:
            print(f"Error evaluating equation {i}: {ex}")

# call the function to solve the equation
solution_station_7()

