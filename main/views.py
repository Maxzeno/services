from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.core.mail import EmailMultiAlternatives
from .models import Contact
from decouple import config

# Create your views here.

class Index(View):
	def get(self, request):
		return render(request, 'index.html', {})

	def post(self, request):
		data = dict(request.POST)
		data.pop('csrfmiddlewaretoken')

		contact = Contact(**self.dict_normaliser(data))
		contact.save()

		msg = EmailMultiAlternatives(f"{data['name']} needs a Website - {data['whatsapp']} - {data['email']}", f"{data['name']} needs a Website - {data['whatsapp']} - {data['email']} \n\n {data['message']}", 
			config('EMAIL_HOST_USER'), ['nwaegunwaemmauel@gmail.com'])
		msg.send()
		return HttpResponse('OK')


	def dict_normaliser(self, data):
		for key in data:
			data[key] = data[key][0]
		return data

