# input name output corresponding learning team
# scrap the data from last year's canvas
import csv

def solution_station_5(first_name, csv_file_path='names.csv') -> int:
    # Define a mapping from learning team names to integers
    team_to_int = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
    }

    try:
        # Convert the input first_name to lowercase for case-insensitive comparison
        first_name_lower = first_name.strip().lower()

        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            
            for row in csv_reader:
                csv_first_name = row['First Name'].strip().lower()
                
                if csv_first_name == first_name_lower:
                    # Return the corresponding integer for the learning team
                    team_name = row['Learning Team']
                    return team_to_int.get(team_name, -1)  # Return -1 if the team name is not found
            
            return -1  # Return -1 if the student is not found
    
    except FileNotFoundError:
        return -2  # Return -2 if the CSV file is not found
    except UnicodeDecodeError:
        return -3  # Return -3 if there's an error decoding the CSV file
