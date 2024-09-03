#The sample outputs are the sines of the sample inputs. Therefore, the function calculates the sine of the inputs to give the desired output

import math

def solution_station_6(input_list):
    output_values = [round(math.sin(x), 4) for x in input_list]
    return output_values

inputs = [47, 28, 47, 58, 46, 15, 73, 72, 30, 22, 58, 38, 34, 35, 16, 46, 47, 28, 47, 91, 62, 72, 87, 78, 95, 49, 40, 24, 21]

outputs = solution_station_7(inputs)

