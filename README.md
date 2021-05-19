
All the below steps are executed on Ubunu 18.04 . A Step by Step document with Screen shots is attached to the git repo

Assumptions:
1)	Docker and Docker compose is installed.
Postgres Docker Installation:
1)	Create 2 Postgres Docker containers using docker-compose.yml to have source and destination database respectively 
Git Repo:
https://github.com/jameshunt76/glints/tree/main/postgres_docker_compose
Source – root_source_postgres_db_1 (0a4fda6b4566)
Destination – root_dest_postgres_db_1 (594fc8dff8bb)
 
2)	Create table in Source Postgres container and add data (Source – root_source_postgres_db_1)
-	Start the container and exec it
-	Login into postgres using the ID password created in docker-compose.yml file
-	psql -h localhost -p 5432 -U src_airflow -d src_airflow
-	Create table and insert 2 records
 
 
user id-src_airflow
password-src_airflow

Below are the 2 records inserted
 

3)	Create table in Destination Postgres container and add data (Destination – root_dest_postgres_db_1)

-	Start the container and exec it
-	Login into postgres using the ID password created in docker-compose.yml file
-	psql -h localhost -p 5432 -U dest_airflow -d dest_airflow
-	Create table (Must be Empty table)
 
user id-dest_airflow
password-dest_airflow

Airflow Docker Installation:
1)	Install Airflow using the docker-compose.yml attached to the git repo
-	https://github.com/jameshunt76/glints/tree/main/airflow_docker_compose

2)	Run docker ps to make sure all the containers are up and healthy
 

3)	Run docker-compose up to start the webserver and scheduler
 

Create a Dag File:

1)	Create the following file in Airflow container
Git Repo:
https://github.com/jameshunt76/glints/tree/main/dags
File Name: glints_technical_assessment.py

 
2)	Verify the script with below command
Command:
python glints_technical_assessment.py
 

3)	You will see the data like below in the destination. Truncate the table after verifying
 
4)	You must see the DAG on the Web UI
 
5)	Run the DAG manually. Because of the schedule it keeps running and start inserting records.

 
6)	Check the table again.  Since the job is running recurring it keeps on adding record. (Need a fix 😊)
 

Note: The below were required to run the python script

pip install psycopg2-binary
  
