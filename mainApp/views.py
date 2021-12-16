from django.shortcuts import render

from . import models 
from django.contrib import messages




def indexPage(request):

    return render(request,"index5.html",{ "all_solutions":models.SolutionDetail.objects.all()})

def about(request):
    
    return render(request,'about.html',{ "all_solutions":models.SolutionDetail.objects.all()})

def contact(request):
    name=''
    email=''
    phone_number=''
    form_message =''
    if request.method == 'POST':
        try:
            name=request.POST['name']
            email=request.POST['email']
            form_message =request.POST['message']
            phone_number=request.POST['phone_number']
            contact = models.Contact.objects.create(name=name,email=email,phone_number=phone_number,message=form_message)
            contact.save()
            messages.success(request, 'Thank you for reach out.. our team will get back to you')

        except:
            messages.success(request, 'Some error Occured Please check the form and try again')
                
    return render(request,'contact.html',{ "all_solutions":models.SolutionDetail.objects.all()})


def solutionDetail(request,pk=None):
    solution= models.SolutionDetail.objects.get(id=pk)
    return render(request,'solutionsDetail.html',{
        "solution":solution,"solution_para":solution.solutiondetailparagraph_set.all(),
        "all_solutions":models.SolutionDetail.objects.all()
        })

def joinPatherShipNetwork(request):
    
    name =''
    email =''
    phone_number =''
    if request.method == 'POST':
        try:
            name =request.POST['name']
            email =request.POST['email']
            phone_number =request.POST['phone']

            data = models.ParthershipNetwork.objects.create(name=name,email=email,phone_number=phone_number)
            data.save()
            messages.success(request, 'Thank you for reach out.. our team will get back to you')
        except:
            messages.success(request, 'Some error Occured Please check the form and try again')
            


    return render(request,'joinPathnershipNetwork.html',{ "all_solutions":models.SolutionDetail.objects.all()})


def workWithEmetrics(request):
    name =''
    email =''
    phone_number =''
    cv = ''
    if request.method == 'POST':
        try:
            name =request.POST['name']
            email =request.POST['email']
            phone_number =request.POST['phone']
            cv = request.FILES['cv_doc']

            data = models.WorkWithus.objects.create(upload_cv=cv,
                name=name,email=email,phone_number=phone_number)
            data.save()
            messages.success(request, 'Thank you for reach out.. our team will get back to you')
        except:
            messages.success(request, 'Some error Occured Please check the form and try again')
            
    return render(request,'workWithEmetrics.html',{ "all_solutions":models.SolutionDetail.objects.all()})


def all_insightPage(request):
    return render(request,'insightPage.html',{ "all_solutions":models.SolutionDetail.objects.all()})

def our_team(request):
    return render(request,'ourTeam.html')