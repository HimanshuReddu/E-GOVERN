from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Complaint,Birth,Death
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import DetailView, ListView
from .forms import ComplaintCreate
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy

def home(request):
    template = loader.get_template('gov1/home.html')
    return HttpResponse(template.render({}, request))


def about(request):
    template = loader.get_template('gov1/about.html')
    return HttpResponse(template.render({}, request))


def gallary(request):
    template = loader.get_template('gov1/gallary.html')
    return HttpResponse(template.render({}, request))


def contactus(request):
    all_complaint = Complaint.objects.all()
    context = {
        'all_complaint': all_complaint,
    }

    return render(request, 'egov/contactus.html', context)


def touristplaces(request):
    template = loader.get_template('gov1/touristplaces.html')
    return HttpResponse(template.render({}, request))



def hospital(request):
    template = loader.get_template('gov1/hospital.html')
    return HttpResponse(template.render({}, request))

def school(request):
    template = loader.get_template('gov1/school.html')
    return HttpResponse(template.render({}, request))

def complaint(request):
    all_complaint = Complaint.objects.all()
    context = {
        'all_complaint': all_complaint,
    }

    return render(request, 'gov1/complaint.html', context)


class ComplaintCreate(CreateView):
    model=Complaint
    fields = ['username', 'email', 'number', 'complaint']
    template_name='gov1/complaint.html'
    success_url = reverse_lazy('gov1:gallery')


class ComplaintList(ListView):
    queryset=Complaint.objects.order_by('username')
    template_name='gov1/gallery.html'


class BirthCreate(CreateView):
    model=Birth
    fields = ['form_no','date','id_number','name','father','mother','dob','gender','occfather','occmother','birthplace','address','number','email']
    template_name='gov1/birth.html'
    success_url = reverse_lazy('gov1:gallery')

class DeathCreate(CreateView):
    model=Death
    fields = ['form_no','date','id_number','name','father','mother','dob','ddate','gender','address','contact','email','cause']
    template_name='gov1/death.html'
    success_url = reverse_lazy('gov1:death')

class ComplaintUpdate(UpdateView):
    model = Complaint
   #form_class = ComplaintCreate
    fields = ['username', 'email', 'number', 'complaint']
    template_name = 'gov1/about.html'
   # success_url = reverse_lazy('gov1:gallery')

class ComplaintDelete(DeleteView):
    model = Complaint
    fields = ['username', 'email', 'number', 'complaint']
    template_name = 'gov1/delete.html'
    #success_url = reverse_lazy('gov1:gallery')

class ComplaintShow(DeleteView):
    model=Complaint
    template_name = 'gov1/show.html'






def delete_complaint(request, username):
    complaint = get_object_or_404(Complaint, pk=username)
    #song = Song.objects.get(pk=song_id)
    complaint.delete()
    return render(request, 'gov1/gallery.html', {'complaint': complaint})




