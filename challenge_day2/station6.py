#The sample outputs are the sines of the sample inputs. Therefore, the function calculates the sine of the inputs to give the desired output

import math

def solution_station_6(input_list):
    output_values = [round(math.sin(x), 4) for x in input_list]
    return output_values

