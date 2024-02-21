0x1A-application_server

Task 0 
ubuntu@431760-web-01:~$ git clone https://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@github.com/AsmaaShehataa/AirBnB_clone_v2.git
Cloning into 'AirBnB_clone_v2'...
remote: Enumerating objects: 667, done.
remote: Total 667 (delta 0), reused 0 (delta 0), pack-reused 667
Receiving objects: 100% (667/667), 127.53 KiB | 5.54 MiB/s, done.
Resolving deltas: 100% (328/328), done.
ubuntu@431760-web-01:~$ ls
0-iamsomeoneelse       AirBnB_clone_v2                ddagent-install.log                temp_mysql_v
0-setup_web_static.sh  alx-system_engineering-devops  mysql-apt-config_0.8.12-1_all.deb  tyrell_corp.sql
ubuntu@431760-web-01:~$ cd AirBnB_clone_v2/
ubuntu@431760-web-01:~/AirBnB_clone_v2$ ls
0-setup_web_static.sh    101-setup_web_static.pp    7-dump.sql  console.py  main_delete.py       setup_mysql_test.sql  tests      web_static
1-pack_web_static.py     2-do_deploy_web_static.py  AUTHORS     file.json   models               test.py               transfer
100-clean_web_static.py  3-deploy_web_static.py     README.md   main.py     setup_mysql_dev.sql  test_params_create    web_flask
ubuntu@431760-web-01:~/AirBnB_clone_v2$ cd ..
ubuntu@431760-web-01:~$ ls
0-iamsomeoneelse       AirBnB_clone_v2                ddagent-install.log                temp_mysql_v
0-setup_web_static.sh  alx-system_engineering-devops  mysql-apt-config_0.8.12-1_all.deb  tyrell_corp.sql
ubuntu@431760-web-01:~$ sudo apt install -y net-tools
Reading package lists... Done
Building dependency tree       
Reading state information... Done
net-tools is already the newest version (1.60+git20180626.aebd88e-1ubuntu1).
0 upgraded, 0 newly installed, 0 to remove and 77 not upgraded.
ubuntu@431760-web-01:~$ sudo get-apt update
sudo: get-apt: command not found
ubuntu@431760-web-01:~$ sudo apt-get update
Hit:1 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal InRelease
Get:2 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal-updates InRelease [114 kB]                                                         
Hit:3 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal-backports InRelease                                                                
Hit:4 http://repo.mysql.com/apt/ubuntu bionic InRelease                                                                                       
Ign:5 https://apt.datadoghq.com stable InRelease                                                                                              
Hit:6 https://apt.datadoghq.com stable Release                                                         
Hit:7 http://security.ubuntu.com/ubuntu focal-security InRelease
Get:8 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal-updates/main amd64 Packages [3109 kB]
Get:9 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal-updates/main Translation-en [498 kB]
Get:10 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal-updates/restricted amd64 Packages [2689 kB]
Get:11 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal-updates/restricted Translation-en [374 kB]
Get:12 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal-updates/universe amd64 Packages [1165 kB]
Get:13 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal-updates/universe Translation-en [279 kB]
Fetched 8229 kB in 3s (3203 kB/s)                          
Reading package lists... Done
ubuntu@431760-web-01:~$ sudo apt install -y net-tools
Reading package lists... Done
Building dependency tree       
Reading state information... Done
net-tools is already the newest version (1.60+git20180626.aebd88e-1ubuntu1).
0 upgraded, 0 newly installed, 0 to remove and 77 not upgraded.
ubuntu@431760-web-01:~$ pip show flask

Command 'pip' not found, but can be installed with:

sudo apt install python3-pip

ubuntu@431760-web-01:~$ sudo apt install python3.8-venv
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  python-pip-whl
The following NEW packages will be installed:
  python-pip-whl python3.8-venv
