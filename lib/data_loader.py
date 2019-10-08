import pandas as pd
import csv

class DataLoader:

	def __init__(self, matched_files):
		self.matched_files = matched_files
		self.aggregate_file_data = []

	def create_dataframe_from_files(self):

		for file in self.matched_files:
			self.aggregate_file_data.extend(fetch_csv_data(file))

		return pd.DataFrame.from_records(self.aggregate_file_data)

def fetch_csv_data(filename):
	
	with open(filename, newline='') as event_data_file:
		try:
			return [line for line in csv.DictReader(event_data_file)]
		except Exception as e:
			print('Unable to return filename = {}'.format(event_data_file))
			print(e)





