from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import ListView
from .forms import FlashcardForm
from django.urls import reverse_lazy
from .models import Flashcard
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import FindForm
#from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from . import forms
@login_required(login_url='/login/')
def IndexView(request,num=1):
    #template_name='index.html'
    #(public_user,public_group)=get_public()
    #flashcard_list=Flashcard.objects.all()
    #page=Paginator(flashcard_list,3)
    params={
        #'data': page.get_page(num),
        }
    return render(request,'index.html',params)

@login_required(login_url='/login/')
def FlashcardCreateView(request):
    params={
        'form': FlashcardForm(),
        }
    if(request.method=='POST'):
        obj=Flashcard()
        flashcard=FlashcardForm(request.POST,instance=obj)
        flashcard.save()
        #success_url=reverse_lazy('flashcard:flashcard_list')
        return redirect(to='/index/list')
    return render(request,'flashcard_create.html',params)
"""   
class FlashcardCreateCompleteView(TemplateView):
    template_name='flashcard_create_complete.html'


class FlashcardListView(ListView):
    template_name='flashcard_list.html'
    flashcard_list=Flashcard.objects.all()
    model=Flashcard
"""
def edit(request, num):
    obj=Flashcard.objects.get(id=num)
    if(request.method == 'POST'):
        flashcard = FlashcardForm(request.POST, instance=obj)
        flashcard.save()
        return redirect(to='/index/list')
    params={
        'id':num,
        'form':FlashcardForm(instance=obj),
    }
    return render(request, 'edit.html',params)

def delete(request,num):
    flashcard=Flashcard.objects.get(id=num)
    if(request.method=='POST'):
        flashcard.delete()
        return redirect(to='/index/list')
    params={
        'id':num,
        'obj':flashcard,
        }
    return render(request, 'delete.html',params)

def find(request,num=1):
    if(request.method == 'POST'):
        form=FindForm(request.POST)
        str=request.POST['find']
        flashcard_list=Flashcard.objects.filter(word__contains=str)
    else:
        form=FindForm()
        flashcard_list=Flashcard.objects.all()
    page=Paginator(flashcard_list,10)
    params = {
        'form': form,
        'flashcard_list': page.get_page(num),
        #'data': page.get_page(num),
        }
    
    
    return render(request,'flashcard_list.html',params)

def test(request):
    #template_name='index.html'
    #(public_user,public_group)=get_public()
    #flashcard_list=Flashcard.objects.all()
    #flashcard_list.number
    #flashcard=Flashcard.objects.get(id=num)
    params={
        #'data': page.get_page(num),
        }
    return render(request,'index.html',params)

class LoginView(LoginView):
    form_class=forms.LoginForm
    template_name="login.html"
    
class test_Indexview(generic.ListView):
    model=Flashcard
    paginate_by=10
    template_name='post_list.html'

class DetailView(generic.DetailView):
    model=Flashcard
    template_name='post_detail.html'
