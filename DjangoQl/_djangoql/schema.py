import graphene
from graphene_django import DjangoObjectType #used to change Django object into a format that is readable by GraphQL
from firstApp.models import Contact

class ContactType(DjangoObjectType):
    # Describe the data that is to be formatted into GraphQL fields
    class Meta:
        model = Contact
        field = ("id", "name", "phone_number")

class Query(graphene.ObjectType):
    #query ContactType to get list of contacts
    list_contact=graphene.List(ContactType)
    read_contact=graphene.Field(ContactType, id=graphene.Int())

    def resolve_list_contact(root, info):
        # We can easily optimize query count in the resolve method
        return Contact.objects.all()
    
    def resolve_read_contact(root, info, id):
        return Contact.objects.get(id=id)
    
class ContactMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        phoneNumber = graphene.String()
    contact = graphene.Field(ContactType)

    @classmethod
    def mutate(cls, root, info, name, phoneNumber, id):
         ###########Create##############
        contact = Contact(name=name, phoneNumber=phoneNumber)
        contact.save()  

         ###########Update##############
        get_contact = Contact.objects.get(id=id)
        get_contact.name = name
        get_contact.phoneNumber = phoneNumber
        get_contact.save()
        return ContactMutation(contact=get_contact)
    


class ContactDelete(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    contact = graphene.Field(ContactType)

    @classmethod
    def mutate(cls, root, info, id):
        contact = Contact(id=id)
        contact.delete()

class Mutation(graphene.ObjectType):
    create_contact = ContactMutation.Field()
    update_contact = ContactMutation.Field()
    delete_contact = ContactDelete.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)