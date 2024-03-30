# NBA PLAYER ANALYTICS DASHBOARD
## Overview

This repo is developed as a capstone project for DataTalks Club's Data Engineering Zoomcamp 2024. The purpose of this project is to apply all the concepts and tools that we have learned and create an end-to-end data pipeline. 
<br>
<br>
The objectives of this specific project are: 
<br>
	- to create end-to-end pipelines to store NBA player statistics data from 1997-present<br>
 	- perform different transformations from this data and show it to a dashboard<br>
  	- this project also utilizes a player point prediction model that calculates a predicted points a player may score on the following match based on historical data <br>

## Index
1. [**Dashboard**](https://github.com/asm-abed/nba-player-analytics-dashboard?tab=readme-ov-file#dashboard) <br>
2. [**Architecture**](https://github.com/asm-abed/nba-player-analytics-dashboard?tab=readme-ov-file#architecture) <br>
   2.1 [**Technologies Used**](https://github.com/asm-abed/nba-player-analytics-dashboard/edit/main/README.md#technologies-used) <br>
3. [**Dataset**](https://github.com/asm-abed/nba-player-analytics-dashboard/edit/main/README.md#dataset) <br>
   3.1 Kaggle NBA Database <br>
   3.2 nba_api data <br>
   3.3 Player Points Prediction Model <br>
4. [**Workflow Orchestration**](https://github.com/asm-abed/nba-player-analytics-dashboard/edit/main/README.md#workflow-orchestration)
   4.1 mage-pipelines filing structure



## Dashboard
You can acces the dashboard through this [**link**](https://lookerstudio.google.com/reporting/2af71728-04ed-40ea-89a0-9612950f50c6). 
<br>
### Page 1: Player Performance Dashboard
![DB Page 1](./misc/dashboard1.png?raw=true "Dasboard Page 1")

### Page 2: Player Season Performance and Prediction Table
![DB Page 2](./misc/dashboard2.png?raw=true "Dasboard Page 2")

## Architecture
![Project Archi](./misc/architecture.png?raw=true "Architecture")

### Technologies Used
In the development of this project, the following tools are used:
- Google Compute Engine as virtual machine in creating pipelines
- Docker to run mage
- Mage as the main workflow orchestration tool
- Google Cloud Storage for the datalake
- Google BigQuery for the data warehouse
- Apache Spark for transformations
- Google Dataproc for submitting Spark jobs
- Looker Studio for the data visualization

## Dataset
  - **Kaggle NBA Data** <br>
   For this project I used the NBA Boxscore Dataset downloaded from [**Kaggle**](https://www.kaggle.com/datasets/szymonjwiak/nba-traditional?select=traditional.csv). The dataset is in csv format which I uploaded to a dedicated GCS bucket. It contains player boxscore data from matches in 1997-2023.

  - **nba_api Data** <br>
   I used the python library nba_api to retrieve boxscore data from the current season which pulls real time data from stats.nba.com api, the same source the Kaggle data is from. You'll find the endpoints and functions of this library in this [**Github Repo**](https://github.com/swar/nba_api)

  - **Player Points Prediction Model** <br>
   I got this model from a study which you'll fine [**here**](https://courses.cs.washington.edu/courses/cse547/23wi/old_projects/23wi/NBA_Performance.pdf). I used the equation they created which the one below:
   ![formula](./misc/formula.png?raw=true "Prediction Formula")

## Workflow Orchestration
![ETL Pipelines](./misc/workflow.png?raw=true "ETL Pipelines")

I created two sets pipelines in Mage as shown, one to load from the Kaggle dataset (historical) and another to retrieve up-to-date data from nba_api and upload them all as partitioned parquet files in the GCS bucket. The pipeline for nba_api can be ran daily to retrieve the latest NBA match data. You can refer to this [**youtube tutorial**](https://www.youtube.com/watch?v=C0fNc8ZOpSI) of how to set instance schedules in Google Compute Engine for Mage pipelines. 

### [mage-pipelines](./mage-pipelines) Filing Structure




