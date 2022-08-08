from django.urls import path
from student import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registration/', views.registration, name="registration"),
    path('instertData/', views.instertData, name="instertData"),
    path('all-records/', views.fetchData, name="all-records"),
    path('editData/<int:id>', views.editData, name="editData"),
    path('updateData/<int:id>', views.updateData, name="updateData"),
    path('deleteData/<int:id>', views.deleteData, name="deleteData"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
]
