import glob

class FileFinder():
	
	def __init__(self, start_directory, file_type):

		self.start_directory = start_directory
		self.file_type = file_type

	def return_file_names(self):

		return (glob.iglob(self.start_directory + "**/" + self.file_type, recursive=True))



