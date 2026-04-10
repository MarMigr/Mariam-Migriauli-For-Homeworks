import json

def salary_file_generation():
    input_file = input("Please enter file name: ")
    
    try:
        with open(input_file, 'r') as file:
            data = json.load(file)
        print("File loaded successfully!")
    except FileNotFoundError:
        print(f"The file name you entered '{input_file}' couldn't be found.")
        return  
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return  
    avg_salaries = {}

    for department in data:
        try:
            name = department['name'] 
            salaries = department['salaries'] 
            avg_salaries[name] = sum(salaries) / len(salaries)

        except KeyError as e:
            print(f"Error: Missing key {e} in department data: {department}")
        except TypeError:
            print(f"Invalid type for salary data in department '{department}'.")
        except ZeroDivisionError:
            print(f"Error: No salaries provided for department '{department}'.")
        except Exception as e:
            print(f"Unexpected error processing department '{department}': {e}")

    print("\nAverage Salaries by Department:")
    for name, avg_salary in avg_salaries.items():
        print(f"{name}: {avg_salary}")

    output_file = 'average_salary.json'
    with open(output_file, 'w') as file:
        json.dump(avg_salaries, file, indent=4)
    print(f"\nAverage salaries saved to '{output_file}'.")

if __name__ == '__main__':
    salary_file_generation()
