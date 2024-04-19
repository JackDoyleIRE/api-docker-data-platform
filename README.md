# Project Readme

## General Overview

The project provides a self contained miniture data platform running in docker

## Objective and Architectural Decisions

The objective of this project is to provide an architecture for ingesting data, performing analytics, and storing results. Key architectural decisions include the utilization of Docker containers for services isolation, a PostgreSQL database for data storage, and Python scripts for data ingestion and analytics. 

Also a a folder called object_store is used to mimic a cloud object store such as S3. The idea here is the code would be more portable to a cloud enviroment with some modifications. 

## How to Run

To start the project, navigate to the root of the project directory and run the following command:

make start

The db service will persist so you can press `Ctrl + C` to stop running the container

To tear down the project and remove the containers run:

make stop

## Service Overview

### Ingestion Service
The ingestion service is responsible for fetching data from the API end points, storing the json in the object store and then loading to the database. It utilizes a Python script (`main.py`) for running the ingestion and also make use of an the `api_operator.py` file. The `schema.py` file defines the schema for the database in partnership with the `init.sql` file the db service.

### Analytics Service
The analytics service executes the sql models on ingested data and outputs the end report. It consists of SQL scripts for data analysis. Results are stored in the `output` directory. This service is dependent on the completion of the ingestion service before it can start.

### Database
A PostgreSQL database is used for storing data. The `init.sql` file contains the initialization script for setting up the database schema. 

## Improvements

- Some secrets management is demonstrated using the api_key but this should be extedend for the db credentials which are currently hard coded in multiple places.
- The insert to database section of the ingestion service has duplicate code and non dynamic values so these should be add to their own class method for db operations
- Make use of a real cloud environment and object store 
- Use services like dbt for the sql modeling and airflow for the orchestration. Right now is a strange mix of python and docker. 
- Add some testing and validation on the python and sql side. 