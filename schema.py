import graphene
from graphene import relay
from graphene.contrib.sqlalchemy import (SQLAlchemyConnectionField,
                                         SQLAlchemyNode)
from models import Degrees as DegreesModel
from models import Objects as ObjectsModel
import models
from database import db_session


class Degrees(SQLAlchemyNode):

    class Meta:
        model = DegreesModel

class InvestedCompany(SQLAlchemyNode):

    class Meta:
        model = ObjectsModel

#@schema.register
#class FundingRounds(SQLAlchemyNode):

 #   class Meta:
  #      model = RoundsModel



class Query(graphene.ObjectType):
    #institute = graphene.String(round=graphene.String())
    all_degrees = SQLAlchemyConnectionField(Degrees, fundingRound = graphene.String())
    all_invested_companies = SQLAlchemyConnectionField(InvestedCompany, college=graphene.String())

    node = relay.NodeField()

    def resolve_all_degrees(self, args, info):
        fundingRound = args.get('fundingRound')
        return models.queryRoundCollege(fundingRound)

    def resolve_all_invested_companies(self, args, info):
        college = args.get('college')
        return models.queryInvestorCompany(college)


# class Query1(graphene.ObjectType):
#     all_companies = SQLAlchemyConnectionField(Objects, college = graphene.String())
#
#     node = relay.NodeField()
#
#     def resolve_all_companies(self, args, info):
#         college = args.get('college')
#         return models.queryInvestorCompany(college)


schema = graphene.Schema(query = Query)