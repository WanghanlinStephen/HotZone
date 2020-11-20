from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import *


# Create your views here.
@login_required
def index(request):
    account = Account.objects.get_or_create(user=request.user)[0]
    return render(request, 'account/index.html', context={'account': account})


@login_required
def upload_img(request):
    """
    Upload image
    :param request:
    :param aid:
    :return:
    """
    aid = request.POST['aid']
    account = get_object_or_404(Account, id=aid)
    file_obj = request.FILES.get('image')
    print(file_obj)
    account.avatar = file_obj
    # https://www.webforefront.com/django/modelmethodsandmetaoptions.html#:~:text=save()%20method,the%20instance%20on%20a%20database.
    # Save the record to the database
    account.save()
    messages.success(request, 'update avatar OK!')
    return redirect(f'/admin/account/account/')


@login_required
def update_txt(request):
    """
    Update text info
    :param request:
    :return:
    """
    # request.POST[''],get the data from the front end
    aid = request.POST['aid']
    account = get_object_or_404(Account, id=aid)
    key = request.POST['key']
    value = request.POST['value']
    if key.find('email') >= 0:
        account.user.email = value
        account.user.save()
    else:
        account.__setattr__(key, value)
        account.save()
    messages.success(request, 'update OK!')
    return redirect(f'/admin/account/account/')
