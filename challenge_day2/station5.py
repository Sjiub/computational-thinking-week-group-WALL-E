# input name output corresponding learning team
# scrap the data from last year's canvas
import csv

def solution_station_5(first_name, csv_file_path='names.csv'):
    try:
        # Convert the input first_name to lowercase for case-insensitive comparison
        first_name_lower = first_name.strip().lower()

        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            
            for row in csv_reader:
                # Convert the CSV field to lowercase for case-insensitive comparison
                csv_first_name = row['First Name'].strip().lower()
                
                if csv_first_name == first_name_lower:
                    return row['Learning Team']
            
            return "Student not found"
    
    except FileNotFoundError:
        return "CSV file not found"
    except UnicodeDecodeError:
        return "Error decoding the CSV file"

# Example usage
print(solution_station_5('shuting'))  # Should work regardless of capitalization
print(solution_station_5('Shuting'))
print(solution_station_5('SHUTING'))
