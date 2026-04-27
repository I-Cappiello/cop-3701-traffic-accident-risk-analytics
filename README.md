## Traffic Accident Risk Analytics Database
This project aims to create a database that tracks various traffic accident risk analytics. This includes accident severity, weather, and location. The final database features include the ability to filter by severity, state, location, and time. The user groups for this model are the traffic overseers and street planners who access the data, and the administrator(s) who manage/alter the data as needed. The information and tools can help plan around or prevent potential accidents. The dataset used for this project was collected by traffic APIs between 2016 and 2023, and compiled by Sobhan Moosavi. I used OrcaleSQL and Streamlit to create the database detailed above.

The original 7 million-record dataset used in the database is linked below (the csv file in the repository only contains the first 1000 records).
[Dataset Link](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents/data)

## ER Diagram
This ER diagram is in 3NF, which is why the severity and coordinate entities exist.
**Accident** - A entity representing an individual accident entry. 
**Time** - An entity where each entry represents a unique start and end time.
**Severity** - An entity that stores the severity ranking for every time entity.
**Location** - An entity where each entry represents a unique pair of starting coordinates.
**Coordinante** - An entity that stores the address information for every location entity.
**Weather** - A composite entity that contains the weather data pertaining to a set of times and a set of coordinates. 
![Final ER Diagram](https://github.com/I-Cappiello/cop-3701-traffic-accident-risk-analytics/blob/main/Final%20ER%20Diagram.png)

## How to Use
1. Download repository files and install the light package of Oracle Instant Client.
2. Use create_db.sql to create the database in either FreeSQL or the Oracle Client.
3. If you wish to use a different set of records, add the csv file to the folder you've extracted to, and run preprocess.py. Inside the file, change the value of input_file if the new csv file does not share the same name as Tiny_US_Accidents_March23.csv.
4. Replace configuration variables (LIB_DIR, DB_USER, DB_PASS, and DB_DSN) with your database details. Then run dataload.py to load the data into the database.
5. Run app.py with the command 'streamlit run app.py.'
![App Screenshot](https://github.com/I-Cappiello/cop-3701-traffic-accident-risk-analytics/blob/main/App_Screenshot.png)
**__Using the Features:__**
- **Spatial Coordinate Query:** When a user inputs two sets of coordinates, all accident records with coordinates between those two points are selected.
- **Retrieve State Data:** A user inputs the abbreviation for a state, and all accident records located within the state are selected.
- **Severity Finder:** The user inputs a severity rating (1,2,3,4,5), and all accident records with that rating are selected. To note: severity is determined by the amount of time traffic was delayed (time_start and time_end).
- **City Finder Query:** A user inputs the name of a city, and all accident records with that city listed as the location of the accident are selected.
- **Time Period Query:** A user inputs two dates, and all the accident records with a start time and end time between those two dates are selected.
