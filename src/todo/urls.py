from django.conf.urls import url, include
from todo import views
from rest_framework.routers import DefaultRouter

#create a router and register our viewsets with it
router = DefaultRouter(trailing_slash=False)
router.register(r'todos', views.TodoItemViewSet)

#the API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls))
]