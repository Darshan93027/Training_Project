from django.urls import path 
from .views import PostListView, PostCRUD, CategoryListView, CategoryCRUD

urlpatterns = [
    path('post/', PostListView.as_view(), name='post-list'),
    path('post/<int:id>/', PostCRUD.as_view(), name='post-detail'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:id>/', CategoryCRUD.as_view(), name='category-detail'),
    a
]


