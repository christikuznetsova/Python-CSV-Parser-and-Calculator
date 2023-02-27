import csv

class TeamMap(object):
    def __init__(self, file):
        raw_csv = csv.reader(file)

        self.data = {}

        file_header = 0

        for index, row in enumerate(raw_csv):
            if index == file_header:
                continue

            team_id = int(row[0])
            team_name = row[1]

            self.data[team_id] = team_name
