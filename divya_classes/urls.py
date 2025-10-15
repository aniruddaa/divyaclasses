from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main import views as main_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.home, name='home'),
    path('enquiry/', main_views.enquiry, name='enquiry'),
    path('enquiry-page/', main_views.enquiry_page, name='enquiry_page'),
    path('ai-chatbot/', main_views.ai_chatbot_api, name='ai_chatbot_api'),
    path('admin-panel/', main_views.admin_panel, name='admin_panel'),
    path('admin/enquiries/', main_views.admin_enquiries, name='admin_enquiries'),
    path('admin/videos/', main_views.admin_videos, name='admin_videos'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
