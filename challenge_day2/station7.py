# figure out variable value and calculate output from results
def solution_station_7(equations: list[str]) -> list[float]:
    a = 3
    b = -1
    c = 4
    d = 7
    e = 0.5
    
    results = []
    
    # Loop through each provided equation
    for i, equation in enumerate(equations, start=1):
        try:
            # Evaluate the equation with the given variables
            result = eval(equation)
            results.append(result)
        except Exception as ex:
            print(f"Error evaluating equation {i}: {ex}")
            results.append(None)  # Append None in case of an error
    
    return results


