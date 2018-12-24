from django.contrib import admin
from app.models import ActiveSessions, PGA, Profiles, CPU, Tablespace, TablespaceHistory, Roles, SQLQuery, Users, SGA

# Register your models here.
admin.site.register(ActiveSessions)
admin.site.register(PGA)
admin.site.register(Profiles)
admin.site.register(CPU)
admin.site.register(Tablespace)
admin.site.register(TablespaceHistory)
admin.site.register(Roles)
admin.site.register(SQLQuery)
admin.site.register(Users)
admin.site.register(SGA)

