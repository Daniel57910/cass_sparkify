from create_aggregate_csv import create_aggregate_csv
from database_handler import create_event_data_table, copy_event_datafile_into_db, execute_query
from model.query import drop_statements, read_statements
from lib.database_wrapper import DatabaseWrapper

def print_the_response(header, response):
  print('\nResult of {}:'.format(header))
  for row in response:
    print(row)

def main():

    core_keyspace = "CREATE KEYSPACE sparkifydb WITH REPLICATION = " 
    keyspace_config = "{ 'class': 'SimpleStrategy', 'replication_factor':  1 }"

    database_wrapper = DatabaseWrapper()
    database_wrapper.create_keyspace(core_keyspace, keyspace_config)

    header = ['song_play', 'user_and_session', 'user_and_song']
    
    for drop_table in drop_statements:
        execute_query(drop_table)

    create_event_data_table()
    create_aggregate_csv()
    copy_event_datafile_into_db()
    response = {}

    for head in header:
      response[head] = execute_query(read_statements[head])

    for header in response:
      print_the_response(header, response[header])

if __name__ == "__main__":
    main()
