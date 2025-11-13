# Status Report

### Datasets

#### Datasets in Planning Stage
  * Original Primary Dataset: Food Inspection
    * URL: https://data.cityofchicago.org/Health-Human-Services/Food-Inspections/4ijn-s7e5/about_data
    * Source: Chicago Data Portal - City of Chicago
    * Format: JSON/CSV
    * Temporal Range: January 2010 to present
    * Update Frequency: Updated daily
    * Number of Rows: 298,000+
    * Columns: Inspection ID, DBA (Doing Business As) Name, AKA (Also Known As) Name, License #, Facility Type, Risk, Address, City, State, Zip, Inspection Date, Inspection Type, Results, Violations, Latitude, Longitude, Location
      
    This dataset will serve as the primary data of the project, as it defines our analytical scope.

  * Original Secondary Dataset: 311 Service Requests
    * URL: https://data.cityofchicago.org/Service-Requests/311-Service-Requests/v6vf-nfxy/about_data
    * Source: Chicago Data Portal - City of Chicago
    * Format: JSON/CSV
    * Temporal Range: December 18th, 2018 to present
    * Update Frequency: Updated multiple times per day
    * Number of Rows: 12,700,000+
    * Columns: SR_Number, SR_Type, SR_Short_Code, Created_Department, Owner_Department, Status, Origin, Created Date, Last Modified Date, Closed Date, Street Address, City, State, Zip_Code, Street_Number, Street_Direction, Street_Name, Street_Type, Duplicate, Legacy_Record, Legacy_SR_Number, Parent_SR_Number, Community_Area, Ward, Electrical_District, Electricity_Grid, Police_Sector, Police_District, Police_Beat, Precinct, Sanitation_Division_Days, Created_Hour, Created_Day_Of_Week, Created_Month, X_Coordinate, Y_Coordinate, Latitude, Longitude, Location

    This dataset will serve as the secondary data of the project, reinforcing the context of our main Food Inspection data.

#### Datasets in Storage and Organization Stage
  * Organized Primary Dataset: Food Inspection
    * URL: https://data.cityofchicago.org/Health-Human-Services/Food-Inspections/4ijn-s7e5/about_data
    * Source: Chicago Data Portal - City of Chicago
    * Format: CSV
    * Temporal Range: January 1st, 2018 to October 6th, 2025
    * Update Frequency: Updated daily
    * Number of Rows: 135,112
    * Columns: Inspection ID, DBA (Doing Business As) Name, AKA (Also Known As) Name, License #, Facility Type, Risk, Address, City, State, Zip, Inspection Date, Inspection Type, Results, Violations, Latitude, Longitude, Location

   The primary dataset was reduced by excluding data beyond the timeliness of the secondary dataset (especially dates before 2018). As a buffer, we included data from January 1st, 2018 to December 17th, 2018. Data in these range can be wiped in the data cleaning stage.
   
  * Organized Secondary Dataset: 311 Service Requests
    * URL: https://data.cityofchicago.org/Service-Requests/311-Service-Requests/v6vf-nfxy/about_data
    * Source: Chicago Data Portal - City of Chicago
    * Format: CSV
    * Temporal Range: December 18th, 2018 to present
    * Update Frequency: Updated multiple times per day
    * Number of Rows: 946,664
    * Columns: SR_Number, SR_Type, SR_Short_Code, Created_Department, Owner_Department, Status, Origin, Created Date, Last Modified Date, Closed Date, Street Address, City, State, Zip_Code, Street_Number, Street_Direction, Street_Name, Street_Type, Duplicate, Legacy_Record, Legacy_SR_Number, Parent_SR_Number, Community_Area, Ward, Electrical_District, Electricity_Grid, Police_Sector, Police_District, Police_Beat, Precinct, Sanitation_Division_Days, Created_Hour, Created_Day_Of_Week, Created_Month, X_Coordinate, Y_Coordinate, Latitude, Longitude, Location
   
  Our secondary dataset was reduced by filtering 'Owner_Department' and 'SR_Type'. We reduced the data to include only from 'Streets and Sanitation' on 'Owner_Department' column. We then picked the five sanitary complaint types (SR_Type) that are strongly related to Food sanitary: 'Rodent Baiting / Rat Complaint, Sanitation Code Violation, Fly Dumping Complaint, Garbage Cart Maintenance, and Dead Animal Pick-Up Request.' 

  Up on Storage and Organization Stage, we decided to import subsets of the original data, since the computational performance was insufficient to perform future stages of the project with the full datasets. Furthermore, the data included unnecessary items because we are using second-hand data, which means that data are not collected for this specific study.

  ##### Data lifecycle

  This project is following the data lifecycle discussed in class.
  The data lifecycle of our project divides into the following stages: Storage/organization, Extraction & Enrichment, Data Integration, Data Quality and Cleaning, and Analysis.
  Currently, our project is at a stage of 'Data Quality and Cleaning.'

  ##### Ethical data handling

  The City of Chicago publicly releases both datasets under government data licenses, which promote their use for analytical processes.
  Our project is using the data for only educational and analytical purposes.

  ##### Storage and organization

  While the City of Chicago data portal provides an API data export, we downloaded data in a CSV file and store a specific version in our GitHub repository under the 'data/raw/' folder.
  This is because the datasets update daily, which may affect the accuracy of our analysis. Also, API only allows upto exporting 1,000 rows without restrictions.
  We will perform data cleaning and integration as well; each of them will be located in 'data/cleaned' and 'data/integrated' directories. (Completed Data integration)

  Our repository stores Jupyter notebook (.ipynb) files for data analysis (coming soon) and integration, Python scripts for potential automation, and Markdown files (ProjectPlan.md, StatusReport.md, and README.md) for documentation.
  

