CREATE TABLE TIM(
    Time_ID VARCHAR2(10) PRIMARY KEY,
    Time_Start DATE NOT NULL,
    Time_End DATE NOT NULL
);

CREATE TABLE SEVERITY(
    Time_Start DATE NOT NULL,
    Time_End DATE NOT NULL,
    Sev_Rating NUMBER NOT NULL,
    CONSTRAINT PK_Severity PRIMARY KEY(Time_Start, Time_End)
);

CREATE TABLE LOC(
    Loc_ID VARCHAR2(10) PRIMARY KEY,
    Loc_Start_Lat NUMBER NOT NULL,
    Loc_Start_Lng NUMBER NOT NULL,
    Loc_End_Lat NUMBER,
    Loc_End_Lng NUMBER
);

CREATE TABLE COORDINATE(
    Loc_Start_Lat FLOAT NOT NULL,
    Loc_Start_Lng FLOAT NOT NULL,
    Loc_Street VARCHAR2(50),
    Loc_City VARCHAR2(50),
    Loc_County VARCHAR2(50) NOT NULL,
    Loc_State VARCHAR2(50) NOT NULL,
    Loc_Country VARCHAR2(10) NOT NULL,
    Loc_Timezone VARCHAR2(20),
    Loc_Airport_Code VARCHAR2(10),
    CONSTRAINT PK_Coordinate PRIMARY KEY(Loc_Start_Lat, Loc_Start_Lng)
);

CREATE TABLE ACCIDENT(
    Acc_ID VARCHAR2(10) PRIMARY KEY,
    Time_ID VARCHAR2(10) NOT NULL,
    Loc_ID VARCHAR2(10) NOT NULL,
    Acc_Source	VARCHAR2(20) NOT NULL,
    Acc_Description  VARCHAR2(500),
    Acc_Distance FLOAT NOT NULL
);

CREATE TABLE WEATHER(
    Time_ID VARCHAR2(10) NOT NULL,
    Loc_ID VARCHAR2(10) NOT NULL,
    Wea_Timestamp DATE,
    Wea_Temperature FLOAT,
    Wea_Condition VARCHAR2(50),
    Wea_Wind_Chill FLOAT,
    Wea_Humidity NUMBER,
    Wea_Visibility FLOAT,
    Wea_Wind_Direction VARCHAR2(10),
    Wea_Wind_Speed FLOAT,
    Wea_Pressure FLOAT,
    Wea_Precipitation FLOAT,
    Constraint PK_Weather PRIMARY KEY(Time_Id,Loc_ID)
);

--Foriegn Key Alterations
ALTER TABLE ACCIDENT
ADD CONSTRAINT FK_ACCIDENT_LOCATION
FOREIGN KEY (Loc_ID)
REFERENCES LOC(Loc_ID);

ALTER TABLE ACCIDENT
ADD CONSTRAINT FK_ACCIDENT_TIME
FOREIGN KEY (Time_ID)
REFERENCES TIM(Time_ID);

ALTER TABLE WEATHER
ADD CONSTRAINT FK_WEATHER_TIME
FOREIGN KEY (Time_ID)
REFERENCES TIM(Time_ID);

ALTER TABLE WEATHER
ADD CONSTRAINT FK_WEATHER_LOCATION
FOREIGN KEY (Loc_ID)
REFERENCES LOC(Loc_ID);

ALTER TABLE TIM
ADD CONSTRAINT FK_TIME_SEVERITY
FOREIGN KEY (Time_Start, Time_End)
REFERENCES SEVERITY(Time_Start, Time_End);

ALTER TABLE LOC
ADD CONSTRAINT FK_Loc_Coordinate
FOREIGN KEY (Loc_Start_Lat,Loc_Start_Lng)
REFERENCES COORDINATE(Loc_Start_Lat,Loc_Start_Lng);
