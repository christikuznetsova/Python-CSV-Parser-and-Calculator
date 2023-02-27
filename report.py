import argparse
from team_map import TeamMap
from product_master import ProductMaster
from sales import Sales
from reports_controller import ReportsController

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

team_map_file = open(args.team_map)
team_map = TeamMap(team_map_file)

product_master_file = open(args.product_master)
product_master = ProductMaster(product_master_file)

sales_file = open(args.sales)
sales = Sales(sales_file)

reports_controller = ReportsController(team_map, product_master, sales)
reports_controller.output_team_report(args.team_report)
reports_controller.output_product_report(args.product_report)
