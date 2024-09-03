# input name output corresponding learning team
# scrap the data from last year's canvas
import csv

def solution_station_5(first_name, csv_file_path='names.csv'):
    try:
        with open(csv_file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            
            for row in csv_reader:
                if row['First Name'] == first_name:
                    return row['Learning Team']
            
            # Moved "Student not found" outside the loop
            return "Student not found"
    
    except FileNotFoundError:
        return "CSV file not found"

# Example usage
print(solution_station_5('Shuting'))
