import csv, sqlite3

con = sqlite3.connect("RealWorldData.db")
cur = con.cursor()

!pip install -q pandas==1.1.5

%load_ext sql

%sql sqlite:///RealWorldData.db

import pandas

df = pandas.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoPublicSchools.csv")
df.to_sql("CHICAGO_PUBLIC_SCHOOLS_DATA", con, if_exists='replace', index=False, method="multi")

# type in your query to retrieve list of all tables in the database
%sql SELECT name FROM sqlite_master WHERE type="table"

# query para saber cuantas columnas hay
%sql SELECT count(name) FROM PRAGMA_TABLE_INFO('CHICAGO_PUBLIC_SCHOOLS_DATA');

# type in your query to retrieve all column names in the SCHOOLS table along with their datatypes and length
%sql SELECT name,type,length(type) FROM PRAGMA_TABLE_INFO('CHICAGO_PUBLIC_SCHOOLS_DATA');

#Cuantas Elementary schools hay en la data
%sql SELECT COUNT(*) FROM CHICAGO_PUBLIC_SCHOOLS_DATA Where "Elementary, Middle, or High School"='ES'

#Cual es el dato mayor
%sql SELECT MAX(SAFETY_SCORE) FROM CHICAGO_PUBLIC_SCHOOLS_DATA;

#cual es el colegio con el dato mayor
%sql select Name_of_School, Safety_Score from CHICAGO_PUBLIC_SCHOOLS_DATA where \
  Safety_Score= (select MAX(Safety_Score) from CHICAGO_PUBLIC_SCHOOLS_DATA)

#cual es el top 10 con el mayor promedio 
%sql select Name_of_School, Average_Student_Attendance from CHICAGO_PUBLIC_SCHOOLS_DATA \
    order by Average_Student_Attendance desc nulls last limit 10 

#cual es el top 5 de las escuelas que no fueron
%sql select Name_of_School, Average_Student_Attendance from CHICAGO_PUBLIC_SCHOOLS_DATA \
    order by Average_Student_Attendance limit 5 
