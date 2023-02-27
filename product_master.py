from csv_data import CSVData

class ProductMasterElement(object):
    def __init__(self, csv_row):
        self.product_id = int(csv_row[0])
        self.product_name = csv_row[1]
        self.product_price= float(csv_row[2])
        self.product_lot_size = int(csv_row[3])

    def __repr__(self):
        return "Product:" + self.product_name

class ProductMaster(CSVData):
    element_class = ProductMasterElement