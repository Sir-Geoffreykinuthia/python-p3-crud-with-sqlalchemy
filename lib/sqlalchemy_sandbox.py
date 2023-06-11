#!/usr/bin/env python3

from datetime import datetime

from sqlalchemy import (create_engine, desc, func,
    CheckConstraint, PrimaryKeyConstraint, UniqueConstraint,
    Index, Column, DateTime, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    __table_args__ = (
        # assingning primary ky status to a Column
        PrimaryKeyConstraint(
          'id', name='id_pk'),
        # checking new records to ensure that they do no match existing records at unique Column(s)  
        UniqueConstraint(
            'email', name='unique_email'),
        # here the checkconstraint uses SQL statements to check if new values meet specific criteria 
        CheckConstraint(
            'grade BETWEEN 1 AND 12')
    )
    # the new constraints for the student model enures that id is a primary key
    # email is unique and grade is between 1-12

    Index('index_name', 'name')
    
    id = Column(Integer())
    name =Column(String())
    email = Column(String(55)) 
    grade = Column(String())
    birthday = Column(DateTime())
    enrolled_date = Column(DateTime(), default=datetime.now())

    def __repr__(self):
        return f"student {self.id}: "\
        +f"{self.name}, " \
        +f"Grade {self.grade}"   
        

    id = Column(Integer(), primary_key=True)
    name = Column(String())

if __name__ == '__main__':
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)

    # here we are using our engine to configure a Session class
    Session = sessionmaker(bind=engine)
    # this Session class creates the session object 
    session = Session()

    geoffrey_kinuthia =Student(
        name = "Geoffrey Kinuthia",
        email = "geoffrey@kinuthia.moringa",
        grade = 45,
        birthday =datetime(
            year = 1889,
            month = 2,
            day=14
        ),
    )
    session.add(geoffrey_kinuthia)
    session.commit()

    print(f"Nw student Id is {geoffrey_kinuthia.id}. ")