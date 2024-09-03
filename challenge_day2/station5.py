# input name output corresponding learning team
# scrap the data from last year's canvas
import csv

def solution_station_5(first_name, csv_file_path='names.csv'):
        with open(challenge_day2/names.csv, mode='r') as file:
            csv_reader = csv.DictReader(file)  
            
            for row in csv_reader:
                if row['first_name'] == first_name:
                    return row['learning_team_number']
        
        return "Student not found"
    
    except FileNotFoundError:
        return "CSV file not found"

# Example usage
team_number = get_learning_team_number('Shuting')
print(team_number)
