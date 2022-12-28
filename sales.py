#  SaleId – an integer uniquely identifying the sale
#  ProductId – an integer identifying the Product (matches the ProductId from the Product Master)
#  TeamId – an integer identifying the Sales Team (matches the TeamId from the Team Map)
#  Quantity – an integer representing how many lots of the product were sold
#  Discount – a floating point discount percentage given on the sale (e.g. 2.5% discount as “2.50”)
#1,1,2,10,0.00


import csv

class Sales(object):
    def __init__(self, file):
        raw_csv = csv.reader(file)

        self.data = []

        for row in raw_csv:
            self.data.append(SaleElement(row))

        print(self.data)

#dictionary is too tacky for this, use below class instead
#create new file type (data structure)
class SaleElement(object):
    def __init__(self, row):
        self.sale_id = int(row[0])
        self.product_id = int(row[1])
        self.team_id= int(row[2])
        self.qty= int(row[3])
        self.discount= float(row[4])

    def __repr__(self):
        return "Sale:" + str(self.sale_id)
