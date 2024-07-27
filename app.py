from flask import Flask, render_template, redirect, url_for
import json
import random

app = Flask(__name__,
            static_folder="static/")

# Function to read the JSON data from the file
def read_mission_data(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

# Function to select a random primary mission
def select_random_primary_mission(mission_data):
    return random.choice(mission_data['primaryMissions'])

# Function to select a random mission rule
def select_random_mission_rule(mission_data):
    return random.choice(mission_data['missionRules'])

# Function to select a random deployment
def select_random_deployment(mission_data):
    return random.choice(mission_data['deployments'])

@app.route('/', methods=['GET', 'POST'])
def index():
    # Read mission data from file
    filename = 'missions/genericmissions.json'
    mission_data = read_mission_data(filename)
    
    # Generate random selections
    primary_mission = select_random_primary_mission(mission_data)
    mission_rule = select_random_mission_rule(mission_data)
    deployment = select_random_deployment(mission_data)

    # Pass the selections to the template for display
    return render_template('index.html', 
                           primary_mission=primary_mission,
                           mission_rule=mission_rule,
                           deployment=deployment)

if __name__ == "__main__":
    app.run(debug=True)