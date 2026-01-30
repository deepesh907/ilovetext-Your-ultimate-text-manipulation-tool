from django.contrib import admin
from django.urls import path
from tools import views

urlpatterns = [
    path("admin/", admin.site.urls),

    # Pages
    # path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("service/", views.service, name="service"),
    path("pricing/", views.pricing, name="pricing"),
    path("guide/", views.guide, name="guide"),
    path("", views.upload_page, name="upload_page"),
    path("download-pdf/", views.download_pdf, name="download_pdf"),
    path("download-docx/", views.download_docx, name="download_docx"),
    path("download-txt/", views.download_txt, name="download_txt"),
    



    # AJAX endpoints
    path("upload-file/", views.upload_file, name="upload_file"),
    path("process-text/", views.process_text, name="process_text"),
]
