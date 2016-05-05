import graphene
import models
class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, args, info):
        return models.querySome()

schema = graphene.Schema(query=Query)

result = schema.execute('{ hello }')
print result.data['hello']
