import numpy as np
import pandas as pd
import json
# create menu function to select the file type

def menu():
    print("Press 1 for CSV File")
    print("Press 2 for JSON File")
    print("Press 3 for TXT File")
    print("Press 4 for Excel File")
    return int(input("Enter the number of File that you want to load: "))

# Function to load files based on user's selection
def loadFiles():
    file = menu()
    path = input(f"Enter the path of the file you want to upload: ")

    if file == 1:
        df = pd.read_csv(path)

    elif file == 2:
        with open(path, 'r') as jsonFile:
            data = json.load(jsonFile)
            df = pd.DataFrame(data)  # Converting JSON data to DataFrame if applicable

    elif file == 3:
        with open(path, 'r') as txtFile:
            data = txtFile.readlines()  # Reading all lines from the txt file
            df = pd.DataFrame(data, columns=["Text"])  # Putting text into a DataFrame

    elif file == 4:
        df = pd.read_excel(path)

    else:
        return "Invalid input"
    
    return df

# Load and display the data
data = loadFiles()
print(data)



            
               
