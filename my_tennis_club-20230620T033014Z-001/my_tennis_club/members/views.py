from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from members.models import Member
from members.models import Person


def root(request):
	template = loader.get_template('root.html')
	return HttpResponse(template.render())

# Create your views here.
def members(request):
	template = loader.get_template('myfirst.html')
	return HttpResponse(template.render())


def testing(request):
	mydata = Member.objects.all()
	template =loader.get_template('template.html')
	context = {
	    'mymembers' : mydata,
	}
	return HttpResponse(template.render(context,request))


def myapp(request):
  mydata = Person.objects.all()
  template = loader.get_template('myapp.html')
  context = {
      'mymember' : mydata
  }
  return HttpResponse(template.render(context,request))

def details(request,id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
   'mymember' : mymember
  }
  return HttpResponse(template.render(context,request))