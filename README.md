# Are Chicagoans Secret Food Safety Inspectors? Analyzing Chicago's Food Inspection and 311-reported Sanitary Complaints Data


## Contributors
<h3>Sean Yoon</h3>
    <ul>
        <li>Managed GitHub repository</li>
        <li>Integrated and cleaned datasets</li>
        <li>Created Snakefile for workflow management</li>
        <li>Wrote data analysis and visualization scripts</li>
    </ul>
<h3>Nathan Diaz</h3>
    <ul>
        <li>Written portion of Data Quality</li>
        <li>Wrote the analysis part of Findings</li>
        <li>Wrote Future Work</li>
        <li>Conductued References</li>
    </ul>
        

## Summary
What comes to your mind when you think about Chicago? Skyscraper? Jazz and blues music? The musical? These are all great representations of Chicago. Yet, Chicago has a strong culinary identity; it is renowned for having exceptional and diverse restaurants, even has a dish named after its city: Chicago-style pizza. While serving delicious food is crucial to becoming a city of appetite, sanitation around food places is as important. The City of Chicago's Department of Public Health conducts the city's food inspections to make sure food served on the table is not only delicious but safe. The sanitation of the whole city is in charge by the 311 non-emergency system, where they receive hundreds of reports weekly. 

Using the datasets publicly available from the two departments, we aim to explore on the correlation between the food inspection results and sanitation complaints across Chicago's neighborhood. This project will answer questions such as: Are Chicago neighborhoods with higher counts of 311 sanitation complaints also more likely to have restaurants that received a fail for city food inspections? Are neighborhoods with higher sanitary complaint volume also more likely to have higher inspection failure rates over the study period? Are there specific facilities that are more sensitive to external sanitation compared to others? Is there specific neighborhood(s) that appear to be more sensitive toexternal sanitation compared to others?

As expected in our hypothesis that food places that receive failure or conditional tend to have a higher rate of sanitation reports, our analysis found a moderate correlation between food inspection results and 311 sanitation complaints across Chicago's neighborhoods. Furthermore, we discovered that certain facility types, grocery stores, restaurants and schools, tend to have a slightly higher fail rate when there is an increase in sanitation complaints. This suggests that some specific types of food establishments may be more sensitive to external sanitation conditions of the facility. Further research could explore the underlying factors contributing to this sensitivity and whether targeted interventions could improve food safety outcomes in these establishments.


## Data Profile
**Disclaimer**: This directory provides applications using data that has been modified for use from its original source, www.cityofchicago.org, the official website of the City of Chicago.  The City of Chicago makes no claims as to the content, accuracy, timeliness, or completeness of any of the data provided at this site.  The data provided at this site is subject to change at any time.  It is understood that the data provided at this site is being used at one’s own risk.

* Primary Dataset: Food Inspection
    * URL: https://data.cityofchicago.org/Health-Human-Services/Food-Inspections/4ijn-s7e5/about_data
    * Source: Chicago Data Portal - City of Chicago
    * Format: CSV
    * Temporal Range: January 1st, 2018 to October 6th, 2025
    * Update Frequency: Updated daily
    * Number of Rows: 135,112
    * Columns: Inspection ID, DBA (Doing Business As) Name, AKA (Also Known As) Name, License #, Facility Type, Risk, Address, City, State, Zip, Inspection Date, Inspection Type, Results, Violations, Latitude, Longitude, Location

* Secondary Dataset: 311 Service Requests
    * URL: https://data.cityofchicago.org/Service-Requests/311-Service-Requests/v6vf-nfxy/about_data
    * Source: Chicago Data Portal - City of Chicago
    * Format: CSV
    * Temporal Range: December 18th, 2018 to October 6th, 2025, 12:00 PM CST
    * Update Frequency: Updated multiple times per day
    * Number of Rows: 946,664
    * Columns: SR_Number, SR_Type, SR_Short_Code, Created_Department, Owner_Department, Status, Origin, Created Date, Last Modified Date, Closed Date, Street Address, City, State, Zip_Code, Street_Number, Street_Direction, Street_Name, Street_Type, Duplicate, Legacy_Record, Legacy_SR_Number, Parent_SR_Number, Community_Area, Ward, Electrical_District, Electricity_Grid, Police_Sector, Police_District, Police_Beat, Precinct, Sanitation_Division_Days, Created_Hour, Created_Day_Of_Week, Created_Month, X_Coordinate, Y_Coordinate, Latitude, Longitude, Location

