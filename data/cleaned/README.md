Used OpenRefine for the Data Cleaning Process
1. On 'Zip' column -> Facet -> Text Facet. Removed data entries that are located outside of Illinois (10014, 46319, 46322, 46494, 46410, 53061, 54971, 80439, 90067, and 91706). Removed by selecting an invalid zip code on Facet, All -> Edit rows -> Remove matching rows.
2. On 'Results' column -> Facet -> Text Facet. Removed data entries recorded as 'Out of Business', 'No Entry', 'Not Ready', and 'Business Not Located.'
3. On 'License #' column -> Facet -> Text Facet. Some data entries recorded the facility's license number as '0', which is not ideal. Therefore, we removed it from our dataset. Select '0' on Facet, All -> Edit rows -> Remove matching rows. Then, we transformed the data type of 'License #' to a number: Edit cells -> Common transforms -> To number. We found four entries with no data, which were also removed: select (blank) -> All -> Edit rows -> Remove matching rows.
4. On 'Facility Type' column, we cleaned the entries in multiple steps. First, we capitalized all our entries to reduce duplication: Edit cells -> Common transforms -> To uppercase. Using a cluster, we edited the columns representing the same category.
    * Key Collision + Fingerprint method: GROCERY/GAS STATION vs. GROCERY(GAS STATION) and CHILDREN'S SERVICES FACILITY vs. CHILDRENS SERVICES FACILITY.
    * Key Collision + n-Gram Fingerprint method: GAS STATION/STORE vs. GAS STATION STORE, ROOFTOPS vs. ROOF TOPS, 1023-CHILDREN'S SERVICES FACILITY vs. 1023 CHILDREN'S SERVICES FACILITY, ROOFTOP vs. ROOF TOP, and GROCERY & RESTAURANT vs. GROCERY/RESTAURANT.
    * Key Collision + Metaphone3 method: CHILDREN'S SERVICES FACILITY vs. 1023 CHILDERN'S SERVICES FACILITY vs. 1023-CHILDREN'S SERVICES FACILITY, THEATER vs. THEATRE, LIQUOR vs. 1475 LIQUOR, COMMISSARY vs. COMMISARY, GAS STATION/FOOD vs. GAS STATION FOOD STORE, MOBILE FOOD PREPARER vs. MOBIL FOOD PREPARED, and LIVE POULTRY SLAUGHTER vs. LIVE POULTRY SLAUGHTER FACILITY.
    * Key Collision + Cologne phonetic method: HERBALIFE vs. HERBAL LIFE.
    * Nearest Neighbor + Levenshtein r = 1.0, Bchars = 6: BANQUET vs. BANQUETS and ROOFTOPS vs. ROOFTOP.
    * Nearest Neighbor + Levenshtein r = 2.0, Bchars = 6: CONVENIENCE STORE vs. CONVENIENT STORE.
    * Nearest Neighbor + Levenshtein r = 3.0, Bchars = 6: CANDY SHOP vs. CANDY STORE and DOLLAR STORE vs. DOLLAR TREE.
    * Nearest Neighbor + PPM r = 1.0, Bchars = 6: LIVE POULTRY SLAUGHTER vs. POULTRY SLAUGHTER
Finally, we remove null entries on 'Facility Type' by selecting '(blank)' on the Facet, All -> Edit rows -> Remove matching rows.
