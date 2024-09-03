# number and boolean
"""
sample input          input           sample output              output
10                    93151           F                          ?
87                    80904           T                          ?
85                    66255           F                          ?
22                    69506           F                          ?
81                    94030           T                          ?
46                    48262           F                          ?
30                    59010           T                          ?
"""

def solution_station_3(input_number: int) -> bool:
  if input_number % 3 == 0:
    return True
  else:
    return False
  
