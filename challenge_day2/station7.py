# figure out variable value and calculate output from results
def solution_station_7(equation: str) -> float:
    # Define the variable values
    a = 3
    b = -1
    c = 4
    d = 7
    e = 0.5

    try:
        # Evaluate the equation with the given variables
        result = eval(equation)
        return result
    except Exception as ex:
        print(f"Error evaluating equation: {ex}")
        return None


