import django_filters
from .models import Job

class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Job
        fields = ['title', 'category','gender','experience']
        exclude=['owner','slug','image','salary','vacancy','job_type','description','publishAt']