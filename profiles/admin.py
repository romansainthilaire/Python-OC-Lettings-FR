from django.contrib import admin

from profiles.models import Profile


class ProfileAdmin(admin.ModelAdmin):

    list_display = ["user", "favorite_city"]
    list_filter = ["favorite_city"]


admin.site.register(Profile, ProfileAdmin)

admin.site.site_header = "Orange County Lettings"
