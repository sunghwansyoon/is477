# IS 477 - Data Management, Curation & Reproducibility


### Overview

What comes to your mind when you think about Chicago? Skyscraper? Jazz and blues music? The musical?
These are all great representations of Chicago. Yet, Chicago has a strong culinary identity; it even has a dish named after its city: Chicago-style pizza.
While serving delicious food is crucial to becoming a city of appetite, sanitation around food places is as important.
The City of Chicago's Department of Public Health conducts the city's food inspections to make sure food served on the table is not only delicious but safe.
The sanitation of the whole city is in charge by the 311 non-emergency system, where they receive hundreds of reports weekly. 

This project aims to bring these two public datasets together into one integrated analysis.
Specifically, we want to explore whether food inspection results correlate with 311 sanitation and rodent complaints across Chicago's neighborhood.
We hypothesize that food places that receive failure or conditional tend to have a higher rate of sanitation reports.

Beyond the technical analysis, our project may explore how civic engagement can affect public health outcomes.

---

### Research Questions

This project will answer the following research questions:
1. Are Chicago neighborhoods with higher counts of 311 sanitation complaints also more likely to have restaurants that received a fail for city food inspections?
2. Does an increase in 311 sanitation reports precede or follow an increase in failure in food inspections?
3. Are there specific facilities that are more sensitive to external sanitation compared to others?

---

### Team
  * Sean Yoon
    * Responsible for managing the GitHub repository
    * Co-working on data integration and cleaning, exploratory analysis, and visualization
    * Proposed Project Plan
  * Nathan Diaz
    * Working on overall background research on the city of Chicago 311 calls and city inspection on resturants 
    * Co-working on data integration and cleaning, exploratory analysis, and visualization
    *

---

### Datasets
  * Primary Dataset: Food Inspection
    * URL: https://data.cityofchicago.org/Health-Human-Services/Food-Inspections/4ijn-s7e5/about_data
    * Source: Chicago Data Portal - City of Chicago
    * Format: JSON/CSV
    * Temporal Range: January 2010 to present
    * Update Frequency: Updated daily
    * Number of Rows: 298,000+
    * Columns: Inspection ID, DBA (Doing Business As) Name, AKA (Also Known As) Name, License #, Facility Type, Risk, Address, City, State, Zip, Inspection Date, Inspection Type, Results, Violations, Latitude, Longitude, Location
      
    This dataset will serve as the primary data of the project, as it defines our analytical scope.


  * Secondary Dataset: 311 Service Requests
    * URL: https://data.cityofchicago.org/Service-Requests/311-Service-Requests/v6vf-nfxy/about_data
    * Source: Chicago Data Portal - City of Chicago
    * Format: JSON/CSV
    * Temporal Range: December 18th, 2018 to present
    * Update Frequency: Updated multiple times per day
    * Number of Rows: 12,700,000+
    * Columns: SR_Number, SR_Type, SR_Short_Code, Created_Department, Owner_Department, Status, Origin, Created Date, Last Modified Date, Closed Date, Street Address, City, State, Zip_Code, Street_Number, Street_Direction, Street_Name, Street_Type, Duplicate, Legacy_Record, Legacy_SR_Number, Parent_SR_Number,    Community_Area, Ward, Electrical_District, Electricity_Grid, Police_Sector, Police_District, Police_Beat, Precinct, Sanitation_Division_Days, Created_Hour, Created_Day_Of_Week, Created_Month, X_Coordinate, Y_Coordinate, Latitude, Longitude, Location

    This dataset will serve as the secondary data of the project, reinforcing the context of our main Food Inspection data. 

  By matching the location information available in both datasets, we can track foodservice establishments in Chicago that received food inspections from January 2019 to September 2025.

  ##### Data lifecycle

  This project will follow the data lifecycle discussed in class. So far, we are using data collected by the City of Chicago. Thus, the data lifecycle of our project includes Storage/organization, Extraction & Enrichment, Data Integration, Data Quality and Cleaning, and Analysis.


  ##### Ethical data handling

  The City of Chicago publicly releases both datasets under government data licenses, which promote their use for analytical processes.
  Our project will use the data for only educational and analytical purposes.


  ##### Storage and organization

  While the City of Chicago data portal provides an API data export, we will download data in a CSV file and store a specific version in our GitHub repository under the 'data/raw/' folder.
  This is because the datasets update daily, which may affect the accuracy of our analysis.
  We will perform data cleaning and integration as well; each of them will be located in 'data/cleaned' and 'data/integrated' directories.

  Our repository will also store a Jupyter notebook for data analysis, Python scripts for potential automation, and Markdown files (ProjectPlan.md, StatusReport.md, and README.md) for documentation.

---
    
### Timeline

* 1.) **Data collection and acquisition (10/06)**:Sean has selected the two datasets that are chosen for the course of the project. The primary datset will be Food Inspection where it describes the location of the resturaunt and when the inspection date took place. The secondary dataset will be 311 service Service Request where it gives the location of the where the request is.

* 2.) **Storage and organization (xx/xx)**: For our data project, we would use a relational databse as our primary storage and organization strategy. This will allow our data to be tabluar format and within a database management system, ideally SQL. For the organization side, we will define a schma that specifies the structure of the table, specifically having primary keys and foreign keys. On the storage side we will save everything to our github page to have easy acess while having different file forms to seperate data.

* 3.) **Extraction and Enrichment (xx/xx)**: Although both of our datsets are form into structured data, Enrichment and Extraction of each datasets are important, for example:
    * Extracting 311 calls that is relted to food or restraunt calls as we are comparing the 311 calls to the food inspection dataset
    * Extracting identical or similar close address from both datsets
    * Enrichment still applies as we can use the addresses or locations of inspections and 311s calls to see if the city of chicago is targeting a specific location.
     
* 4.) **Data Integration (xx/xx)**: Data integration will be performed using shared spatial and temporal keys:
    * Spatial key: ZIP code, Location (Latitude, Longitude)
    * Temporal key: Date of inspection, Date of 311 report 
    
    Using the DuckDB or Pandas library, we will perform a left join of the food inspection (primary) data with aggregated 311 (secondary) data, ensuring each inspection record includes contextual information about recent complaint activity within its area and timeframe.
  
* 5.)**Data Quality (xx/xx)**: Despite the datasets being well-maintained, they are likely to have issues shared by municipal data:
    * Missing ZIP codes and addresses
    * Duplicate inspection IDs or 311 complaints
  
* 6.)**Data Cleaning (xx/xx)**: Data cleaning will:
    * Remove duplicate records
    * Remove missing values in location columns
    * Convert data types if needed
  
* 7.)**Workflow automation and provenance**(xx/xx): This process we will smoothly integrate our two clean datsets where we are able to answer our research questions. 
  
* 8.)**Reproducibility and transparency (xx/xx)**: By displaying our datset into python, where we are able to clean the dataset to adress our goals for data cleaning and data quality. 
  
* 9.)**Meta and Data Documentation (xx/xx)**: Through our outisde research of meta and data documentation, we will achieve this by making sure the 

---

### Constraints
* Reporting Bias: 311 complaints are voluntary reports; Neighborhoods can be underrepresented or overrepresented.
* Time Matching: Food inspection does not occur periodically, so precise temporal alignment might be burdensome.

---

### Gaps
* Workflow automation and provenance: Our project may be able to implement automation by fetching the latest data from APIs, and output correlation and visualization analysis. We would need additional inputs for this process.
* Machine Learning Implementation: We can further extend our project by building a simple logistic regression model that determines pass/fail on food inspections based on 311 reports data, if there is a significant correlation between 311 reports and food inspections data.
