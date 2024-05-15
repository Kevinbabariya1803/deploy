from . import views
from django.urls import path

urlpatterns = [
    path('',views.overview,name='overview'),
    path('generate-pdf/', views.generate_pdf, name='generate_pdf'),

    # path('total/',views.totals,name='total')


]