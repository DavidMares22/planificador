from django.urls import path
from meetings.views import detail,room


urlpatterns = [
   
    path('<int:id>',detail,name='detail'),
    path('rooms/',room,name='rooms'),
    

]