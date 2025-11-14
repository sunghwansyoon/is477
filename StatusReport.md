# Status Report

### Datasets

#### Datasets in Planning Stage:
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


#### Datasets in Storage and Organization Stage:
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

---

### Ethics
  
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
    --> Update on Data Integration: We used Pandas python library to join the primary and secondary datasets because it was able to check the implementation step by step, providing more insights during the integration process.

    Data Integration Process:
    1. Before joining, we aggregated the 311 Service Requests (or 311 in short) dataset at the ZIP-code level. We grouped all 311 sanitary related service requests by 'ZIP_CODE' and counted the number of unique 311 records per 'ZIP_CODE.' Then, we added a column 'sr_count,' the number of 311 sanitary requests recorded in a specific ZIP area.
    2. We changed the data type of ZIP code to string for both datasets to match data type to join two datasets. Rows with missing ZIP codes were removed since they can not be matched by the join key.
    3. Performed left join on Food Inspections dataset with 311 sanitary (aggregated) dataset, which preserved every food inspection records and added new 'sr_count' column to each row. With ZIP code not matching 311 records, sr_count is filled with '0'.
    4. Joining allowed us to analyze following research questions: "Do ZIP codes with more sanitation complaints have more failed inspections?", "Is there a relationship between public complaint behavior and inspection outcomes?", and "Which neighborhoods show the highest sanitation burden relative to restaurant safety performance?"
    5. The output (integrated) dataset is located at 'data/integrated/food_inspections_with_311_by_zip.csv'.
  
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

  *Beginning of our rough draft report*

**Source**: “Food Inspections” on the Chicago Data Portal
**URL**: https://data.cityofchicago.org/Health-Human-Services/Food-Inspections/4ijn-s7e5/about_data
**Summary description**:
This dataset contains inspection records of restaurants and other food establishments in the City of Chicago, collected by the Chicago Department of Public Health’s Food Protection Program. Inspections are performed using a standardized procedure, in which an inspector records findings, the facility’s risk category, violations (if any), and the result (e.g., pass / pass with conditions / fail).
Temporal / Spatial Scope:

Covers inspections from January 1, 2010 to the present (or at least up to the last modified date) according to the Data.gov catalogue.
The City of Chicago is the spatial domain (establishments within Chicago).

Data accuracy and duplication: The publisher explicitly states: “Attempts have been made to minimise any and all duplicate inspection reports. However, the dataset may still contain such duplicates and the appropriate precautions should be exercised when viewing or analyzing these data.”

Temporal comparability caution: Because the inspection procedure changed on July 1 2018, comparisons across that date may reflect procedural changes rather than true underlying changes. You must flag this when analyzing trends.

Geolocation / privacy: The dataset includes latitude and longitude coordinates of establishments. Although these are business locations (not private persons), you should still consider whether any subset of data might indirectly identify individuals (e.g., proprietor’s home address if mobile vendor). If you join with other data that contain personal information, you must ensure compliance with privacy standards.

Interpretation caution: Inspection results reflect a snapshot in time, and as the publisher notes, “the result of the inspections … may not reflect findings noted at other times.” data.wu.ac.at+1 So any inference must explicitly note that these are point-in-time inspection outcomes, not necessarily complete representations of food safety history.

Bias and representativeness: The dataset is for Chicago only; establishments that are unlicensed or informal may not be represented. Also, inspections may be triggered by complaints or follow-ups, so there may be selection bias — this matters especially if you're using the data for predictive modelling or risk analysis.

Summary:
In summary, the Chicago Food Inspections dataset is a rich, open repository of regulatory inspection records that can be leveraged for compliance monitoring, risk modelling, spatial analysis and time-trend evaluation. However, users must account for procedural changes (post-July 2018), potential duplicates, snapshot nature of results, and ensure responsible handling of geolocation data and business identities. Attribution to the City of Chicago is appropriate, and checking for any specific usage terms is prudent.

**311 Service Requests**
**Source**: “311 Service Requests” on the Chicago Data Portal
**URL**: https://data.cityofchicago.org/Service-Requests/311-Service-Requests/v6vf-nfxy/about_data
Summary description:
This dataset captures non-emergency service requests made by residents, callers, or staff via the City’s 311 system (City of Chicago) for issues such as potholes, graffiti removal, abandoned vehicles, sanitation complaints, and more. The dataset includes requests created after the launch of the “new 311 system” on December 18, 2018, along with some records from the previous system (as indicated by the “LEGACY_RECORD” field).
Temporal / Spatial Scope:

Start date: December 18, 2018 (new system), plus some legacy records from before that date.

Continuously updated (metadata shows last modified November 8, 2025) according to the catalogue. 

Spatial domain: City of Chicago service areas (requests include address information).

Because it is a live system, dataset may update daily or near-real-time.

