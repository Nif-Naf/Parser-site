from email.message import Message
from django.contrib import admin

from .models import External, Result, Messages

admin.site.register(External)
admin.site.register(Result)
admin.site.register(Messages)