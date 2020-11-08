"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += [
    path('HotZone/', include('HotZone.urls')),
]
urlpatterns += [
    path('', RedirectView.as_view(url='/HotZone/')),
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += [
    path('reset_password/',
    auth_views.PasswordResetView.as_view(template_name="../templates/registration/password_reset.html"),
    name="reset_password"),

    path('reset_password_sent/', 
    auth_views.PasswordResetDoneView.as_view(template_name="../templates/registration/password_reset_sent.html"), 
    name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name="../templates/registration/password_reset.html"), 
    name="password_reset_confirm"),

    path('reset_password_complete/', 
    auth_views.PasswordResetCompleteView.as_view(template_name="../templates/registration/password_reset_done.html"), 
    name="password_reset_complete"),
]
# urlpatterns += [
#     path('accounts/', include('django.contrib.auth.urls')),
#  ]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
