def solution_station_7():
    # Define the variable values
    a = 3
    b = -1
    c = 4
    d = 7
    e = 0.5
    
    # Ask the user for three equations
    for i in range(1, 4):
        equation = input(f"Enter equation {i}: ")
        try:
            # Evaluate the equation with the given variables
            result = eval(equation)
            print(f"Result of equation {i}: {result}")
        except Exception as ex:
            print(f"Error evaluating equation {i}: {ex}")

# Call the function to evaluate equations
solution_station_7()

