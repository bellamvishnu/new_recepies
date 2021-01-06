from django.shortcuts import render,get_object_or_404
from . models import Recipe
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Recipe


def index(request):
    context = Recipe.objects.all()
    return render(request,'recipe/index.html',{'context':context})


def detail(request,id):
    ch = get_object_or_404(Recipe,pk=id)
    return render(request,'recipe/detail.html',{'ch':ch})


def create(request):
    if request.method == 'POST':
        Recipe.objects.create(
            name = request.POST["name"],
            ingre = request.POST["ingre"],
            process = request.POST["process"],
        )
        return HttpResponseRedirect(reverse('recipe:index'))
    return render(request,'recipe/create.html')


def delete_recipe(request, pk):
    Recipe.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('app:recipes_list'))

# def create_1(request):
#     if request.method == 'GET':
#         Recipe.objects.create(
#             name = request.GET["name"],
#             ingre = request.GET["ingre"],
#             process = request.GET["process"],
#         )
#         return HttpResponseRedirect(reverse('recipe:index'))
#     return render(request,'recipe/create_1.html')
