from django.conf.urls import patterns, url
from rat import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^home',views.home, name='home'),
    url(r'^personal/', views.personal, name='personal'),
    url(r'^college_ranking/', views.college_ranking, name='college_ranking'),
    url(r'^department_ranking/(?P<dept_id>\w*)/$', views.department_ranking, name='department_ranking'),
    url(r'^personal_profile/', views.personal_profile, name='personal_profile'),
    
    
    #url(r'^current_datetime/',views.current_datetime,name='current_datetime'),
    )