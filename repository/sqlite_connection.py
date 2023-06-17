from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SqliteConnection:
    _instance = None
    _connection = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._connection = create_engine('sqlite:///addresses.sqlite')
            Base.metadata.create_all(bind=cls._connection)
        return cls._instance

    @property
    def connection(self):
        return self._connection

    def create_session(self):
        from sqlalchemy.orm import sessionmaker
        Session = sessionmaker(bind=self._connection)
        return Session()

    def __enter__(self):
        self._session = self.create_session()
        return self._session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._session.close()