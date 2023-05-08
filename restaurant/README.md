# [restaurant api using graphql](https://www.codecademy.com/article/smyja/how-to-use-graphql-with-django)

to use GraphQL in your application you need to install the following packages:
1. graphene-django - `pip3 install graphene-django` -  then since it is a third part package you need to add it to the list of installed apps

## graphql configuration

### GraphQL urls

from the normal django url styling for apps, we are going to need to take a twist for our app to function as a graphql application

for normal django routes we normally declare routes this way:

```python
from django.url import path

urlpatterns = [
    path('/users', view.as_view, name='users'),
]
```

but for our graphql we are going to define routes this way:

we need to import the graphql view first from `graphene_django`

```python
from graphql_django import GraphQLView
```

this is the view that we are going to pass a parameter to our application url

```python

...
from graphql_django import GraphQLView
from django.urls import path
from django.view.decorators import crsf_excempt

urlpatterns = [
    path('graphql', crsf_excempt(GraphQLView.as_view(graphiql=True)))
]
```

### GraphQL Schemas

the components that make up the GraphQL schema include:

1. object types - these represent the entities in your data model i.e users, posts, products
2. fields - these represent the set of fields each object types has -  for users it will be something like 'username, email, password,  address'
3. Queries - these represent or specify the operations that can be performed on the data, i.e the CRUD operations
4. Mutations  - these specify the operations that can be used to modify the data i.e creating a new post or updating a user profile.
5. subscription - these allows the users to recieve real time updates when data changes on the server.
   
#### building a GraphQL schema

you first define a schema.py file in your app directory

