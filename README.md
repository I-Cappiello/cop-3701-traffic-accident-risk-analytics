## Traffic Accident Risk Analytics Database
This project aims to create a database that tracks various traffic accident risk analytics. This includes accident severity, weather, and location. The final database should include features such as the ability to detect accident hotspots, filtering by severity, and spatial-temporal query optimization. The users this database is best suited for are traffic operations and similar organizations focused on traffic management/accident prevention. The information and tools of this database can help plan around or prevent potential accidents. The dataset used for this project was collected by traffic APIs between 2016 and 2023, and compiled by Sobhan Moosavi. I intend to use OrcaleSQL and VScode to create the database detailed above.

The original 7 million-record dataset used in the database is linked below (the csv in the repository only contains the first 1000 records).
[Database Link](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents/data)

## ER Diagram
The user groups for this model are the traffic overseers and street planners who access the data, and the administrator(s) who manage/alter the data as needed. 

![Final ER Diagram](https://github.com/I-Cappiello/cop-3701-traffic-accident-risk-analytics/blob/main/Final%20ER%20Diagram.png)

## How to Use
1. Download repo files and make sure you have the light package of oracle instant client downloaded.
2. Use create_db.sql to create the database in either FreeSQL or the Oracle Client.
3. If you wish to use a different set of records, add the csv file into the folder you've stored the files in, and run preprocess.py. Inside of the file, change the value of input_file if the new csv file does not share the same name as Tiny_US_Accidents_March23.csv.
4. Run dataload.py to load the data into the database. Replace configuration variables (LIB_DIR, DB_USER, DB_PASS, and DB_DSN) with your database details.
5. Run app.py with the command 'streamlit run app.py'

Using the Features:
- **Spatial Coordinate Query:** When a user inputs two sets of coordinates, all accidents records with coordinates between those two points are selected.
- **Retrieve State Data:** A user inputs the abbreviation for a state, and all accident records located within the state are selected.
- **Severity Finder:** The user inputs a severity rating (1,2,3,4,5) and all accidents records with that rating are selected. To note: severity is determined by the amount of time traffic was delayed (time_start and time_end).
- **City Finder Query:** A user inputs the name of a city, and all accident records with that city listed as the location of the accident are selected.
- **Time Period Query:** A user inputs two dates, and all the accident records with a start time and end time between those two dates are selected.
