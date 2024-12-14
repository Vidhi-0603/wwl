from django.contrib import admin
from .models import members,property,Enquiry,Agents,AgentsInfo,Contact_User

# Register your models here.

admin.site.register(members)
admin.site.register(property)
admin.site.register(Enquiry)
admin.site.register(Agents)
admin.site.register(AgentsInfo)
admin.site.register(Contact_User)