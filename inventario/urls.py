from django.urls import path

from . import views

app_name = "inventario"

urlpatterns =[    
    path("", views.ServidorList.as_view(), name="list"),
    path("create/", views.ServidorCreate.as_view(), name="create"),
    path("update/<int:pk>/", views.ServidorUpdate.as_view(), name="update"),
    path("detail/<int:pk>/", views.ServidorDetail.as_view(), name="detail"),
    path("delete/<int:pk>/", views.ServidorDelete.as_view(), name="delete"),
    path('export/csv-database-write/', views.csv_database_write, name='csv_database_write'),
]