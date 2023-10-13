from flask import Flask, render_template, request, redirect, url_for
import sqlite3

# Setting up Flask
app = Flask(__name__)
# Connecting to the sql database and setting up the table
connect_to_database = sqlite3.connect('countries.db', check_same_thread=False)
connect_to_database.execute('''
CREATE TABLE IF NOT EXISTS countries (
    CountryName TEXT UNIQUE NOT NULL
)
''') #single column

# Inserting countries into the table
country_lst = ['Albania', 'Andorra', 'Australia', 'Brazil', 'Belgium', 'Canada', 'China', 'France', 'Germany', 'India', 'Indonesia', 'Ireland', 'Italy', 'Japan', 'Kenya', 'Luxembourg', 'Mexico', 'New Zealand', 'Nigeria', 'Portugal', 'Russia', 'South Africa', 'South Korea', 'Spain', 'Sweden', 'Thailand', 'Ukraine', 'United Kingdom', 'United States of America', 'Vietnam', 'Zambia']
for country in country_lst:
    connect_to_database.execute("INSERT OR IGNORE INTO countries (CountryName) VALUES (?)", (country,))
connect_to_database.commit() #looping and inserting

#@app - index runs when / is accessed
@app.route('/', methods=['GET', 'POST']) #single route handls both get and post
def index():
    empty_lst = []
    if request.method == 'POST':  #user input captured
        user_inp = request.form['searchTerm'].lower()
        matching_countries = connect_to_database.execute("SELECT CountryName FROM countries WHERE CountryName LIKE ?", ('%' + user_inp + '%',)).fetchall()
    
        for i in matching_countries: 
            empty_lst.append(i[0])

    return render_template('index.html', x=empty_lst)


# Running the Flask app
app.run(debug=True, threaded=False) #threaded = false was a fix for error