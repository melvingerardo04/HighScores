# Run the Query below in your local to Create database. 
	CREATE DATABASE Game_Dev

# After Creating Database. Now Create a table for saving  

	CREATE TABLE high_score (id INT (11) NOT NULL PRIMARY KEY AUTO_INCREMENT,name VARCHAR (255), 
  	score INT (11),categories VARCHAR (50),
	type VARCHAR (50), date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP )