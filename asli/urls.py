from django.urls import path
from . import views


urlpatterns = [
    path("",views.home,name="home"),
    path("add",views.add_work,name="add_title"),
    path("delet/<int:id>",views.del_work,name="del_title"),
    path("complet/<int:id>",views.complete_work,name="complete_work")

]
