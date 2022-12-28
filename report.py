import argparse
from team_map import TeamMap
from product_master import ProductMaster
from sales import Sales
from reports_controller import ReportsController
#python3 report.py -t TeamMap.csv -p ProductMaster.csv -s Sales.csv --team-report=TeamReport.csv --product-report=ProductReport.csv

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-t', '--team-map', required=True,
                    help='file containing team mapping')
parser.add_argument('-p', '--product-master', required=True,
                    help='file containing product master data')
parser.add_argument('-s', '--sales', required=True,
                    help='file containing sales data')
parser.add_argument('--team-report', required=True,
                    help='output file for team report')
parser.add_argument('--product-report', required=True,
                    help='output file for product report')
args = parser.parse_args()

# Read team mapping from file

team_map_file = open(args.team_map) #opens the file path to csv file that user input
team_map = TeamMap(team_map_file) #this is a dictionary created using the csv file entries

product_master_file = open(args.product_master)
product_master = ProductMaster(product_master_file)

sales_file = open(args.sales)
sales = Sales(sales_file)

reports_controller = ReportsController(team_map, product_master, sales)
reports_controller.output_team_report(args.team_report)
reports_controller.output_product_report(args.product_report)
