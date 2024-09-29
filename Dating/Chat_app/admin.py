from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(LikeDislike)
admin.site.register(Match)
admin.site.register(Message)
admin.site.register(Preferences)