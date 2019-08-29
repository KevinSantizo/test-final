from django.urls import path
from estate import views

app_name = 'estate'
urlpatterns = [
    path('index/<int:user_pk>/', views.index, name='index'),
    path('actions/<int:user_pk>/', views.actions, name='actions'),
    path('new-land/<int:user_pk>/', views.new_land, name='new-land'),
    path('edit-land/<int:land_pk>/', views.edit_land, name='edit-land'),
    path('delete-land/<int:land_pk>/', views.delete_land, name='delete-land'),
    path('actions-plot/<int:user_pk>/', views.actions_plot, name='actions-plot'),
    path('new-plot/<int:user_pk>/', views.new_plot, name='new-plot'),
    path('edit-plot/<int:plot_pk>/', views.edit_plot, name='edit-plot'),
    path('delete-plot/<int:plot_pk>/', views.delete_plot, name='delete-plot'),
    path('actions-tree-admin/<int:user_pk>/', views.actions_tree_admin, name='actions-tree-admin'),
    path('actions-tree-user/<int:user_pk>/', views.actions_tree_user, name='actions-tree-user'),
    path('new-tree/<int:user_pk>/', views.new_tree, name='new-tree'),
    path('edit-tree/<int:tree_pk>/', views.edit_tree, name='edit-tree'),
    path('delete-tree/<int:tree_pk>/', views.delete_tree, name='delete-tree'),
]
