import csv

class ReportsController(object):
    def __init__(self, team_map, product_master, sales):
        self.team_map = team_map.data
        self.product_master = product_master.data
        self.sales = sales.data

    def output_team_report(self, output_path):
        self.calculate_team_report()

        fields = ['Team', 'GrossRevenue']

        self.output_file(output_path, self.team_report, fields)

    def output_product_report(self, output_path):
        self.calculate_product_report()

        fields = ['Name', 'GrossRevenue', 'TotalUnits', 'DiscountCost']

        self.output_file(output_path, self.product_report, fields)

    def calculate_team_report(self):
        self.team_report = []

        for team_id, team_name in self.team_map.items():
            team_gross_rev = self.calculate_gross_rev_for_team(team_id)
            self.team_report.append([team_name, team_gross_rev])

        #sort by GrossRevenue
        self.team_report.sort(key=lambda x: x[1], reverse=True)

    def calculate_product_report(self):
        self.product_report = []

        for product in self.product_master:
            gross_rev, total_units, discount_cost = self.calculate_product_report_for_given_product(product)
            self.product_report.append([product.product_name, gross_rev, total_units, discount_cost])

        #sort by GrossRevenue
        self.product_report.sort(key=lambda x: x[1], reverse=True)

    def calculate_gross_rev_for_team(self, team_id):
        gross_rev = 0

        #for "each" sale in "new array"  [" where we select" sale for "each" sale in self.sales if sale.team_id == team_id]:
        for sale in [sale for sale in self.sales if sale.team_id == team_id]:

            product_matches = [product for product in self.product_master if product.product_id == sale.product_id]

            if len(product_matches) > 0:
                product = product_matches[0]
            else:
                #product is not found
                continue

            gross_rev += sale.qty * product.product_price * product.product_lot_size

        return format(gross_rev, '.2f')

    def calculate_product_report_for_given_product(self, product):
        gross_rev = 0
        total_units = 0
        discount_cost = 0

        for sale in [sale for sale in self.sales if sale.product_id == product.product_id]:

            gross_rev += sale.qty * product.product_price * product.product_lot_size
            total_units += sale.qty * product.product_lot_size
            discount_cost += sale.qty * product.product_price * product.product_lot_size * sale.discount * 0.01

        return  '{:g}'.format(gross_rev), total_units, '{:g}'.format(discount_cost)

    def output_file(self, output_path, data_report, fields):
        with open(output_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(fields)
            for each in data_report:
                writer.writerow(each)
