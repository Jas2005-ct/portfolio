from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(Education)
admin.site.register(Certificate)
admin.site.register(Internship)
admin.site.register(Profession)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(SocialLink)
admin.site.register(Resume)
admin.site.register(Technology)