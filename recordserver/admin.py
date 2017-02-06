from sumatra.recordstore.django_store.models import Project
from sumatra_server.models import ProjectPermission
from django.contrib import admin

admin_site = admin.AdminSite()

admin_site.register(Project)
admin_site.register(ProjectPermission)