from django.urls import path

from product import views
app_name = 'product'
urlpatterns = [
    # Пока список пуст, чтобы сервер запустился без ошибок.
    # Позже вы добавите сюда пути, например:
    path('', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),

# ОТДЕЛЬНЫЕ СТРАНИЦЫ ДЛЯ SPACE MARINES
    path('space_marines/', views.sm_list, name='sm_list'),
    path('space_marines/<int:pk>/', views.sm_details, name='sm_details'),

    path('imperium/', views.sm_list, name='imp_list'),
    path('imperium/<int:pk>/', views.sm_details, name='imp_details'),

    path('chaos/', views.sm_list, name='chaos_list'),
    path('chaos/<int:pk>/', views.sm_details, name='chaos_details'),

    path('xenos/', views.sm_list, name='xenos_list'),
    path('xenos/<int:pk>/', views.sm_details, name='xenos_details'),
]