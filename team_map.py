import csv

class TeamMap(object):
    def __init__(self, file):
        raw_csv = csv.reader(file)

        self.data = {}

        for index, row in enumerate(raw_csv):
            if index == 0:
                #skip the first row representing file header
                continue

            team_id = int(row[0])
            team_name = row[1]

            self.data[team_id] = team_name

        print(self.data)
