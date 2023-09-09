from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base


class Person(Base):

    __tablename__ ='person'
    id = Column(Integer,primary_key=True, index=True)
    firstname = Column(String(40), nullable= false)
    lastname = Column(String(40), nullable= false)
    isMale = Column(Boolean)
    