from django.shortcuts import render

from . import models 



def indexPage(request):

    return render(request,"index5.html",{ "all_solutions":models.SolutionDetail.objects.all()})

def about(request):
    
    return render(request,'about.html',{ "all_solutions":models.SolutionDetail.objects.all()})

def contact(request):
    
    return render(request,'contact.html',{ "all_solutions":models.SolutionDetail.objects.all()})


def solutionDetail(request,pk=None):
    solution= models.SolutionDetail.objects.get(id=pk)
    return render(request,'solutionsDetail.html',{
        "solution":solution,"solution_para":solution.solutiondetailparagraph_set.all(),
        "all_solutions":models.SolutionDetail.objects.all()
        })