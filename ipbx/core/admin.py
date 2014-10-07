# -*- coding: utf-8 -*-

from ipbx.core.models import *
from ipbx.core.views import *
from django.contrib import admin

class BlacklistAdmin(admin.ModelAdmin):
    #exclude = ('user',)
    list_display = ('did', 'description')
    list_filter = ('did', 'description')
    search_fields = ['did', 'description']
    
class ConferenceAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_filter = ('id', 'confno', 'name')
    search_fields = ['id', 'confno', 'name']
    
    fieldsets = (
        ('', {
            'fields': ['name',('confno', 'pin'),],
        }),
        (u'Avançado', {
            'classes': ('collapse closed',),
            'fields' : (('starttime','endtime'), 'opts', 'adminpin', 'adminopts', 'members','maxusers')
            },
         ),
        )

class ExtensionsAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    classes = ('collapse closed',)
    fieldsets = (
        ('', {
            'fields': ['description', 'name', 'callerid', 'dialrules_groups', 'lcr', 'pickupgroup', ('host', 'port'), 'secret'],
        }),
        (u'Mais configurações', {
            'classes': ('collapse closed',),
            'fields': ('nat',
                       'dnd', 'followme', 'followme_busy', 'followme_noanswer', 'overflow',
                        'monitor', 'force_monitor', 'mailbox',),
        }),
        (u'Avançado', {
            'classes': ('collapse closed',),
            'fields' : ('accountcode', 'amaflags', 'callgroup', 'canreinvite', 'context', 'defaultip', 'dtmfmode', 'fromuser', 'fromdomain', 'insecure',
                        'language', 'md5secret', 'permit', 'deny', 'mask', 'qualify', 'restrictcid', 'rtptimeout', 'rtpholdtimeout', 'type',
                        'allow', 'musiconhold', 'regseconds', 'ipaddr', 'regexten', 'cancallforward', 'lastms', 'defaultuser', 'fullcontact', 'regserver', 'useragent',
                        'callbackextension', 'rtcachefriends', 'rtautoclear'),
        }),
                 
    )
  
    list_display = ('name', 'host','callerid','dialrules_groups','lcr','pickupgroup')
    list_filter = ('name', 'host','callerid','dialrules_groups','lcr','pickupgroup')
    search_fields = ['name', 'host','callerid','dialrules_groups','lcr','pickupgroup']
    
    def queryset(self, request):
        qs = super(ExtensionsAdmin, self).queryset(request)
        return qs.filter(device_type='extension')

class ProvidersAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    classes = ('collapse closed',)
    fieldsets = (
        ('', {
            'fields': ['description', 'name', 'callerid', 'dialrules_groups', 'rate_groups', ('host', 'port'), 'secret', 'register', ('fromuser', 'fromdomain',)],
        }),
        (u'Avançado', {
            'classes': ('collapse closed',),
            'fields' : ('nat', 'accountcode', 'amaflags', 'canreinvite', 'context', 'defaultip', 'dtmfmode', 'insecure',
                        'language', 'md5secret', 'permit', 'deny', 'mask', 'qualify', 'restrictcid', 'rtptimeout', 'rtpholdtimeout', 'type',
                        'allow', 'musiconhold', 'regseconds', 'ipaddr', 'regexten', 'cancallforward', 'lastms', 'defaultuser', 'fullcontact', 'regserver', 'useragent',
                        'callbackextension', 'rtcachefriends', 'rtautoclear'),
        }),
                 
    )
  
    list_display = ('description','name', 'host','callerid','dialrules_groups','lcr','pickupgroup')
    list_filter = ('description','name', 'host','callerid','dialrules_groups','lcr','pickupgroup')
    search_fields = ['description','name', 'host','callerid','dialrules_groups','lcr','pickupgroup']
    readonly_fields = ['name',]
    
#    def queryset(self, request):
#        qs = super(ProvidersAdmin, self).queryset(request)
#        return qs.filter(device_type='provider')

class LcrProvidersAdmin(admin.TabularInline):
    model = LcrProviders
    sortable_field_name = 'priority'
    fieldsets = (
        ('', {
            'fields': ['lcr', 'provider', 'active', 'priority'],
        }),
    )
    
class LcrAdmin(admin.ModelAdmin):
    inlines = [LcrProvidersAdmin,]
    readonly_fields = ('id',)
    #exclude = ('user',)
    list_display = ('name', 'order')
    list_filter = ('name', 'order')
    search_fields = ['name', 'order']
        

class DialrulesAdmin(admin.TabularInline):
    model = Dialrules    

class DialrulesGroupsAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_filter = ['name']
    #exclude = ('user',)
    search_fields = ['name']
    list_display = ['name']
    inlines = [DialrulesAdmin,]

class RatesAdmin(admin.TabularInline):
    model = Rates
    
class RatesGroupsAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_filter = ['name']
    #exclude = ('user',)
    search_fields = ['name']
    list_display = ['name']
    inlines = [RatesAdmin,]
    
class PickupGroupsAdmin(admin.ModelAdmin):
    #exclude = ('user',)
    pass

class QueuesMembersAdmin(admin.TabularInline):
    model = QueueMembers
    sortable_field_name = 'penalty'
    fieldsets = (
        ('', {
            'fields': ['interface', 'penalty',],
        }),
    )
    
    
class QueuesAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    classes = ('collapse closed',)
    fieldsets = (
        ('', {
            'fields': ['name', 'description', 'musiconhold'],
        }),
        (u'Avançado', {
            'classes': ('collapse closed',),
            'fields' : ('announce', 'context', 'timeout', 'monitor_join', 'monitor_format', 'queue_youarenext', 'queue_thereare', 'queue_callswaiting', 'queue_holdtime', 'queue_minutes',
                        'queue_seconds', 'queue_lessthan', 'queue_reporthold', 'announce_frequency', 'announce_round_seconds', 'announce_holdtime', 'retry', 'wrapuptime', 'maxlen', 'servicelevel',
                        'strategy', 'joinempty', 'leavewhenempty', 'eventmemberstatus', 'eventwhencalled', 'reportholdtime', 'memberdelay', 'weight', 'timeoutrestart', 'setinterfacevar'),
        }),
                 
    )
  
    list_display = ('name', 'description',)
    list_filter = ('name', 'description',)
    search_fields = ['name', 'description',]
    inlines = [QueuesMembersAdmin,]
    
    def get_readonly_fields(self, request, obj = None):
        if obj: #In edit mode
            return ('name',) + self.readonly_fields
        return self.readonly_fields
    

class ReportAdmin(admin.ModelAdmin):
    list_filter = ['exten_description', 'origin','extension','destination','forward','status','duration','duration_billing','calldate','provider','name','value','call_type','observation','uniqueid','uri']
    search_fields = ['exten_description', 'origin','extension','destination','forward','status','duration','duration_billing','calldate','provider','name','value','call_type','observation','uniqueid','uri']
    actions = None
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):        
        pass
admin.site.register(Blacklist, BlacklistAdmin)
admin.site.register(Conference, ConferenceAdmin)
admin.site.register(Devices, ExtensionsAdmin)
admin.site.register(Providers, ProvidersAdmin)
admin.site.register(Lcr, LcrAdmin)
admin.site.register(Queues, QueuesAdmin)
admin.site.register(DialrulesGroups,DialrulesGroupsAdmin)
admin.site.register(RatesGroups,RatesGroupsAdmin)
admin.site.register(PickupGroups,PickupGroupsAdmin)
admin.site.register(Report, ReportAdmin)
