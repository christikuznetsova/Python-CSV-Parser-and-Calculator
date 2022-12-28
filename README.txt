The Sales Report Generator
Created December 8, 2022
Last Updated December 13, 2022

This is a folder containing an application that uses a Python program to read three input files containing team, product, and sales information to perform calculations and produce two output files containing the gross revenue per team and per product. 

The input files are TeamMap.csv, ProductMaster.csv, and Sales.csv. Where, 
--TeamMap.csv contains the team ID and the corresponding team name with headers in the first row of the file; 
--ProductMaster.csv contains the product information with each row containing the product ID, the product name, the product price per unit of the product sold, and the number of units sold in one lot; 
--and, Sales.csv contains individual sales with each row containing the sale ID, the product ID, the team ID, the number of lots sold, and the discount applied in percent. 

The output files are TeamReport.csv and ProductReport.csv, where TeamReport.csv contains the gross revenue per team, and the ProductReport.csv contains the gross revenue per product, total units sold per product, and the discount cost per product. The information in the output files is arranged in columns with the first row containing the column headers

Pre-requisites. Python 3 is required to use this project. The minimum version of Python 3 is 3.5, and the recommended version is 3.8. If you are using a version lower than 3.5, please upgrade your Python installation before proceeding.

To run the application, follow the steps below.

1. Ensure the pre-requisites listed above are met.
2. Un-Zip the folder by extracting the files into a single location.
3. Use the TeamMap.csv, ProductMaster.csv, and Sales.csv example files and the file descriptions above to populate data into the appropriate columns of the TeamMap.csv, ProductMaster.csv, and Sales.csv files. Save and close the files.
4. Open a Python editor or a command-line interface in the same location as the extracted files. 
5. Copy and paste the following line of code: python report.py -t TeamMap.csv -p ProductMaster.csv -s Sales.csv --team-report=TeamReport.csv --product-report=ProductReport.csv

The steps above will generate the two output files, TeamReport.csv and ProductReport.csv in the same location. Use the file descriptions above to interpret the output files.

For any question, contact christi.kuznetsova@gmail.com.

