# py_flask_web_app
A basic web app template built with Python Flask framework
### WARNING: ONLY TESTED ON LINUX MACHINES AT THIS POINT ###

DEPENDENCIES-->PIP/PIP3 INSTALL FOR PYTHON PLUS:
* flask
* flask_mysqldb
* wtforms
* passlib
* functools
- python3.7+
- git
- MySQL

DOWNLOAD AND RUN INSTRUCTIONS
* Clone repo and ensure all DEPENDENCIES are installed and up-to-date
* Log into MySQL:
  mysql -u root -p    # Or another MySQL user who can CREATE new databases and tables
  CREATE DATABASE flask_app_dp;
  ### NOTE: The database name is used in app.py in the "Config MySQL" section
  ### app.config['MYSQL_DB'] = 'flask_app_db' <-- Change this to any database you want to use
  USE flask_app_db;
  
  CREATE TABLE users(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), email VARCHAR(100), username VARCHAR(50), password VARCHAR(100), register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
  
  CREATE TABLE articles(id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), author VARCHAR(100), body TEXT, create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
  
  exit;   # EXIT OUT OF MYSQL
  
  cd into cloned repo
  ### The following terminal command should launch the flask_app on your machine's localhost:
  python3 app.py
  ### Open a web browser (Firefox, Chrome, etc.) and type "localhost:5000/home" into the url address bar
  ### Please note that ":5000" is the port number that flask uses when launched and this number may be different on some Operating Systems (OS)
  ### Check the terminal output to confirm the port number that flask_app is running on
  ### To shut down the server:
  ctrl+C
  
  #### In the event that the flask_app home page does not load, please double check all DEPENDENCIES are up-to-date and that the MySQL database is functioning properly
  #### If problems continue, please consult stackoverflow or similar community boards for help loading a flask application on your system
  
