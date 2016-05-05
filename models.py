from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from database import engine, Base


def loadSession():
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

class Degrees(Base):
    __tablename__ = 'cb_degrees'
    __table_args__ = {'autoload': True}

class FundingRounds(Base):
    __tablename__ = 'cb_funding_rounds'
    __table_args__ = {'autoload': True}

class People(Base):
    __tablename__ = 'cb_people'
    __table_args__ = {'autoload': True}


class Objects(Base):
    __tablename__ = 'cb_objects'
    __table_args__ = {'autoload': True}

class Investments(Base):
    __tablename__ = 'cb_investments'
    __table_args__ = {'autoload': True}

#class Growth(FundingRounds):
#class InvestedCompany(Base):
    #__tablename__ = 'employee'
    #id = Column(Integer, primary_key=True)
    #name = Column(String)
    #investor_id = column(String, ForeignKey('cb_investments.investor_id'))
    # Use default=func.now() to set the default hiring time
    # of an Employee to be the current time when an
    # Employee record was created
    # Use cascade='delete,all' to propagate the deletion of a Department onto its Employees
    #investor = relation(
     #   Investments,
      #  backref=backref('',
       #                 uselist=True,
        #                cascade='delete,all'))


meta = MetaData()
meta.reflect(bind = engine)
objects_table = meta.tables['cb_objects']
investment_table = meta.tables['cb_investments']
people_table = meta.tables['cb_people']
degrees_table = meta.tables['cb_degrees']



def queryRoundCollege(fundingRound):
    session = loadSession()


    res = session.query(Degrees).join(People, Degrees.object_id == People.object_id). \
        join(Objects, Objects.name == People.affiliation_name). \
        join(FundingRounds, FundingRounds.object_id == Objects.id). \
        filter(FundingRounds.funding_round_type == fundingRound).distinct()

    return res

def queryInvestorCompany(college):
    session = loadSession()




    res1 = session.query(Objects).join(People, People.affiliation_name == Objects.name).\
        join(Degrees, Degrees.object_id == People.object_id).\
        filter(Degrees.institution == college).subquery()

    res2 = session.query(Investments).join(Degrees, Degrees.object_id == Investments.investor_object_id).\
        filter(Degrees.institution == college).subquery()
    res3 = session.query(Objects).join(res1, res1.c.id == Objects.id).join(res2, res2.c.funded_object_id == res1.c.id)

    return res3

    #return session.query(InvestedCompany).from_statement(res5)



if __name__ == '__main__':
    res = queryRoundCollege("series-b")
    #session = loadSession()
    print res[0].id