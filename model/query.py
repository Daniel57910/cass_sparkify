#queries for dropping data from tables
drop_event = 'drop table if exists sparkifydb.event_data_model'
drop_user_and_session = 'drop table if exists sparkifydb.user_and_session_model'
drop_user_and_song = 'drop table if exists sparkifydb.user_and_song_model'
drop_statements = [drop_event, drop_user_and_session, drop_user_and_song]

#queries for reading data from DB
song_play = 'select artist, song, length from sparkifydb.event_data_model where "sessionId" = 338 and "itemInSession" = 4'
user_and_session = 'select artist, song, "firstName", "lastName", "sessionId" from sparkifydb.user_and_session_model where "userId" = 10 and "sessionId" = 182 order by "sessionId" desc'
user_and_song = 'select "firstName", "lastName" from sparkifydb.user_and_song_model where song = ' +  "'All Hands Against His Own'"

read_statements = {}
read_statements['song_play']              = song_play
read_statements['user_and_session']       = user_and_session
read_statements['user_and_song']          = user_and_song