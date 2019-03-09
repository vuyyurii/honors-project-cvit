from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name = 'search'),
    path('<int:meeting_id>/', views.meeting, name='meeting'),
    path('meeting1', views.temp, name='temp'),
    path('ajax/get_meeting_images', views.get_meeting_images, name='Ajax request for getting images'),
    path('ajax/get_meeting_details', views.get_meeting_details, name='Ajax request for getting meeting details'),
    path('ajax/get_search_results', views.get_search_results, name='Ajax request for getting search results'),
    path('ajax/get_index_page', views.get_index_page, name='Ajax request for getting index page')
]