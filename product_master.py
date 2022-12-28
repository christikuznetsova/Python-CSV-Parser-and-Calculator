import csv

class ProductMaster(object):
    def __init__(self, file):
        raw_csv = csv.reader(file)

        self.data = []

        for row in raw_csv:
            self.data.append(ProductMasterElement(row))

        print(self.data)

#dictionary is too tacky for this, use below class instead
#create new file type (data structure)
class ProductMasterElement(object):
    def __init__(self, row):
        self.product_id = int(row[0])
        self.product_name = row[1]
        self.product_price= float(row[2])
        self.product_lot_size = int(row[3])

    def __repr__(self):
        return "Product:" + self.product_name
