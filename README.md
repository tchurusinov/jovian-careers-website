# jovian-careers-website
A careers website for Jovian

## Database-driver web apps

- basically real course starts at 02:22, rest is a recap of previous actions
- for a cloud db, he uses planetscale.com

## db creation and connection

- he creates a mysql database, then through mysql workbench, connection is made
```
SHOW DATABASES;   - display all available databases
USE <db name>
SHOW TABLES;   - display tables 
CREATE TABLE <name> (
    id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(250) NOT NULL,
    location VARCHAR(250) NOT NULL,
    salary INT,
    currency VARCHAR(10),
    responsiblities VARCHAR(2000),
    requirements VARCHAR(2000),
    PRIMARY KEY(id)
);           - will create a table with the specified name and columns
SELECT * FROM <name>;
INSERT INTO <name> (col, names) VALUES ('val1', 'val2')    - to manually insert
```

- connection to the database - can be seen in `database.py`
- code is present but for a non-existent db, as the theory is what is important, this can be connected to any db

## dynamic webpages 

- in a way, connecting the db to the domain is making it dynamic as it will load diff things, based on contents of db
- he showed how to add a secret by using env variables and key-value pairs, how through github? how when local?

- but now, for dynamic webpages - each job opening to have its own page - basically not much different than the rest api, just it renders another html
- speaking of that, he then focuses again on styling the html and css with bootstrap, so just copy-pasted the code there

## html applications handling

- this is the last step, basically implementing the option to take applications from the webpge and upload to the database
- applications table needs to be created
```
CREATE TABLE applications (
  id INT NOT NULL AUTO_INCREMENT,
  job_id INT NOT NULL,
  full_name VARCHAR(250) NOT NULL,
  email VARCHAR(250) NOT NULL,
  linkedin_url VARCHAR(500),
  education VARCHAR(2000),
  work_experience VARCHAR(2000),
  resume_url VARCHAR(500),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);
```
VIDEO DONE