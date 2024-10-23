#* ***********************************************************************
# Bhabis Lamichhane
# Assignment 2 - Fact Finder
# CS30 IB
# Oct 22, 2024

#This program is my own work - Digital Signature (BL) */
# References: Stackoverflow, Geeksforgeeks, Alexander Li

# Import pandas
import pandas as pd # Reference: Geeksforgeeks

# Main function to run the game
def main():
    # Turn df into a global variable for easy access
    global df
    # Initialize CSV file as a dataframe
    df = pd.read_csv("CIA Fact Finder.csv")  # Reference: Geeksforgeeks
    # Remove the indexes in the dataframe Reference: Geeksforgeeks
    blankIndex = [''] * len(df)
    df.index = blankIndex
    new_country_list = list_of_countries()
    # Instructions and background
    print('''
                       *****CIA Fact Finder*****
Find information about the 30 most powerful countries in the world!

                             Instructions:
1. Choose whether you want to find a specific fact about a country or sort all the countries based on a specific metric (extension)
2. If you chose to find a fact about a specific country:
    2a. Choose a country among the top 30 most powerful countries (list provided)
    2b. Choose what fact you would like to find (list provided)
    2c. The program will then tell you about the fact about your chosen country!
3. If you chose to sort the countries based on a metric (extension):
    3a. Choose what metric to sort the countries on (list provided)
    3b. Choose whether the list should be ascending or descending
    3c. The program will make you list of the countries based on your chosen metric!
4. Choose whether or not you want to play again''')
    # Forces the user into a loop
    choice = "YES"
    while choice == "YES":
        # Asks the user for the game "mode"
        choice = input("\nSee a metric on a specific country(a) or sort the countries based on one metric(b)? ").lower()
        # Error handling
        while choice != "a" and choice != "b":
            print("Invalid input! Please enter a or b")
            choice = input("\nSee a metric on a specific country(a) or sort the countries based on one metric(b)? ").lower()
        if choice == "a":
            chosen_country = ask_country(new_country_list)
            country_number = find(chosen_country, new_country_list)
            fact(country_number, chosen_country)
        elif choice == "b":
            sort()
        # Choice to play again
        choice = input("\nWould you like to play again? ").upper()
        # Error handling
        while choice != "YES" and choice != "NO":
            print("Invalid input! Please enter yes or no")
            choice = input("\nWould you like to play again? ").upper()
        if choice == "NO":
            print("Hope you found this useful!")

# Creates a list of the countries
def list_of_countries():
    # Turn the "Country" column of the csv file into a list
    country_list = df["Country"].tolist() # Reference: Stackoverflow and Geeksforgeeks
    # Change the formating by making only the first letter uppercase
    country_list = list(map(str.capitalize, country_list)) # Reference: Stackoverflow
    # Removes all the spaces (for error handling)
    new_country_list = []
    for element in country_list:
        new_country_list.append(element.replace(" ", ""))
    return new_country_list

# Asks the user for a country
def ask_country(new_country_list):
    # Print all the countries the user can choose
    print("\nA list of the top 30 countries (countries you can choose):")
    print(df[["Country"]])
    # Ask the user for the country and change the user's input to prevent errors later
    chosen_country = input("\nWhich country would you like to see information about? ").capitalize()
    chosen_country = chosen_country.replace(" ", "")
    # Check to see if the user's chosen country is a country in the list
    while chosen_country not in new_country_list:
        chosen_country = input("\nWhich country would you like to see information about? ").capitalize()
        chosen_country = chosen_country.replace(" ", "")
    return chosen_country


# Finds the index of the user's country
def find(chosen_country, new_country_list):
    found = False
    # Runs while the country is not yet found
    while found == False:
        for i in range(0, 30):
            # Linear search to find the country
            if new_country_list[i] == chosen_country:
                country_number = i
                found = True
    return country_number

# Prints out the fact of the country
def fact(country_number, chosen_country):
    # Obtains the chosen metric from the user
    fact = metric()
    # Creates a list of the fact (eg. A list of the Birth Rates of all countries if the metric is Birth Rate)
    metric_list = df[fact].tolist()
    print("\nThe", fact, "of", chosen_country, "is:", metric_list[country_number])

# Asks the user for a metric
def metric():
    # Ask the user for the metric they would like
    chosen_metric = input(('''
\nWhich metric do you choose? 
1. Population
2. Birth Rate
3. GDP Per Capita
4. Unemployment Rate
(please just input the number) '''))
    # Error handling
    while chosen_metric not in ["1", "2", "3", "4"]:
        print("Invalid input! Please enter 1, 2, 3, or 4")
        chosen_metric = input(('''
        \nWhich metric do you choose? 
        1. Population
        2. Birth Rate
        3. GDP Per Capita
        4. Unemployment Rate
        (please just input the number)
                '''))
    # Change the numbers into the appropriate metric
    if chosen_metric == "1":
        chosen_metric = "Population"
    elif chosen_metric == "2":
        chosen_metric = "Birth Rate"
    elif chosen_metric == "3":
        chosen_metric = "GDP Per Capita"
    elif chosen_metric == "4":
        chosen_metric = "Unemployment Rate"
    return chosen_metric

# Sorts the countries
def sort():
    # Obtains the metric to sort the countries by
    sorting_metric = metric()
    sorting_format = input("\nDo you want an ascending list (a) or a decending list(d)? ").lower()
    # Error handling
    while sorting_format != "a" and sorting_format != "b":
        print("Invalid input! Please enter a or d")
        sorting_format = input("\nDo you want an ascending list (a) or a decending list(d)? ").lower()
    # Sorts the dataframe
    if sorting_format == "a":
        sorted_df = df.sort_values(by=[sorting_metric], ascending=True) #Reference: Geeksforgeeks
    elif sorting_format == "d":
        sorted_df = df.sort_values(by=[sorting_metric], ascending=False)
    print("\nList of Countries sorted", sorting_format, "based on", sorting_metric, ":")
    print(sorted_df[["Country", sorting_metric]])

# Calls the main function to run the game
main()
