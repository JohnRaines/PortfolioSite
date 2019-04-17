from django.shortcuts import render
from django.http import HttpResponse
from .models import Pieces

# Create your views here.
def index(request):
	pieces = Pieces.objects.all()
	context = {
		'title':'pieces',
		'pieces': pieces
	}
	return render(request, 'catalog/listings.html', context)
	
def catalog(request):
	return HttpResponse("hello from CATALOT")
	
def details(request, id):
	piece = Pieces.objects.get(id=id)	#get the piece selected
	count = len(Pieces.objects.all().filter(series=piece.series))  #get the total number of pieces in the same series
	
	context = {
		'piece': piece,					#specific piece requested
		'next': (piece.id + 1) % count, #id of next piece in series
		'prev': (piece.id - 1) % count  #id of previous piece in series
	}
	return render(request, 'catalog/piece.html', context)
