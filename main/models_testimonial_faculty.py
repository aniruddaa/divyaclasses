from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    image = models.ImageField(upload_to='faculty/', blank=True)
    bio = models.TextField(blank=True)
    def __str__(self):
        return self.name
