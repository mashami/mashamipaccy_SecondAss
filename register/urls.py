from unicodedata import name
from django.urls import path
from .import views 


urlpatterns=[
    path("create",views.create_Trainee,name="create"),
    path("listAllTrainee",views.listAllTrainee, name="listAll"),
    path("editTrainee/<int:id",views.edit_Trainee, name="EditTrainee"),
    path("update/<int:id>",views.update_Trainee, name="update"),
    path("delete/<int:id>",views.delete_Trainee, name="delete"),
    path("log_in",views.log_in, name="logIn")
    

]