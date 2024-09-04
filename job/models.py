from django.db import models
from django.utils.text import slugify 

# Define choices for gender and job type
GENDER_TYPE = (
    ("Male", "Male"),
    ("Female", "Female"),
)

JOB_TYPE = (
    ("Full Time", "Full Time"),
    ("Part Time", "Part Time"),
)

class Category(models.Model):
    nama = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.nama

def image_upload(instance, filename):
    image_name, extension = filename.split(".")
    return f"Jobs/{instance.id}.{extension}"

class Job(models.Model):
    title = models.CharField(max_length=50)
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField()
    publishAt = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    experience = models.IntegerField(default=1)
    gender = models.CharField(max_length=10, choices=GENDER_TYPE)
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.title

class Apply(models.Model):
    job = models.ForeignKey(Job, related_name='applications', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    website = models.URLField(max_length=40)
    cv = models.FileField(max_length=80)
    email = models.EmailField(max_length=30)
    createdAt = models.DateTimeField(auto_now=True)
    cover_letter = models.TextField(max_length=150)
    
    def __str__(self) -> str:
        return self.name
