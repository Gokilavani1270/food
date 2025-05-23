from . import views
from django.urls import path

app_name='food'
urlpatterns = [
	path('index/',views.index,name='index'),
    path('<int:pk>/',views.FoodDetail.as_view(),name='detail'),
    path('',views.ItemClassView.as_view(),name='item'),
    path('add',views.CreateItem.as_view(),name="create_item"), 
    path('update/<int:id>/',views.update_item,name="update_item"),
    path('delete/<int:id>/',views.delete_item,name="delete_item"),
]
