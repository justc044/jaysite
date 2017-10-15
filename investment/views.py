#-*- coding: utf-8 -*-

from django.shortcuts import render
from .models import StockMarketItem, Objective, Phase, Blog
from .forms import StockForm, BlogForm
from django.shortcuts import redirect
from datetime

def home(request):
    posts = Blog.objects.order_by('-post_date')[:3]
    return render(request, 'home.html',{'posts': posts})

def about(request):
    return render(request, 'about.html')

def blogs(request):
    try:
        posts = Blog.objects.all()
    except Objective.DoesNotExist:
        raise Http404("No blog exists")
    return render(request, 'blog_list.html', {'posts': posts})

def blog_list(request, id):
    try:
        post = Blog.objects.get(pk=id)
    except Objective.DoesNotExist:
        raise Http404("Something's wrong with the post")
    return render(request, 'blog.html', {'post': post})

def blog_new(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.category = blog.category.encode('utf-8')
            blog.publish_date = datetime.datetime.now()
            blog.save()
            return redirect('blogs')
    else:
        form = BlogForm()
    return render(request, 'blog_edit.html', {'form': form})

def invest_list(request):
    stockitems = StockMarketItem.objects.all()
    try:
        objective = Objective.objects.order_by('post_date')[:1]
    except Objective.DoesNotExist:
        raise Http404("Objective does not exist")
    phases = Phase.objects.order_by('enddate')
    return render(request, 'investment/invest_list.html'
, {'stocks': stockitems, 'objective': objective, 'phases': phases})

def invest_new(request):
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.comment_during = ""
            stock.comment_after = ""
            stock.save()
            return redirect('invest_list')
    else:
        form = StockForm()
    return render(request, 'investment/invest_edit.html', {'form': form})

def invest_edit(request, pk):
    stock = get_object_or_404(StockMarketItem, pk=pk)
    if request.method == "POST":
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.comment_during = ""
            stock.comment_after = ""
            stock.save()
            return redirect('invest_detail', pk=stock.pk)
    else:
        form = StockForm(instance=post)
    return render(request, 'blog/invest_edit.html', {'form': form})
