import json

def print_json_values(file_path):
    try:
        # Open and read the JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Recursive function to print values
        def print_values(data):
            if isinstance(data, dict):
                for key, value in data.items():
                    print(f"{key}: ", end='')
                    print_values(value)
            elif isinstance(data, list):
                for item in data:
                    print_values(item)
            else:
                print(data)

        print_values(data)
    
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON data.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the path to your JSON file
file_path = 'interpreting.json'
print_json_values(file_path)

