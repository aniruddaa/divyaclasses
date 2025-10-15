from django.db import models
# --- Testimonials and Faculty ---
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
from django.db import models



class LectureVideo(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	video = models.FileField(upload_to='videos/')
	uploaded_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title


class Enquiry(models.Model):
	STANDARD_CHOICES = [
		("8th", "8th"),
		("9th", "9th"),
		("10th", "10th (SSC/HSC/CBSE)"),
		("11th", "11th (HSC/CBSE)"),
		("12th", "12th (HSC/CBSE)"),
		("JEE", "JEE"),
		("NEET", "NEET"),
		("CET", "CET"),
	]
	name = models.CharField(max_length=100)
	email = models.EmailField()
	phone = models.CharField(max_length=20, blank=True)
	standard = models.CharField(max_length=20, choices=STANDARD_CHOICES)
	message = models.TextField(blank=True)
	submitted_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.name} ({self.standard})"