0 upgraded, 2 newly installed, 0 to remove and 77 not upgraded.
Need to get 1811 kB of archives.
After this operation, 2339 kB of additional disk space will be used.
Do you want to continue? [Y/n] Y
Get:1 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal-updates/universe amd64 python-pip-whl all 20.0.2-5ubuntu1.10 [1805 kB]
Get:2 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal-updates/universe amd64 python3.8-venv amd64 3.8.10-0ubuntu1~20.04.9 [5452 B]
Fetched 1811 kB in 0s (29.6 MB/s)   
Selecting previously unselected package python-pip-whl.
(Reading database ... 120234 files and directories currently installed.)
Preparing to unpack .../python-pip-whl_20.0.2-5ubuntu1.10_all.deb ...
Unpacking python-pip-whl (20.0.2-5ubuntu1.10) ...
Selecting previously unselected package python3.8-venv.
Preparing to unpack .../python3.8-venv_3.8.10-0ubuntu1~20.04.9_amd64.deb ...
Unpacking python3.8-venv (3.8.10-0ubuntu1~20.04.9) ...
Setting up python-pip-whl (20.0.2-5ubuntu1.10) ...
Setting up python3.8-venv (3.8.10-0ubuntu1~20.04.9) ...
ubuntu@431760-web-01:~$ ls
0-iamsomeoneelse       AirBnB_clone_v2                ddagent-install.log                temp_mysql_v
0-setup_web_static.sh  alx-system_engineering-devops  mysql-apt-config_0.8.12-1_all.deb  tyrell_corp.sql
ubuntu@431760-web-01:~$ python3 -m venv airbnb2
ubuntu@431760-web-01:~$ ls
0-iamsomeoneelse       AirBnB_clone_v2  alx-system_engineering-devops  mysql-apt-config_0.8.12-1_all.deb  tyrell_corp.sql
0-setup_web_static.sh  airbnb2          ddagent-install.log            temp_mysql_v
ubuntu@431760-web-01:~$ source airbnb2/bin/activate
(airbnb2) ubuntu@431760-web-01:~$ cd AirBnB_clone_v2
(airbnb2) ubuntu@431760-web-01:~/AirBnB_clone_v2$ pip install flask 
Collecting flask
  Downloading flask-3.0.2-py3-none-any.whl (101 kB)
     |████████████████████████████████| 101 kB 10.7 MB/s 
Collecting Werkzeug>=3.0.0
  Downloading werkzeug-3.0.1-py3-none-any.whl (226 kB)
     |████████████████████████████████| 226 kB 33.9 MB/s 
Collecting click>=8.1.3
  Downloading click-8.1.7-py3-none-any.whl (97 kB)
     |████████████████████████████████| 97 kB 10.3 MB/s 
Collecting Jinja2>=3.1.2
  Downloading Jinja2-3.1.3-py3-none-any.whl (133 kB)
     |████████████████████████████████| 133 kB 53.6 MB/s 
Collecting importlib-metadata>=3.6.0; python_version < "3.10"
  Downloading importlib_metadata-7.0.1-py3-none-any.whl (23 kB)
Collecting blinker>=1.6.2
  Downloading blinker-1.7.0-py3-none-any.whl (13 kB)
Collecting itsdangerous>=2.1.2
  Downloading itsdangerous-2.1.2-py3-none-any.whl (15 kB)
Collecting MarkupSafe>=2.1.1
  Downloading MarkupSafe-2.1.5-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (26 kB)
Collecting zipp>=0.5
  Downloading zipp-3.17.0-py3-none-any.whl (7.4 kB)
Installing collected packages: MarkupSafe, Werkzeug, click, Jinja2, zipp, importlib-metadata, blinker, itsdangerous, flask
Successfully installed Jinja2-3.1.3 MarkupSafe-2.1.5 Werkzeug-3.0.1 blinker-1.7.0 click-8.1.7 flask-3.0.2 importlib-metadata-7.0.1 itsdangerous-2.1.2 zipp-3.17.0
(airbnb2) ubuntu@431760-web-01:~/AirBnB_clone_v2$ vi web_flask/0-hello_route.py
(airbnb2) ubuntu@431760-web-01:~/AirBnB_clone_v2$ python3 -m web_flask.0-hello_route
 * Serving Flask app '0-hello_route'
 * Debug mode: off
Address already in use
Port 5000 is in use by another program. Either identify and stop that program, or start the server with a different port.
(airbnb2) ubuntu@431760-web-01:~/AirBnB_clone_v2$ netstat -tuln | grep 5000
tcp        0      0 127.0.0.1:5000          0.0.0.0:*               LISTEN     
(airbnb2) ubuntu@431760-web-01:~/AirBnB_clone_v2$ sudo lsof -i :5000
COMMAND    PID     USER   FD   TYPE  DEVICE SIZE/OFF NODE NAME
agent   345640 dd-agent    9u  IPv4 2888337      0t0  TCP localhost:5000 (LISTEN)
(airbnb2) ubuntu@431760-web-01:~/AirBnB_clone_v2$ sudo kill 345640
(airbnb2) ubuntu@431760-web-01:~/AirBnB_clone_v2$ python3 -m web_flask.0-hello_route
 * Serving Flask app '0-hello_route'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://10.247.222.190:5000
Press CTRL+C to quit

2nd window 


Last login: Wed Feb 21 12:48:39 2024 from 154.180.126.30
ubuntu@431760-web-01:~$ ls
0-iamsomeoneelse       AirBnB_clone_v2  alx-system_engineering-devops  mysql-apt-config_0.8.12-1_all.deb  tyrell_corp.sql
0-setup_web_static.sh  airbnb2          ddagent-install.log            temp_mysql_v
ubuntu@431760-web-01:~$ cd AirBnB_clone_v2/
ubuntu@431760-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1:5000/airbnb-onepage/
Hello HBNB!ubuntu@431760-web-01:~/AirBnB_clone_v2$ 