---
    
### Timeline

* {Completed}~~1.) **Data collection and acquisition (10/06)**: Sean has selected the two datasets that are chosen for the course of the project. The primary datset will be Food Inspection where it describes the location of the resturaunt and when the inspection date took place. The secondary dataset will be 311 service Service Request where it gives the location of the where the request is.~~ Completed.

* {Completed}~~2.) **Storage and organization (10/17)**: For our data project, we would use a relational database as our primary storage and organization strategy. This will allow our data to be tabluar format and within a database management system, ideally SQL. For the organization side, we will define a schema that specifies the structure of the table, specifically having primary keys and foreign keys. On the storage side we will save everything to our github page to have easy acess while having different file forms to seperate data.~~

   When importing datasets from the City of Chicago, we imported subsets of the datasets due to the file sizes exceeding the computational power in the future steps.
   For further details on this, please check the 'Datasets' section above.

* {Completed}~~3.) **Extraction and Enrichment (10/24)**: Although both of our datsets are form into structured data, Enrichment and Extraction of each datasets are important, for example:~~
    ~~* Extracting 311 calls that is related to sanitary issues as we are comparing the 311 calls to the food inspection dataset~~
    ~~* Extracting Zip codes from both datsets~~
    ~~* Enrichment still applies as we can use the addresses or locations of inspections and 311s calls to see if the City of Chicago is targeting a specific location.~~ Completed.
     
* {Completed}~~4.) **Data Integration (10/31)**: Data integration will be performed using shared spatial and temporal keys:~~
    ~~* Spatial key: ZIP code, Location (Latitude, Longitude)~~
    ~~* Temporal key: Date of inspection, Date of 311 report~~

    We decided to use ZIP code to aggregate our datasets. When two datasets were joined with Location (Latitude, Longitude), we have too little entries matching its value.
    For initial analysis, temporal keys are not going to be used. This is because we do not know when the food inspection take places, making difficult to match.
    Also, our main purpose of analysis is to find the area (zip code) with most sanitary issue and compare it with food inspections data. 
    
    Using the DuckDB or Pandas library, we will perform a left join of the food inspection (primary) data with aggregated 311 (secondary) data, ensuring each inspection record includes contextual information about recent complaint activity within its area and timeframe.
    - Update on Data Integration: We used pandas to join two datasets 
  
* 5.)**Data Quality (11/07)**: Despite the datasets being well-maintained, they are likely to have issues shared by municipal data:
    * Missing ZIP codes and addresses
    * Duplicate inspection IDs or 311 complaints
  
* 6.)**Data Cleaning (11/14)**: Data cleaning will:
    * Remove duplicate records
    * Remove missing values in location columns
    * Convert data types if needed
  
* 7.)**Workflow automation and provenance(11/21)**: This process we will smoothly integrate our two clean datsets and have a built code where the code could have a new category having a row categorize which part of Chicago the resturaunt is located. Example: Northside, southside, downtown, etc. At the same time having the data being automaticaly being cleaned.
  
* 8.)**Reproducibility and transparency (11/28)**: Disclosing what are processed was and how we were able to clean the data.
  
* 9.)**Meta and Data Documentation (12/10)**: Giving background information of the data and idetifiying the variables and the variables that were useful to answering our research questions. 
