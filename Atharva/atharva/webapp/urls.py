from django.urls import path

from webapp import views

app_name = 'webapp'

urlpatterns = [
    path('', views.home,name="home"),
    path('about', views.about,name="about"),
    path('contact', views.contact, name="contact"),
    path('partners',views.partners_func,name="partners"),
    path('clients',views.clients_page,name="clients"),
    path('administrator',views.upload_partners,name="administrator"),
    path('upload_clients',views.upload_clients,name="upload_clients"),
    path('solutions',views.solutions,name="solutions"),
    path('faq',views.faq,name="faq"),
]
