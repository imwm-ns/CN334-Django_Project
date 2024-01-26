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

def home_view(req):
    return render(req, 'home.html')

def category_view(req):
    return render(req, 'category.html')

def product_view(req, id):
    data = {
        "id": id
    }
    return render(req, 'product.html', context=data)

def admin_view(req, id):
    data = {
        "id": id
    }
    return render(req, 'admin.html', context=data)

def contact_view(req):
    return render(req, 'contact.html')