Due to the insufficient computational performance available, our research team decided to import subsets of the original data from the Chicago Data Portal using the built-in query tool available on its website. 

During the import, we eliminated data beyond the time scope to ensure timeliness of data and consistency of the results. The primary dataset included records since 2010, which may include out-of-date information. Thus, we limited the temporal range to January 1st, 2018 to October 6th, 2025. The secondary dataset included records since 18th of December 2018, which affected the temporal consistency when merging with the primary dataset. Both datasets updated daily, so we set the end date to October 6th, 2025, the date when we accessed the data.

The secondary data set contained various types of service requests, but we only focused on sanitary-related complaints to align with our research question. We filtered the dataset to include only records where the "SR_Type" column contained "Sanitary Condition" or similar keywords. This ensured that we were analyzing relevant data that could potentially impact food inspection results.


## Data Quality
The data was collected using the standardized procedure by the Chicago Department of Public Health’s (CDPH) Food Protection Program staff. While the author clearly states the descriptions of data elements in a separate PDF document, no technical terms or detailed data collection methods are mentioned in the documentation. Regarding data quality issues and limitations, the admin warns of potential duplicate inspection records, which may require an appropriate precaution in data analysis. We spot some inconsistencies in the update frequency – metadata states the dataset is updated daily, while the PDF document for descriptions of the data elements states that the datasets are updated every Friday.

For our documentation we were also using Food Inspections data so we were also able identify the same key problems from the previous problem. But As for our other dataset we had used the 311 service request which is also found on Chicago Data Portal. They explain their data collection by putting calls and service requests into the dataset and updating regularly. The features are relatively understandable as some describe the location of where the 311 service request would like to be at but there are also other unique features such as “CREATED_DEPARTMENT” where it defines which department created the service request.“OWNER_DEPARTMENT” where it describes “the department with initial responsibility for the service request.” 

However, data collection still lacks full transparency: the documentation does not thoroughly describe how requests are triaged, whether certain request types are prioritized, or how duplicates are merged. There are also notable data quality issues including missing values in address, ZIP code, created_department, and owner_department. These missing fields may reflect privacy redactions, citizen reporting errors, or back-end workflow gaps, but the documentation does not clarify this.
Both datasets clearly list update frequency—Food Inspections updates automatically and 311 updates daily—but they do not describe data latency, archival processes, or whether older records are revised after publication. Overall, while both datasets provide surface-level metadata, they lack deeper explanations needed for fully transparent, reproducible analysis.

* Below is a list of possible errors and features that impacts the quality of both datsets:
    * Missingness Patterns Not Explained: Although both datasets contain missing values, neither source explains why certain fields are missing or how missingness occurs.
    * Lack of Versioning or Revision History: Chicago Data Portal does not show what data changed over time, only that the dataset was updated.
    * Potential Data Entry / Human Error: portions of each dataset rely on manual entry by inspectors or call center staff, typographical errors, inconsistent formatting, or ambiguous text fields can occur. These inconsistencies may lead to misclassification or reduced accuracy when parsing categorical variables or free-text commentary.
    * Inconsistent Use of Categorical Labels:Some categorical fields lack strict controlled vocabularies. For example, similar categories may appear under slightly different names across years, and the documentation does not provide a definitive enumeration of all possible values. These inconsistencies reduce interoperability and complicate aggregation across time.
    * Lack of Metadata About Data Validation Processes: There is no description of internal data validation, auditing procedures, or error-checking rules. Without clarity on how invalid records, incomplete entries, or duplicates are detected and corrected, data consumers must assume potential unreported errors remain in the dataset.
    * Temporal Accuracy and Event Timing Issues: Timestamps in both datasets lack detailed temporal metadata such as time zone, method of capture, and whether times are system-generated or manually recorded. In 311 data, resolution times may be missing or inconsistently logged, making it difficult to compute accurate service response intervals.


## Findings
### 1. Overall Correlation Analysis

We calculated the Pearson correlation coefficient between the average number of 311 sanitary complaints and the food inspection fail rates across different ZIP codes in Chicago. The `correlation` coefficient was `0.5462`, indicating a moderate positive correlation. The `p-value` was `1.4886e-08`, suggesting that the correlation is statistically significant. However, the moderate strength of the correlation indicates that other factors may also be influencing food inspection outcomes.

