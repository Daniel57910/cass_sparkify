from cassandra.cluster import Cluster
from cassandra import AlreadyExists
from sys import exit

class DatabaseWrapper:

	def __init__(self):	
		self.cluster = Cluster(['127.0.0.1'])

	def create_keyspace(self, core_keyspace, config):
  
		try:
			session = self.cluster.connect()
			session.execute(
				core_keyspace + config
			)
		except AlreadyExists:
			pass
		except Exception as e:
			print('Unable to execute keyspace')
			print(e)
			exit(1)

	def execute_query(self, query):
		try:
			session = self.cluster.connect()
			result = session.execute(query)
			self.close_db_connection()
			return result
		except Exception as e:
			print('Unable to execute query\n.{}'.format(e))
			exit(1)
		
	def close_db_connection(self):
		try:
			self.cluster.shutdown()
		except Exception as e:
			print('Unable to close connection to DB\n.{}'.format(e))
			exit(1)
