from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^history/', views.history, name='history'),
    url(r'^house/', views.house, name='house'),
    url(r'^exec/', views.ex, name='ex'),
    url(r'^sisterhood/', views.sisterhood, name='sisterhood'),
    url(r'^philanthropy/', views.philanthropy, name='philanthropy'),
    url(r'^blm/', views.blm, name='blm'),
    url(r'^recruitment/', views.recruitment, name='recruitment'),
    url(r'^faq/', views.faq, name='faq'),
    url(r'^sisters/', views.sisters, name='sisters'),
    url(r'^involvement/', views.involvement, name='involvement'),
    url(r'^alumni/', views.alumni, name='alumni'),
    url(r'^outsidemit/', views.outsidemit, name='outsidemit'),
]
