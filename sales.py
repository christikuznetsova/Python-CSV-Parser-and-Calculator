from csv_data import CSVData

class SaleElement(object):
    def __init__(self, csv_row):
        self.sale_id = int(csv_row[0])
        self.product_id = int(csv_row[1])
        self.team_id= int(csv_row[2])
        self.qty= int(csv_row[3])
        self.discount= float(csv_row[4])

    def __repr__(self):
        return "Sale:" + str(self.sale_id)

class Sales(CSVData):
    element_class = SaleElement
