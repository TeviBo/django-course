from django.urls import path, re_path

from . import views

APP_NAME = "person_app"

urlpatterns = [
    path("personas/", views.ListaPersonas.as_view(), name="personas"),
    path("api/person/", views.PersonListApiView.as_view(), name='person-list'),
    path("api/person/add", views.PersonCreateView.as_view(), name='person-add'),
    path("api/person/profile/<pk>/", views.PersonDetailView.as_view(), name='person-detail'),
    path("api/person/delete/<pk>/", views.PersonDeleteView.as_view(), name='person-delete'),
    path("api/person/update/<pk>/", views.PersonUpdateView.as_view(), name='person-update'),
    path("api/person/modify/<pk>/", views.PersonRetrieveUpdateView.as_view(), name='person-modify'),
    path("api/person/hobbies", views.HobbyListApiView.as_view(), name='hobby-list'),
    path("api/person/hobbies/new", views.CreateHobbyView.as_view(), name='hobby-add'),
    path("api/person/meets/", views.MeetListApiView.as_view(), name='meet-list'),
    path("api/person/meets-link/", views.MeetListApiViewLink.as_view(), name='meet-list-link'),
    path("api/person/meets/new", views.CreateMeetView.as_view(), name='meet-add'),
    path("api/person/meets/by-job/", views.MeetsByPersonJob.as_view(), name='meet-by-job'),
]