![Alt text](results/plots/fail_rate_vs_sr_count_scatter_labeled.png)


### 2. Facility Type Sensitivity
We analyzed the sensitivity of different facility types to 311 sanitary complaints. Restaurants and schools showed a higher sensitivity, with fail rates increasing more significantly with the number of complaints. This suggests that these facility types may be more affected by external sanitation conditions.

![Alt text](results/plots/facility_type_fail_vs_sr_comparison.png)


### 3. Sensitive ZIP Codes
We identified specific ZIP codes that exhibited a significant increase in food inspection fail rates with an increase in 311 sanitary complaints. These ZIP codes may require targeted interventions to improve sanitation and food safety.

![Alt text](results/plots/sensitive_zips_highlighted.png)


### 4. Top ZIP Codes by Average Sanitary Complaints
We identified the top 15 ZIP codes with the highest average number of 311 sanitary complaints. These areas may benefit from increased sanitation efforts to potentially improve food inspection outcomes.

![Alt text](results/plots/zip_rank_by_sr_count_top15.png)


### 5. Facility Type Fail Rates
We calculated the fail rates for different facility types. Restaurants had the highest fail rate, followed by schools and grocery stores. This information can help prioritize inspection efforts.

![Alt text](results/plots/facility_fail_rate_top.png)

Through each of our graphs we can conclude the 311 sanitary rates for each type of facility that was complained on along with the location of where the most complaints are with the help of zip codes. With this we wer able to align the zip codes of both datasets that had the most 311 sanitary complaints along with the Facilaty type fail rates. Through Figure 3 we were able to identify the top 75th percentile of zip codes that had a high fail rate and sanitary complaints. With the help of google maps and Chicago Public Schools locator we were able to identify the types of neighborhoods and the conditions. For example 60628 is the neighborhood Roseland, in the south side of Chicago. And if we continue finding the neighborhoods and where they are located in Chicago, we are seeing a correlation. For example:
* 60628- Roseland (South Side)*
* 60620 - Beverly View (South Side)
* 60629 - West Law (South West Side)
* 60617 - South Chicago (South Side)*
* 60619 - East Chatham (South Side)
* 60623 - Cicero/ Little Village (South Side)
* 60639 - Northwest (Northwest side)
* 60647 - Logan Square (North side)
* 60636 - Englewood (South Side)*
* 60651 - West Humboldt Park (West Side)*
* 60624 - West Garfield Park (West Side)*
* 60644 - Austin (West Side)*
* 60625 - Ravenswood (North side)

Now there is a common trend on how there are more violations and more 311 sanitation complaints in the south side of Chicago. With the City of Chicago pdf file of their “Chi BIZ Strong Grant Program” where it helps focus Chicago business and community area, shows the community areas with at least 65%  low or moderate income residents. 6 out of the 13 neighborhoods are on the list which are marked with a star. Now we assume that there may be a correlation between high failure rates and high sanitation complaints with low/ moderate income neighborhoods. But we would like to remind you that correlation does cause causation.


## Future Work
About potential future work, we consider the followings:

A natural extension of the current project is to explore how the relationship between 311 sanitary complaints and food inspection outcomes evolves over time. Since both datasets span many years and are updated regularly, they are well-suited for investigating trends, seasonality, and changes in reporting behavior or inspection strategy.
Future work could begin by constructing a time-series pipeline that aggregates sanitary complaints and inspection results by meaningful intervals—such as week, month, quarter, or year. This would allow for several forms of temporal exploration:

### Trend Analysis
Analysts could examine whether increases in sanitary-related 311 complaints reliably precede spikes in inspection failures. If a lagged correlation exists, this might suggest that 311 requests could serve as an early-warning system for identifying potential high-risk establishments.
Seasonality and Event Impacts
Chicago’s seasonal conditions (e.g., humid summers, freezing winters) may influence food safety outcomes or citizen complaint behavior. A temporal decomposition could reveal:
* seasonal peaks in certain types of violations
* yearly cycles in complaint volume
* changes connected to specific public health campaigns or new policies
### Geospatial Analysis

A second major direction for future work is to leverage the geographic richness of both datasets to perform a full geospatial analysis of sanitary complaints and inspection results across Chicago. Because each record contains location information (addresses, ZIP codes, census tracts, or coordinates), spatial patterns could be visualized and analyzed to uncover geographic disparities or localized risk factors.
Mapping and Visualization
Using geospatial libraries such as geopandas, folium, or mapping tools like Kepler.gl, future work could:
* Map sanitary complaints across the city
* Overlay inspection results to compare complaint hotspots with high-failure areas
* Visualize spatial clustering of Risk 1 (High) establishments


