from django.contrib import admin
from django.urls import path, include

# Graphql Import
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from .schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gql/', GraphQLView.as_view(graphiql=True)),
]
