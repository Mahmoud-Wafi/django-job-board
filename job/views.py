from .models import Job
from django.core.paginator import Paginator
from .form import ApplyForm , JobForm
from django.shortcuts import render, get_object_or_404 , redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filters import JobFilter
# Create your views here.
def job_list(request):
    job_list = Job.objects.all()
    myfilter=JobFilter(request.GET,queryset=job_list)
    job_list=myfilter.qs
    paginator = Paginator(job_list, 4) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "jobs": page_obj,
        "jobsCounts": job_list.count(),
        "myfilter":myfilter
    }
    return render(request, 'job/job_list.html', context)

def job_detail(request, slug):
    job_details = get_object_or_404(Job, slug=slug)
    
    if request.method == "POST":
        form = ApplyForm(request.POST , request.FILES)
        if form.is_valid():
           myform= form.save(commit=False)
           myform.job = job_details
           myform.save()
    else:
        form = ApplyForm()
    
    context = {
        "job": job_details,
        "form": form
    }
    
    return render(request, 'job/job_detail.html', context)

@login_required
def add_job(request):
    if request.method == "POST":
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.owner=request.user
            myform.save()
            messages.success(request, "Job added successfully!")
            # return redirect(reverse('jobs:job_list')) 
    else:
        form = JobForm() 

    context = {
        "form": form
    }

    return render(request, 'job/add_job.html', context)