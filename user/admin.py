from django.contrib import admin
from user.models import User, DocumentName, Document


admin.site.register(User)
admin.site.register(DocumentName)
admin.site.register(Document)
