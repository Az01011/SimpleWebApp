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
''')

# Inserting countries into the table
country_lst = ['Albania', 'Andorra', 'Australia', 'Brazil', 'Belgium', 'Canada', 'China', 'France', 'Germany', 'India', 'Indonesia', 'Ireland', 'Italy', 'Japan', 'Kenya', 'Luxembourg', 'Mexico', 'New Zealand', 'Nigeria', 'Portugal', 'Russia', 'South Africa', 'South Korea', 'Spain', 'Sweden', 'Thailand', 'Ukraine', 'United Kingdom', 'United States of America', 'Vietnam', 'Zambia']
for country in country_lst:
    connect_to_database.execute("INSERT OR IGNORE INTO countries (CountryName) VALUES (?)", (country,))
connect_to_database.commit()

@app.route('/', methods=['GET', 'POST'])
def index():
    countries = ''
    if request.method == 'POST':
        user_inp = request.form['searchTerm'].lower()
        matching_countries = connect_to_database.execute("SELECT CountryName FROM countries WHERE CountryName LIKE ?", ('%' + user_inp + '%',)).fetchall()

        #ouputting searched countries to a list
        matching_countries_list = []
        for record in matching_countries:
            matching_countries_list.append(record[0])
        countries = ', '.join(matching_countries_list)
    return render_template('index.html', countries=countries)

# Running the Flask app
app.run(debug=True, threaded=False)
