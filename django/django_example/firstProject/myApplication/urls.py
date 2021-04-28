from django.urls import path
from.import views

urlpatterns=[
    path('', views.index),
    path('frontpage', view.showpage3),
    # path('blog', views.blog)
    # path('blog/new', view.blog)

    #:::::::display methods:::::
    #def displayIndex(request,) 

    #::::::::action methonds:::::::
    #def sendHome(request):
    #   return redirect('/')
]