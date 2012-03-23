from django.contrib                       import admin
from models                               import Subscription
import datetime

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'phone', 'creat_at')
    date_hierarchy = 'creat_at'
    search_field = ('name', 'cpf', 'email', 'creat_at', 
                     'subscribed_today')
    list_filter = ['creat_at']

    def subscribed_today(self, obj):
        return obj,creat_ad.date() == datetime.date.today()
    subscribed_today.short_description = u'Inscrito Hoje'
    subscribed_today.boolean = True

admin.site.register(Subscription, SubscriptionAdmin)
