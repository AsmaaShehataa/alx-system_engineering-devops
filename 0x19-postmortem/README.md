
![image](https://github.com/AsmaaShehataa/alx-system_engineering-devops/assets/72894781/a5904569-4213-491f-a29d-c09c811b9bab)


Database Outage - Airbnb_v4_Webdynamic date/time 12 -02- 2024 to 13- 02- 2024 15:00 pm GMT - Back to work  13 -02- 2024 17:00 pm GMT

The Issue:-
- in cloning the project of Airbnb specially the dynamic_web part when we are dealing with the database
I experinced an outage in the database when we are sending HTTP requests from the database (server) to the webserver(browser) it returned nothing and wasnot connected to the database we encounter an error that states "erorr 404".


Action taken - investigation/debugging paths that were taken:- 

-first I open mysql DB and connect to the root user 
mysql -u root -p 
I found this error 
![Screenshot](/images/Screenshot.png)

-Then I tried to connect to the database by using this command 
cat 100-dump.sql | mysql -u root -p
 but also I got an error 

 ![Screen2](/images/Screen2.png)

-thirdly I try to connect to MySql database by the root user and based on this error I realised the error is in the password setup itself doesnt matches the policy of Medium policy password vakidation 
so I used this command to change the policy validation of the root user from medium to Low 
like this 
![policy_validate](/images/policy_validate.png)

![policy_val_low](/images/policy_val_low.png)

Finally it worked and when I ran this command  ( cat 100-dump.sql | mysql -u root -p) again 
I got connected to the database and to the webserver gave me the status of 200: OK

![status_ok](//images/status_ok.png)
So my solution was to change the policy validation of the root user from Medium to Low and then reconnect to the database of the Airbnb_cloning prohject




