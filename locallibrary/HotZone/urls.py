from django.contrib import admin
from django.urls import include,path 
from HotZone import views
from django.views.generic import RedirectView
urlpatterns = [
    path('', views.index, name='index'),
    path('SearchItem/',views.searchItem,name='searchItem'),
    path('Search/',views.search,name='search'), #在search当中implement使用外部API进行地址的添加
    path('Home/',views.index ,name='home'),
    path('Virus/',views.VirusListView.as_view(),name='virus'),
    path('Virus/<int:pk>', views.VirusDetailView.as_view(), name='virus-detail'),
    path('Patient/',views.PatientListView.as_view(),name='patient'),
    path('Patient/<int:pk>', views.PatientDetailView.as_view(), name='patient-detail'),
    path('Case/',views.CaseListView.as_view(),name='case'),
    path('Case/<int:pk>', views.CaseDetailView.as_view(), name='case-detail'),
    path('Location/',views.LocationListView.as_view(),name='location'),
    path('Location/<int:pk>', views.LocationDetailView.as_view(), name='location-detail'),
    path('Visit/',views.VisitListView.as_view(),name='visit'),
    path('Visit/<int:pk>', views.VisitDetailView.as_view(), name='visit-detail'),
    
    # path('addLocation/<str:id>',views.AddLocation,name="addLocation"),
    path(r'^addLocation/$', views.AddLocation, name="addLocation"),
]
