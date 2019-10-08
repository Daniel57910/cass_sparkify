from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

class EventDataModel(Model):

    __table_name__ = 'event_data_model'
    sessionId = columns.Integer(primary_key=True)
    itemInSession = columns.Integer(primary_key=True)
    artist = columns.Text()
    firstName = columns.Text()
    gender = columns.Text()
    lastName = columns.Text()
    length = columns.Float()
    level = columns.Text()
    location = columns.Text()
    song = columns.Text()
    userId = columns.Integer()

class UserAndSessionModel(Model):

    __table_name__ = 'user_and_session_model'
    userId = columns.Integer(primary_key=True)
    sessionId = columns.Integer(primary_key=True, clustering_order='DESC')
    artist = columns.Text()
    firstName = columns.Text()
    gender = columns.Text()
    itemInSession = columns.Integer()
    lastName = columns.Text()
    length = columns.Float()
    level = columns.Text()
    location = columns.Text()
    song = columns.Text()

class UserAndSongModel(Model):
	__table_name__ = 'user_and_song_model'
	song = columns.Text(primary_key=True)
	firstName = columns.Text()
	lastName = columns.Text()
