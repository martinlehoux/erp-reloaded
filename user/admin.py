from django.contrib import admin

from user.models import Document, DocumentName, User

admin.site.register(User)
admin.site.register(DocumentName)
admin.site.register(Document)
