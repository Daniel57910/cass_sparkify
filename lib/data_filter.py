
class DataFilter:

	def __init__(self, panda_dataframe):
		self.panda_dataframe = panda_dataframe

	#rather than unique dataframe ensure that column is not null
	def return_subset_not_null(self, columns, cluster_columns=None):
		
		if not cluster_columns: 
			return self.panda_dataframe[columns]

		return self.panda_dataframe[columns].dropna(subset=cluster_columns)

