from django.contrib import admin

from .models import Advertisement


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'auction', 'created_date', 'updated_at']
    list_filter = ['auction', 'created_at']
    list_editable = ['auction']
    actions = ['make_auction_as_false', 'make_auction_as_true', 'make_auction_as_invert']
    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description')
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })

    )

    @admin.action(description='Отключить возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Включить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

    @admin.action(description='Изменить значение доступности торга на противоположное')
    def make_auction_as_invert(self, request, queryset):
        for obj in queryset:
            obj.auction = not obj.auction
            obj.save()

admin.site.register(Advertisement, AdvertisementAdmin)
