## cop-3701-traffic-accident-risk-analytics
Tenatively, this project aims to create a database that tracks various traffic accident risk analytics. This includes accident severity, weather, and location. The final database should include features such as the ability to detect accident hotspots, severity ranking, and spatial-temporal query optimization. The users this database is best suited for are traffic operations and similar organizations focused on traffic management/accident prevention. The information and tools of this database can help plan around or prevent potential accidents. The dataset used for this project was collected by traffic APIs between 2016 and 2023, and compiled by Sobhan Moosavi.

I intend to use OrcaleSQL and DatGrip to create the database detailed above. As for the challenges with the application, the challenge comes more with the unfamiliarity with DatGrip than from any particular facet of DatGrip/OracleSQL's functions.

The dataset used for this project is linked below.
[Database Link](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents/data)

### ER Diagram
The user groups for this model are the traffic overseers and street planners who access the data, and the administrator(s) who manage/alter the data as needed. 

Below is the final ER diagram, and the structure that the database actually uses. It is in 3NF.
![Final ER Diagram](https://github.com/I-Cappiello/cop-3701-traffic-accident-risk-analytics/blob/main/Final%20ER%20Diagram.png)


