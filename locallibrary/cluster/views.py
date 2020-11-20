from django.shortcuts import render

# Create your views here.
def index(request):
    """

    :param request:
    :return:
    """
    return render(request, 'clutser/index.html')