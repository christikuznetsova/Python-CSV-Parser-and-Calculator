import csv

class CSVData(object):
    def __init__(self, file):
        raw_csv = csv.reader(file)

        self.data = []

        for row in raw_csv:
            self.data.append(self.element_class(row))
