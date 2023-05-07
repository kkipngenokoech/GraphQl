# GraphQl

GraphQL: APIs for humans

it is a query language for apis, and a runtime for fulfilling those queries with existing data.

GraphQL represents data not in terms of resource URLs, secondary keys, or join tables; but in terms of a graph of objects and the models that are ultimately used in apps, like NSObjects or JSON

To get data from a GraphQL API, create queries from the frontend or client to get data from that particular endpoint.

## GraphQL API and Rest API and Django

we normally create serializers for django rest api

for GraphQL API however, we are going to create schemas.

To set up the schema, create a new file at the same folder where you have your settings.py file and name it schema.py

unlike rest api, graphql doesnt require verbs i.e `POST`, `PUT`, `DELETE` for requests nor do they need multiple end points

they just have one endpoint and making a query to that endpoint is all it is needed.

## properties of GraphQL API

1. schema - describes the functionalities available to the client application that connects to it.
2. Query - a schema type that represents the get request, it defines the functionalities that can be used in reading and fetching data.
3. Nesting -  queries can be nested inside other queries
4. Mutation - a schema type that defines the kind of operations that can be performed to modify data.
5. subscription - notifies the client in real time about the changes in data
6. Resolver - provides a function that returns values for fields associated with existing schemas

