# -*- coding:utf-8 -*-
from django import forms
from django.forms import ModelForm
from models import *

class BlacklistForm(ModelForm):
    class Meta:
        model = Blacklist
        fields = ('did','description',)
    def __init__(self, *args, **kwargs):
        super(BlacklistForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['class'] = "span4"

class ConferenceForm(ModelForm):
    class Meta:
        model = Conference
        fields = ('name','confno', 'pin')

class DeviceForm(ModelForm):
    class Meta:
        model = Devices
        fields = ('description', 'name', 'callerid', 'dialrules_groups', 'lcr', 'pickupgroup', 'host', 'secret', 'port', 'nat',
                  'dnd', 'followme', 'overflow', 'monitor',)
    def __init__(self, *args, **kwargs):
        super(DeviceForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = "span1"
        self.fields['description'].widget.attrs['class'] = "span3"
        self.fields['port'].widget.attrs['class'] = "span1"
        self.fields['followme'].widget.attrs['class'] = "span1"
        self.fields['nat'].widget.attrs['class'] = "span2"


class ProviderForm(ModelForm):
    class Meta:
        model = Providers
        fields = ('description', 'name', 'callerid', 'dialrules_groups', 'rate_groups', 'host', 'port', 'secret', 'register', 'fromuser', 'fromdomain',)
    def __init__(self, *args, **kwargs):
        super(ProviderForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['class'] = "span3"
        self.fields['port'].widget.attrs['class'] = "span1"
        self.fields['secret'].widget.attrs['class'] = "span2"


class QueuesForm(ModelForm):
    class Meta:
        model = Queues
        fields = ('name','description', 'musiconhold')
    def __init__(self, *args, **kwargs):
        super(QueuesForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = "span1"
        self.fields['description'].widget.attrs['class'] = "span3"


class QueueMembersForm(ModelForm):
    interface = forms.ChoiceField(choices=[],)
    paused = forms.BooleanField(required=False)
    class Meta:
        model = QueueMembers
        fields = ('penalty','interface','paused')
    
    def __init__(self, *args, **kwargs):
        super(QueueMembersForm, self).__init__(*args, **kwargs)
        self.fields['penalty'].widget.attrs['class'] = "span1"
        self.fields['interface'].widget.attrs['class'] = "span2"
        self.fields['interface'].choices = Devices.objects.filter(device_type='extension').extra(select={'cod': "'SIP/' || name"}).values_list('cod','name')
        self.fields['interface'].choices.insert(0, ('','---------' ))

class PickupGroupsForm(ModelForm):
    class Meta:
        model = PickupGroups
        fields = ('name',)
        

class LcrForm(ModelForm):
    class Meta:
        model = Lcr
        fields = ('name','order')
        
class LcrProvidersForm(ModelForm):
    class Meta:
        model = LcrProviders
        fields = ('priority','provider','active')
    def __init__(self, *args, **kwargs):
        super(LcrProvidersForm, self).__init__(*args, **kwargs)
        self.fields['priority'].widget.attrs['class'] = "span1"        
        self.fields['provider'].widget.attrs['class'] = "span3"        

class DialrulesGroupsForm(ModelForm):
    class Meta:
        model = DialrulesGroups
        fields = ('name',)

class DialrulesForm(ModelForm):
    class Meta:
        model = Dialrules
        fields = ('name','cut','add','min_len','max_len',)
    def __init__(self, *args, **kwargs):
        super(DialrulesForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = "span3"
        self.fields['cut'].widget.attrs['class'] = "span1"
        self.fields['add'].widget.attrs['class'] = "span1"
        self.fields['min_len'].widget.attrs['class'] = "span1"
        self.fields['max_len'].widget.attrs['class'] = "span1"

class RatesGroupsForm(ModelForm):
    class Meta:
        model = RatesGroups
        fields = ('name',)

class RatesForm(ModelForm):
    class Meta:
        model = Rates
        fields = ('prefix','price','min_time','increment',)
    def __init__(self, *args, **kwargs):
        super(RatesForm, self).__init__(*args, **kwargs)
        self.fields['prefix'].widget.attrs['class'] = "span2"
        self.fields['price'].widget.attrs['class'] = "span1"
        self.fields['min_time'].widget.attrs['class'] = "span1"
        self.fields['increment'].widget.attrs['class'] = "span1"


class InboundRoutesForm(ModelForm):
    class Meta:
        model = InboundRoutes
        fields = ('description','providers','did')
    def __init__(self, *args, **kwargs):
        super(InboundRoutesForm, self).__init__(*args, **kwargs)
        self.fields['providers'].queryset = Providers.objects.filter(device_type='provider')

WEEKDAYS = (
         ('1','Segunda'),
         ('2',u'Terça'),
         ('3','Quarta'),
         ('4','Quinta'),
         ('5','Sexta'),
         ('6',u'Sábado'),
         ('0','Domingo'),
)

class InboundRulesForm(ModelForm):
    weekdays = forms.MultipleChoiceField(label='Dias da Semana',choices=WEEKDAYS, widget=forms.CheckboxSelectMultiple(),)
    destination = forms.ChoiceField(choices=[],label='Desvio')
    class Meta:
        model = InboundRules

    def __init__(self, *args, **kwargs):
        super(InboundRulesForm, self).__init__(*args, **kwargs)
        self.fields['destination'].choices = Devices.objects.filter(device_type='extension').extra(select={'cod': "'Ramal: ' || name"}).values_list('name','cod')
        self.fields['destination'].choices += Queues.objects.extra(select={'cod': "'Fila: ' || description"}).values_list('name','cod')
        self.fields['destination'].widget.attrs['class'] = "span3"
        self.fields['description'].widget.attrs['class'] = "span4"
        self.fields['start'].widget.attrs['class'] = "span1"
        self.fields['stop'].widget.attrs['class'] = "span1"
        self.fields['specific_date'].widget.attrs['class'] = "span1"
