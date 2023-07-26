from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.redirect_to_login),
    path('index/', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('about/', views.about, name="about"),
    path('projects/', views.projects, name="projects"),
    path('projects/<int:id>', views.project_detail, name="project_detail"),
    path('tasks/', views.tasks, name="tasks"),
    path('create_task/', views.create_task, name="create_task"),
    path('create_project/', views.create_project, name="create_project"),
    path('products/', views.products, name="products"),
    path('create_product/', views.create_product, name="create_product"),
    path('product_detail/<int:id>/', views.product_detail, name="product_detail"),
    path('products/<int:id>/edit/', views.edit_product, name='edit_product'),
    path('product_detail/<int:id>/delete/', views.delete_product, name='delete_product'),
    path('terms/', views.terms_and_conditions, name='terms'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
]
