from django.http import HttpResponse
from django.shortcuts import render
from .models import article

# Create your views here.
# def home(request):
#     latest_article_list = article.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.body for q in latest_article_list])
#     return HttpResponse(output)

def home(request):
    #latest_article_list = article.objects.order_by('-pub_date')[:5]
    context = locals()
    return render(request, 'home.html', context)

def about(request):
    context = locals()
    return render(request, 'about.html', context)
