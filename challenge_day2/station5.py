# input name output corresponding learning team
# scrap the data from last year's canvas
import csv

def solution_station_5(first_name, csv_file_path='names.csv'):
        with open(challenge_day2/names.csv, mode='r') as file:
            csv_reader = csv.DictReader(file)  
            
            for row in csv_reader:
                if row['First Name'] == first_name:
                    return row['Learning Team']
        
                else:
                        return "Student not found"
    
        except FileNotFoundError:
                return "CSV file not found"

# Example usage
print(solution_station_5('Shuting'))

