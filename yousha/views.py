from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render_to_response
from yousharizvi.yousha.models import *
from yousharizvi.yousha.forms import *
# Create your views here.
class home(ListView):
    template_name ='home.html'
    model = HomeModel
    context_object_name = 'object_list'

def contact(request):
    return render_to_response('contact.html')
