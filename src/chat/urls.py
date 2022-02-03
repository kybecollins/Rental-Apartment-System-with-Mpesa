from django.urls import path
from chat.views import(
    home,
    room,
    send,
    getMessages,
    checkview
)

app_name='chat'
urlpatterns = [
    path('',home, name='home'),
    path('<str:room>/',room, name='room'),
    path('checkview',checkview, name='checkview'),
    path('send',send, name='send'),
    path('getMessages/<str:room>/',getMessages, name='getMessages'),

]