These visualizations would help identify neighborhoods where sanitary concerns frequently arise but are not necessarily matched with inspection failures, suggesting possible gaps in resource deployment or reporting accuracy.
Another important direction for future work involves addressing the computational challenges posed by the size and complexity of the datasets used in this project. Both the 311 Service Requests and Food Inspections datasets are updated daily and contain records stretching back many years, which means they effectively operate as append-only historical archives. The 311 dataset alone exceeds 13 million individual entries, and the Food Inspections dataset continues to grow as the city logs every inspection, reinspection, and violation. Working with data at this scale introduces significant performance constraints, particularly when conducting repeated filtering, merging, temporal aggregation, or spatial operations.

During our analysis, we relied primarily on our computers, which limited the kinds of advanced workflows we could run efficiently. Larger-scale tasks—such as training predictive models using full historical data, calculating spatial autocorrelation metrics, or running multi-year rolling windows for temporal forecasting—would require more memory, faster processing speeds, and potentially cloud-based infrastructure. As the datasets continue to grow, even simple operations like geocoding addresses, computing proximity relationships, or dynamically clustering millions of points become computationally expensive.

A stronger computing environment would therefore enable a much more ambitious analytical pipeline. With increased computational capacity, we could run full geospatial analyses that incorporate every historical record, rather than relying on sampled subsets. This would allow for more accurate spatial hotspot detection, neighborhood-level mapping, and integration with external geographic datasets such as census boundaries or zoning maps. Similarly, stronger hardware would allow us to perform multi-year temporal modeling using the complete dataset rather than simplified or aggregated versions.


## Reproducing
1. Overall Correlation Analysis

2. Facility Type Sensitivity

3. Sensitive ZIP Codes

4. Top ZIP Codes by Average Sanitary Complaints

5. Facility Type Fail Rates


## References
* City of Chicago. (n.d.). 311 service requests. Chicago Data Portal. https://data.cityofchicago.org/Service-Requests/311-Service-Requests/v6vf-nfxy/about_data

* City of Chicago. (n.d.). Food inspections. Chicago Data Portal. https://data.cityofchicago.org/Health-Human-Services/Food-Inspections/4ijn-s7e5/about_data

* Chicago Public Schools. (n.d.). CPS school locator. https://schoolinfo.cps.edu/schoollocator/index.html

* Chicago Department of Public Health. (n.d.). Food inspections data dictionary. Chicago Data Portal. https://data.cityofchicago.org/api/assets/BAD5301B-681A-4202-9D25-51B2CAE672FF

* Chicago Department of Innovation & Technology. (n.d.). 311 service request data dictionary. Chicago Data Portal. https://data.cityofchicago.org/api/assets/BAD5301B-681A-4202-9D25-51B2CAE672FF

* City of Chicago. (n.d.). Chi Biz Strong Grant Program: Community areas with at least 65% low or moderate income residents [Internal draft for policy deliberation; PDF].

* McKinney, W. (2010). Data structures for statistical computing in Python. In Proceedings of the 9th Python in Science Conference (pp. 51–56). https://pandas.pydata.org/(The pandas Development Team). (2024). pandas [Computer software]. https://pandas.pydata.org/

* Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. Computing in Science & Engineering, 9(3), 90–95. https://matplotlib.org/

* Waskom, M. L. (2021). Seaborn: Statistical data visualization. Journal of Open Source Software, 6(60), 3021. https://seaborn.pydata.org/

* Virtanen, P., Gommers, R., Oliphant, T. E., Haberland, M., Reddy, T., Cournapeau, D., … van Mulbregt, P. (2020). SciPy 1.0: Fundamental algorithms for scientific computing in Python. Nature Methods, 17(3), 261–272. https://scipy.org/

* Harris, C. R., Millman, K. J., van der Walt, S. J., Gommers, R., Virtanen, P., Cournapeau, D., … Oliphant, T. E. (2020). Array programming with NumPy. Nature, 585, 357–362. https://numpy.org/

* Python Software Foundation. (2024). pathlib (Version 3.x) [Standard library module]. https://docs.python.org/3/library/pathlib.html


