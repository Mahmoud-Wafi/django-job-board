from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator

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
def job_detail(request , slug):
    job_details=Job.objects.get(slug=slug)
    context={
        "job":job_details
    }
    return render(request ,'job/job_detail.html' ,context)
    