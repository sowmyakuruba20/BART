# BART Time and Fare Calculator
Welcome to the BART Time and Fare Calculator repository! This application provides a convenient way to calculate the travel time and fare between any two BART (Bay Area Rapid Transit) stations.

# Overview
The BART Time and Fare Calculator consists of a Flask application that connects to a Neo4j graph database. It utilizes the "shortest path" algorithm to determine the optimal route between the selected source and destination stations. The application provides real-time data and accurate fare calculations based on the BART fare system.

# Prerequisites
Before running the BART Time and Fare Calculator, ensure that you have the following installed:
1. Python 3.x
2. Flask
3. Neo4j

# Installation
Follow the steps below to set up and run the application:

1. Clone this repository to your local machine.
2. Install the necessary dependencies by running the following command:
pip install -r requirements.txt
3. Configure the Neo4j database connection settings in app.py. Make sure to provide the correct hostname, port, username, and password.
4. Start the application by running the following command:
python app.py
5. Open your web browser and navigate to http://localhost:5000 to access the BART Time and Fare Calculator.

# How to Use
1. Upon accessing the application, you will see a user-friendly interface where you can select your source and destination stations from drop-down menus.
2. After selecting the stations, click on the "Calculate" button to obtain the travel time and fare information.
3. The application will display the estimated travel time in minutes and the fare amount in USD.
4. Feel free to explore different source and destination combinations to find the optimal routes and fare details.

To access the detailed walkthrough, instructions, and code examples, please visit the following link:
https://medium.com/@sowmya.kuruba/bart-using-neo4j-d2e58812bb6a

# Acknowledgements
We would like to express our gratitude to the developers and contributors of the following tools and libraries used in this project:

Flask: https://flask.palletsprojects.com
Neo4j: https://neo4j.com
