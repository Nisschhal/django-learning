from django.contrib import admin
from .models import Topic, WebPage, AccessRecord

# Register your models here.
admin.site.register(Topic)
admin.site.register(WebPage)
admin.site.register(AccessRecord)
