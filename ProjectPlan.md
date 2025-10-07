# IS 477 - Data Management, Curation & Reproducibility


### Overview
##### Describe the overall goal of your project.

---

### Research Questions
##### What is/are the question(s) you intend to address?

This project will answer the following research questions:
1. Are Chicago neighborhoods with higher counts of 311 sanitation complaints also more likely to have restaurants that received a fail for city food inspections?
2. Does an increase in 311 sanitation reports precede or follow an increase in failure in food inspections?

---

### Team
  * Sean Yoon
  * Nathan Diaz

---

### Datasets
##### Identify and describe the datasets that you will use. You need to use at least two different datasets that need to be integrated.
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

---
    
### Timeline
##### Document the plan and timeline for implementing your project, including who will complete each task.


---

### Constraints


---

### Gaps

