from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    P_obj = Phone.objects.all().order_by('price')
    if sort == 'min_price':
        P_obj = Phone.objects.all().order_by('price')
    else:
        if sort == 'max_price':
            P_obj = Phone.objects.all().order_by('price').reverse()
        else:
            if sort == 'name':
                P_obj = Phone.objects.all().order_by('name')
    context = {'phones': P_obj}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.get(slug=slug)}
    return render(request, template, context)
