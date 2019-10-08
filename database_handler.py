from lib.database_wrapper import DatabaseWrapper
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine.connection import setup
import model.table
import os
import subprocess

def create_event_data_table():
  try:
    setup(['127.0.0.1'], 'sparkifydb', retry_connect=True)
    sync_table(model.table.EventDataModel)
    sync_table(model.table.UserAndSessionModel)
    sync_table(model.table.UserAndSongModel)
  except Exception as e:
    print(e)
    exit(1)


def copy_event_datafile_into_db():
  try:
    process = subprocess.run(cqlsh_load_csv(), shell=True)
    process = subprocess.run(cqlsh_load_user(), shell=True)
    process = subprocess.run(cqlsh_load_user_song(), shell=True)
  except Exception as e:
    print(e)
    exit(1)

def cqlsh_load_csv():
	return ('cqlsh -e "COPY sparkifydb.event_data_model FROM ' +
	"'{}/event_datafile_new.csv' ".format(os.getcwd()) + 
	'WITH HEADER=TRUE"')

def cqlsh_load_user():
	return ('cqlsh -e "COPY sparkifydb.user_and_session_model FROM ' +
	"'{}/user_and_session.csv' ".format(os.getcwd()) + 
	'WITH HEADER=TRUE"')

def cqlsh_load_user_song():
  	return ('cqlsh -e "COPY sparkifydb.user_and_song_model FROM ' +
	"'{}/user_and_song.csv' ".format(os.getcwd()) + 
	'WITH HEADER=TRUE"')


def execute_query(query):
	database_wrapper = DatabaseWrapper()
	return (database_wrapper.execute_query(query))
