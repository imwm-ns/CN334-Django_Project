from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def ecommerce_index_view(req):
    '''This function render index page of ecommerce views.'''
    return HttpResponse('Welcome to 6410742412 Narathip Jaroensuk views!')

def item_view(req, item_id):
    context_data = {
        "item_id": item_id
    }
    return render(req, 'index.html', context= context_data)