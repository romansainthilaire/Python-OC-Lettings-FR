from django.contrib import admin

from lettings.models import Address, Letting


class AdressAdmin(admin.ModelAdmin):

    list_display = ["address", "country_iso_code"]
    list_filter = ["city"]

    def address(self, obj):
        return f"{obj.number} {obj.street}, {obj.city}, {obj.state} {obj.zip_code}"


class LettingAdmin(admin.ModelAdmin):

    list_display = ["title", "location"]
    search_fields = ["title"]

    def location(self, obj):
        return (
            f"{obj.address.number} {obj.address.street}, {obj.address.city}, " +
            f"{obj.address.state} {obj.address.zip_code}"
            )


admin.site.register(Address, AdressAdmin)
admin.site.register(Letting, LettingAdmin)
