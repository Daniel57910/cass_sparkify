from lib.file_finder import FileFinder
from lib.data_loader import DataLoader
import os

def has_hashable_key(key):
    return len(str(key)) > 0

def create_aggregate_csv():

    event_columns = ['sessionId', 'itemInSession', 'artist', 'firstName', 'gender', 'lastName', 'length', 'level', 'location', 'song', 'userId']
    user_columns = ['userId', 'sessionId', 'artist', 'firstName', 'gender', 'itemInSession', 'lastName', 'length', 'level', 'location', 'song']
    user_and_song_columns = ['song', 'firstName', 'lastName']

    event_data_path = os.getcwd() + '/event_data'
    aggregate_csv_path = os.getcwd() + '/event_datafile_new.csv'
    user_and_session_path = os.getcwd() + '/user_and_session.csv'
    user_and_song_path = os.getcwd() + '/user_and_song.csv'

    file_finder = FileFinder(event_data_path, '*.csv')
    all_csv_files = file_finder.return_file_names()
    data_loader = DataLoader(all_csv_files)
    csv_dataframe = data_loader.create_dataframe_from_files()

    event_frame = csv_dataframe[
     csv_dataframe.itemInSession.apply(has_hashable_key) &
     csv_dataframe.sessionId.apply(has_hashable_key)
    ]

    user_frame = csv_dataframe[
     csv_dataframe.userId.apply(has_hashable_key) &
     csv_dataframe.sessionId.apply(has_hashable_key)
    ]
    
    user_and_song_frame = csv_dataframe[
      csv_dataframe.song.apply(has_hashable_key)
    ]

    event_frame[event_columns].to_csv(
        path_or_buf=aggregate_csv_path, index=False
		)

    user_frame[user_columns].to_csv(
			path_or_buf=user_and_session_path, index=False
		)

    user_and_song_frame[user_and_song_columns].to_csv(
      path_or_buf=user_and_song_path, index=False
    )
