from django.urls import path
from django.contrib import admin
from .import views 
# from .views import bookcreate
from django.urls import path, include


app_name = 'booking'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    # path('', views.XDSoftDateTimePickerView.as_view(), name='xdsoft'),
   
    path('create/', views.BookCreate.as_view(), name='book-create'),
    path('booking/<int:pk>/', views.DetailView.as_view(), name='book-detail'),
    path('booking/<int:pk>/update/', views.BookEdit.as_view(), name='book-update'),
    path('booking/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),

    

    # path('', index, name='home'),
    # path('detail/<id>/', detail, name='detail'),
    # path('create/', bookcreate, name='create'),
    
    
    # path('manual-form/', views.ManualFormView.as_view(), name='manual'),
    # path('bootstrap-datetimepicker/', views.BootstrapDateTimePickerView.as_view(), name='bootstrap'),
    # path('fengyuanchen-datepicker/', views.FengyuanChenDatePickerView.as_view(), name='fengyuanchen'),

   
]
