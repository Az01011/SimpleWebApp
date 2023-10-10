#This application should display a list of countries, including a text input
#field for searching. You should be able to provide a string in this input
#field, run a search on the list of countries, and return those which match
#your input. For example, searching for "eden" should return "Sweden" in
#the new list, and searching "united" should return "United States of
#America" & "United Kingdom" in the new list. The search functionality
#should be case insensitive (e.g "ireland" should return "Ireland" in the
#new list).
import sqlite3

"""
list_of_countries = ['Albania', 'Andorra', 'Australia', 'Brazil', 'Belgium', 'Canada', 'China', 'France', 'Germany', 'India', 'Indonesia', 'Ireland', 'Italy', 'Japan', 'Kenya', 'Luxembourg', 'Mexico', 'New Zealand', 'Nigeria', 'Portugal', 'Russia', 'South Africa', 'South Korea', 'Spain', 'Sweden', 'Thailand', 'Ukraine', 
                     'United Kingdom', 'United States of America', 'Vietnam', 'Zambia']

start_program_option = input("Do you want to run the program? y/n: ")

if start_program_option == "n":
    print("Program exited.")
else:
    list_of_countries = ['Albania', 'Andorra', 'Australia', 'Brazil', 'Belgium', 'Canada', 'China', 'France', 'Germany', 'India', 'Indonesia', 'Ireland', 'Italy', 'Japan', 'Kenya', 'Luxembourg', 'Mexico', 'New Zealand', 'Nigeria', 'Portugal', 'Russia', 'South Africa', 'South Korea', 'Spain', 'Sweden', 'Thailand', 'Ukraine', 
                     'United Kingdom', 'United States of America', 'Vietnam', 'Zambia']
    print("Available countries:", ', '.join(list_of_countries))
    # shows comma sep strig
    
    while True:
        user_inp = input("Search for a country: ").lower()
        
        new_lst = []
        for i in list_of_countries:
            if user_inp in i.lower():
                new_lst.append(i)
        
        print(new_lst)
        
        x = input("Do you want to continue? y/n: ")
        if x == "n":
            print("Program exited.")
            break
"""

# Connect to the database and set it up
connect_to_database = sqlite3.connect('countries.db')

# Create table for countries if it doesn't exist
connect_to_database.execute('''
CREATE TABLE IF NOT EXISTS countries (
    CountryName TEXT UNIQUE NOT NULL
)
''')

# Insert the list of countries into the table
country_lst = ['Albania', 'Andorra', 'Australia', 'Brazil', 'Belgium', 'Canada', 'China', 'France', 'Germany', 'India', 'Indonesia', 'Ireland', 'Italy', 'Japan', 'Kenya', 'Luxembourg', 'Mexico', 'New Zealand', 'Nigeria', 'Portugal', 'Russia', 'South Africa', 'South Korea', 'Spain', 'Sweden', 'Thailand', 'Ukraine', 
                     'United Kingdom', 'United States of America', 'Vietnam', 'Zambia']
for i in country_lst:
    connect_to_database.execute("INSERT OR IGNORE INTO countries (CountryName) VALUES (?)", (i,))

connect_to_database.commit()

user_option = input("Do you want to run the program? y/n: ")

if user_option == "n":
    print("Program exited.")
else:
    while True:
        print("Available countries:", country_lst)

        user_inp = input("Search for a country: ").lower()
        
        matching_countries = connect_to_database.execute("SELECT CountryName FROM countries WHERE CountryName LIKE ?", ('%' + user_inp + '%',)).fetchall()
        
        # Displaying the matching countries
        new_lst = []
        for i in matching_countries:
            new_lst.append(i[0])
        print(new_lst)
        
        x = input("Do you want to continue? y/n: ")
        print("\n")
        if x == "n":
            print("Program exited.")
            break
            
connect_to_database.close()