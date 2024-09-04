from .models import Job
from django.core.paginator import Paginator
from .form import ApplyForm
from django.shortcuts import render, get_object_or_404

# Create your views here.
def job_list(request):
    job_list = Job.objects.all()
    paginator = Paginator(job_list, 2)  # Show 1 job per page (adjust as needed)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "jobs": page_obj,
        "jobsCounts": job_list.count()
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