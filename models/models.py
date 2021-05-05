from sqlalchemy import *
from sqlalchemy import Column, Integer, String, DateTime, Text
from settings.database import Base
from datetime import datetime


class Audio():
		"""docstring for Audio"""

		uploaded_time = Column(DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.utcnow)
		duration_in_sec = Column(Integer, default=0, nullable=False)
		

class Song(Audio, Base):
		"""docstring for Song"""
		__tablename__ = 'song'

		id = Column(Integer, primary_key=True)
		name = Column(String(100), nullable=False)

class Podcast(Audio, Base):
		"""docstring for Podcast"""
		__tablename__ = 'podcast'

		id = Column(Integer, primary_key=True)
		name = Column(String(100), nullable=False)
		host = Column(String(100), nullable=False)
		participants = Column(Text, nullable=True)

class Audiobook(Audio, Base):
		"""docstring for Audiobook"""
		__tablename__ = 'audiobook'

		id = Column(Integer, primary_key=True)
		title = Column(String(100), nullable=False)
		author = Column(String(100), nullable=False)
		narrator = Column(String(100), nullable=False)
