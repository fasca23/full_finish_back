from django.urls import path
from cloud_api.views import view_files as views

urlpatterns = [
     path('', views.getMyFiles, name = 'listfiles'),
     path('user/<int:pk>/', views.FileList, name = 'filelistuser'),
     path('<int:pk>/', views.FileDetail, name = 'detailfile'),
     path('download/<int:pk>/', views.download, name = 'download'),
     path('downloadshare/<uuid:pk>/', views.download_share, name = 'download_share'),
     path('create/', views.CreateFile, name = 'createfile'),
     path('edit/<int:pk>/', views.EditFile, name = 'editfile'),
     path('delete/<int:pk>/', views.DeleteFile, name = 'deletelfile'),
]