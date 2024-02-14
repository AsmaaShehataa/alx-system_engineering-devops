Database Outage - Airbnb_v4_Webdynamic date/time 12 -02- 2024 to 13- 02- 2024 15:00 pm GMT - Back to work  13 -02- 2024 17:00 pm GMT

The Issue:-
- in cloning the project of Airbnb specially the dynamic_web part when we are dealing with the database
I experinced an outage in the database when we are sending HTTP requests from the database (server) to the webserver(browser) it returned nothing and wasnot connected to the database we encounter an error that states "erorr 404".


Action taken - investigation/debugging paths that were taken:- 

first I open mysql DB and connect to the root user 
mysql -u root -p 
I found this error 
![Screenshot](Screenshot.png)

