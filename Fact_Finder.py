# Referances: stackoverflow, geeksforgeeks,

# Import pandas
import pandas as pd # Referance: Geeksforgeeks

# Initialize CSV file as a dataframe
df = pd.read_csv("CIA Fact Finder.csv") # Referance: Geeksforgeeks

def country():
    # Make it into a global variable for easiness
    global chosen_country
    global country_list
    global country_number
    # Turn the "Country" column of the csv file into a list
    country_list = df["Country"].tolist() # Referance: Stackoverflow and Geeksforgeeks
    # Change the formating by making only the first letter uppercase and removing all spaces
    country_list = list(map(str.capitalize, country_list)) # Referance: Stackoverflow
    new_country_list = []
    for element in country_list:
        new_country_list.append(element.replace(" ", ""))
    # Ask the user for the country and change the user's input to prevent errors later
    chosen_country = input("Country? ").capitalize()
    chosen_country = chosen_country.replace(" ", "")
    # Check to see if the user's chosen country is a country in the list
    while chosen_country not in new_country_list:
        chosen_country = input("Country? ").capitalize()
        chosen_country = chosen_country.replace(" ", "")
    # Find the index the country is in
    found = False
    while found == False:
        for i in range(0, 30):
            if new_country_list[i] == chosen_country:
                country_number = i
                found = True




def metric():
    # Ask the user for the metric they would like
    chosen_metric = input(('''
Metric? 
1. Population
2. Birth Rate
3. GDP Per Capita
4. Unemployment Rate
    '''))
    # Change the numbers into
    if chosen_metric == "1":
        chosen_metric = "Population"
    elif chosen_metric == "2":
        chosen_metric = "Birth Rate"
    elif chosen_metric == "3":
        chosen_metric = "GDP Per Capita"
    elif chosen_metric == "4":
        chosen_metric = "Unemployment Rate"
    metric_list = df[chosen_metric].tolist()
    print("The", chosen_metric, "of", chosen_country, "is", metric_list[country_number])

#def instructions():

country()
metric()
