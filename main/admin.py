from django.contrib import admin


from .models import LectureVideo, Enquiry, Testimonial, Faculty
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
	list_display = ('name', 'created_at')
	search_fields = ('name', 'message')

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
	list_display = ('name', 'subject')
	search_fields = ('name', 'subject')


@admin.register(LectureVideo)
class LectureVideoAdmin(admin.ModelAdmin):
	list_display = ('title', 'uploaded_at')

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
	list_display = ('name', 'standard', 'email', 'phone', 'submitted_at')
	list_filter = ('standard', 'submitted_at')
	search_fields = ('name', 'email', 'phone', 'standard')
