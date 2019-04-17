from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

# Create your views here.
def index(request):
	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			email = form.cleaned_data['from_email']
			message = form.cleaned_data['message']
			try:
				send_mail(subject, message, email,['johnmastonraines@gmail.com'])
			except BadHeaderError:
				return HttpResponse('Invalid header')
			return redirect('sentpage')
			
	context = {
		'form': form
	}
	return render(request, 'contact/contact.html', context)
	
def sent(request):
	return HttpResponse("your email was sent")