* Potential Uses / Strengths:

 * Allows spatial and temporal analysis of public service demand (which neighborhoods have higher volumes of particular request types)

 * Can be used as a proxy for “neighborhood issues” or “urban condition” (e.g., graffiti, sanitation, abandoned vehicles)

 * Could be combined with other data (crime, demographic, infrastructure) to support service-allocation modelling, predictive analytics, or equity analysis. Indeed, academic work has used 311 data in such fashion. arXiv+1


* Key Ethical / Legal Constraints:


The dataset is publicly accessible; but as with the food inspections data the license field states “License: No license information was provided.”


Users must attribute the City of Chicago as the publisher and check for any terms of service on the portal.


Bias and representativeness: A major caution: the propensity for residents to place 311 requests is not uniform across populations or neighborhoods. Research shows significant socio-spatial variation in complaint rates (i.e., some locations may under-report). arXiv+1 If you use the data for modelling or inference, you need to explicitly account for differential reporting biases (e.g., higher-income neighborhoods might complain more than lower-income ones).


Geolocation and privacy: The dataset includes location information of incident reports, which may relate to private property or identify patterns in specific buildings. If you join with other datasets (e.g., demographic data or business data) you must check for indirect identification risks.


Temporal system change: Because the dataset switched to a new system on December 18, 2018, and legacy records exist, you must ensure proper handling of pre- and post-system change. Comparisons across the transition may be confounded by system architecture rather than actual service request changes. Chicago


Interpretation caution: A service request does not always imply a confirmed issue or fault of the city; some are “information only”, or may be incorrectly located/addressed. The catalogue notes: “For purposes of all columns indicating geographic areas or locations, please note that requests of the type 311 INFORMATION ONLY CALL often are entered with the address of the City's 311 Center.” Data.gov


Equity implications: If you use the data to compare neighborhoods, you must be mindful of structural biases in who reports issues. Using the data without this lens may inadvertently reinforce inequities or misinterpret neighborhood conditions.


Summary:
The 311 Service Requests dataset offers a comprehensive and up-to-date record of citizen-reported service issues within Chicago, enabling analyses of spatial demand for city services, temporal patterns, and linkages to infrastructure or neighbourhood characteristics. However, users should be cautious about using it as a pure measure of “need” or “service deficiency” without adjusting for reporting bias, system-change effects, or the fact that a request does not necessarily result in verification. Proper attribution and privacy-aware handling of location data is required.

Joint considerations & recommendations
When using these two datasets together (which I assume you intend, given your data-driven skill set and interest in integrative analysis), here are some key points:


Linking datasets: Because the Food Inspections dataset includes geolocation (lat/long) and address, and the 311 dataset includes service request location, you may be able to join or spatially overlay to explore hypotheses (for example: are food establishments in areas with higher volumes of sanitation or rodent-related 311 calls more likely to fail inspections?). This kind of integrative analysis is quite powerful but also demands caution around spatial scale, potential confounders, and temporal alignment.


Time alignment: Ensure that you align the time frames suitably — e.g., the 311 requests dataset starts post-Dec 18 2018 new system, whereas the inspections dataset covers back to 2010. If you pull a subset of inspections post-2018 you may avoid some temporal bias. Also ensure that you consider any inspection procedure changes (July 1 2018) and system change in 311 (Dec 2018) in your analysis.


Geographical granularity: When merging or associating spatially, you might choose to aggregate to census-tract, ZIP code, or neighbourhood level if assembly of individual lat/long is too fine or risks re-identification. Also check for missing or malformed coordinates/addresses.


Bias and causality: Be transparent in your analysis about limitations — e.g., higher 311 call volumes might reflect more engaged residents rather than worse underlying conditions; similarly, past inspection outcomes may influence both the business behaviour and the neighbourhood environment. Avoid implying causal relationships unless carefully tested.


Ethical use of location data: Because both datasets involve physical addresses or coordinates, you should ensure that you do not inadvertently expose private individual data or use addresses in a way that could identify individuals (especially for mobile vendors, small business owner home-addresses, or when joined with owner names). You should treat business address data responsibly and, if disseminating results, consider aggregating or anonymising as needed.


Attribution and licensing: While the datasets are public, and their metadata states “No license information was provided,” good practice is to attribute the City of Chicago as provider and include a note in your documentation that you used the City’s open-data portal. If you plan to publish findings, check the portal’s “Terms of Use” page to be safe.


Document limitations: In your data-profile write-up (which you asked for) and in any downstream work, explicitly document known limitations: e.g., potential duplicates in the inspection data, procedural changes in mid-2018, reporting/selection bias in 311 data, incomplete coverage (only included if reported/inspected), and that inspection results represent the state at one point in time only.



If you like, I can extract the full column dictionaries (field names, types, definitions) for both datasets (so you have a full schema list) and provide them in a ready-to-use format (CSV or Markdown) for your data-pipeline work. Would you like me to do that?

