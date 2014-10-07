# -*- coding:utf-8 -*-
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.shortcuts import (render, render_to_response, get_object_or_404, redirect)
from django.forms.models import modelformset_factory
from django.template import RequestContext,loader, Context
from django.core import serializers
from datetime import datetime, timedelta, date, time
from django import forms
from forms import *
from models import *
from django.forms.models import inlineformset_factory
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q

@login_required(login_url='/login/')
def home(request):
    context = {}
    return render(request, 'home.html', context)

def login(request):
    context = {}
    return render(request, 'login.html', context)

def logout(request):
    context = {}
    logout(request)
    return render(request, 'login.html', context)

#######################################################################################
####################################################################################### 

@login_required(login_url='/login/')
def blacklists(request):
    context = {}
    list = Blacklist.objects.all().values('id', 'did','description')
    context['header'] = [u'Número', u'Descrição']
    context['list'] = list
    context['title'] = u'Blacklists'
    return render(request, 'defaultlist.html', context)
 
@login_required(login_url='/login/')
def blacklistsAdicionar(request):
    context = {}
    form = BlacklistForm(request.POST or None)
    form.instance.user = request.user
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect('/blacklists/')

    context = RequestContext(request, {'form': form})
    context['title'] = 'Blacklists'
    context['operation'] = 'Adicionar Blacklist'

    return render_to_response('defaultform.html', context) 

@login_required(login_url='/login/')
def blacklistsEditar(request, id):
    list = Blacklist.objects.get(pk=id)
    if request.method == 'POST':
        form = BlacklistForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/blacklists/')
    else:
        form = BlacklistForm(instance=list)

    context = RequestContext(request, {'form': form, 'id': id})
    context['title'] = 'Blacklists'
    context['operation'] = 'Editar Blacklist #' + id
    return render_to_response('defaultform.html', context)

@login_required(login_url='/login/')
def blacklistsDeletar(request, id):
    list = Blacklist.objects.get(pk=id)
    list.delete()
    return HttpResponseRedirect('/blacklists/')


#######################################################################################
#######################################################################################
@login_required(login_url='/login/')
def conferencias(request):
    context = {}
    list = Conference.objects.all().values('id', 'name','confno')
    context['header'] = ['Nome', u'Descrição']
    context['list'] = list
    context['title'] = u'Salas de Conferência'
    return render(request, 'defaultlist.html', context)

 
@login_required(login_url='/login/')
def conferenciasAdicionar(request):
    form = ConferenceForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.instance.user = request.user
        form.save()
        return HttpResponseRedirect('/conferencias/')
    context = RequestContext(request, {'form': form})
    context['title'] = u'Salas de Conferência'
    context['operation'] = u'Adicionar Sala de Conferência'
    return render_to_response('defaultform.html', context) 


@login_required(login_url='/login/')
def conferenciasEditar(request, id):
    list = Conference.objects.get(pk=id)
    if request.method == 'POST':
        form = ConferenceForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/conferencias/')
    else:
        form = ConferenceForm(instance=list)
    context = RequestContext(request, {'form': form, 'id': id})
    context['title'] = u'Salas de Conferência'
    context['operation'] = u'Editar Sala de Conferência #' + id
    return render_to_response('defaultform.html', context)

@login_required(login_url='/login/')
def conferenciasDeletar(request, id):
    list = Conference.objects.get(pk=id)
    list.delete()
    return HttpResponseRedirect('/conferencias/')


#######################################################################################
#######################################################################################

@login_required(login_url='/login/')
def ramais(request):
    context = {}
    list = Devices.objects.filter(device_type='extension').values('id','name', 'description', 'callerid',)
    context['header'] = ['Descrição', u'CallerID', 'Ramal']
    context['list'] = list
    context['title'] = u'Ramais'
    return render(request, 'defaultlist.html', context)
 
@login_required(login_url='/login/')
def ramaisAdicionar(request):
    form = DeviceForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.instance.user = request.user
        form.save()
        return HttpResponseRedirect('/ramais/')
    
    context = RequestContext(request, {'form': form})
    context['title'] = u'Ramais'
    context['operation'] = u'Adicionar Ramal'
    return render_to_response('extensionsform.html', context) 

@login_required(login_url='/login/')
def ramaisEditar(request, id):
    list = Devices.objects.get(pk=id)
    if request.method == 'POST':
        form = DeviceForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ramais/')
    else:
        form = DeviceForm(instance=list)
    context = RequestContext(request, {'form': form, 'id': id})
    context['title'] = u'Ramais'
    context['operation'] = u'Editar Ramal #' + id
    return render_to_response('extensionsform.html', context)

@login_required(login_url='/login/')
def ramaisDeletar(request, id):
    list = Devices.objects.get(pk=id)
    list.delete()
    return HttpResponseRedirect('/ramais/')


#######################################################################################
#######################################################################################

@login_required(login_url='/login/')
def provedores(request):
    context = {}
    list = Providers.objects.filter(device_type='provider').values('id','name', 'description', 'callerid',)
    context['header'] = ['Descrição', u'CallerID', 'Provedor']
    context['list'] = list
    context['title'] = u'Provedores'
    return render(request, 'defaultlist.html', context)
 
@login_required(login_url='/login/')
def provedoresAdicionar(request):
    form = ProviderForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.instance.user = request.user
        form.save()
        return HttpResponseRedirect('/provedores/')
    
    context = RequestContext(request, {'form': form})
    context['title'] = u'Provedores'
    context['operation'] = u'Adicionar Provedor'
    return render_to_response('providersform.html', context) 

@login_required(login_url='/login/')
def provedoresEditar(request, id):
    list = Providers.objects.get(pk=id)
    if request.method == 'POST':
        form = ProviderForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/provedores/')
    else:
        form = ProviderForm(instance=list)
    context = RequestContext(request, {'form': form, 'id': id})
    context['title'] = u'Provedores'
    context['operation'] = u'Editar Provedor #' + id
    return render_to_response('providersform.html', context)

@login_required(login_url='/login/')
def provedoresDeletar(request, id):
    list = Providers.objects.get(pk=id)
    list.delete()
    return HttpResponseRedirect('/provedores/')


#######################################################################################
#######################################################################################

@login_required(login_url='/login/')
def filas(request):
    context = {}
    list = Queues.objects.all().values('id', 'name','description')
    context['header'] = ['Descrição','Código']
    context['list'] = list
    context['title'] = u'Filas'
    return render(request, 'defaultlist.html', context)
 
@login_required(login_url='/login/')
def filasAdicionar(request):
    form = QueuesForm()
    inline = inlineformset_factory(Queues, QueueMembers, form=QueueMembersForm, extra=5)
    if request.method == 'POST':
        form = QueuesForm(request.POST, request.FILES)
        form.instance.user = request.user
        if form.is_valid():
            instance = form.save()
            formset = inline(request.POST, request.FILES, instance=instance)
            if formset.is_valid():
                formset.save()
                return HttpResponseRedirect('/filas/')
    
    context = RequestContext(request, {'form': form, 'inline' : inline})
    context['title'] = u'Filas'
    context['operation'] = u'Adicionar Fila'
    return render_to_response('queuesform.html', context)

@login_required(login_url='/login/')
def filasEditar(request, id):
    list = Queues.objects.get(pk=id)
    formset = inlineformset_factory(Queues, QueueMembers, form=QueueMembersForm, extra=5)
    form = QueuesForm(instance=list)
    if request.method == 'POST':
        inline = formset(request.POST, instance=list)
        form = QueuesForm(request.POST, instance=list)
        if form.is_valid() and inline.is_valid():
            form.save()
            inline.save()
            return HttpResponseRedirect('/filas/')
    else:
        inline = formset(instance=list)

    context = RequestContext(request, {'form': form, 'inline': inline, 'id': id})
    context['title'] = u'Filas'
    context['operation'] = u'Editar Fila #' + id
    return render_to_response('queuesform.html', context)

@login_required(login_url='/login/')
def filasDeletar(request, id):
    list = Queues.objects.get(pk=id)
    list.delete()
    return HttpResponseRedirect('/filas/')

#######################################################################################
#######################################################################################
@login_required(login_url='/login/')
def gruposcaptura(request):
    context = {}
    list = PickupGroups.objects.all().values('id','name')
    context['header'] = [u'Descrição']
    context['list'] = list
    context['title'] = u'Grupos de Captura'
    return render(request, 'defaultlist.html', context)
 
@login_required(login_url='/login/')
def gruposcapturaAdicionar(request):
    context = {}
    form = PickupGroupsForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        form.instance.user = request.user
        form.save()
        return HttpResponseRedirect('/gruposcaptura/')

    context = RequestContext(request, {'form': form})
    context['title'] = 'Grupos de Captura'
    context['operation'] = 'Adicionar Grupo de Captura'

    return render_to_response('defaultform.html', context) 

@login_required(login_url='/login/')
def gruposcapturaEditar(request, id):
    list = PickupGroups.objects.get(pk=id)
    if request.method == 'POST':
        form = PickupGroupsForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/gruposcaptura/')
    else:
        form = PickupGroupsForm(instance=list)

    context = RequestContext(request, {'form': form, 'id': id})
    context['title'] = 'Grupos de Captura'
    context['operation'] = 'Editar Grupo de Captura #' + id
    return render_to_response('defaultform.html', context)

@login_required(login_url='/login/')
def gruposcapturaDeletar(request, id):
    list = PickupGroups.objects.get(pk=id)
    list.delete()
    return HttpResponseRedirect('/gruposcaptura/')


#######################################################################################
#######################################################################################
@login_required(login_url='/login/')
def lcrs(request):
    context = {}
    list = Lcr.objects.all().values('id', 'name')
    context['header'] = ['Descrição']
    context['list'] = list
    context['title'] = u'Rotas de Saída'
    return render(request, 'defaultlist.html', context)
 
@login_required(login_url='/login/')
def lcrsAdicionar(request):
    form = LcrForm()
    inline = inlineformset_factory(Lcr, LcrProviders, form=LcrProvidersForm, extra=5)
    if request.method == 'POST':
        form = LcrForm(request.POST, request.FILES)
        form.instance.user = request.user        
        if form.is_valid():
            instance = form.save()
            formset = inline(request.POST, request.FILES, instance=instance)
            if formset.is_valid():
                formset.save()
                return HttpResponseRedirect('/lcrs/')

    context = RequestContext(request, {'form': form, 'inline' : inline})
    context['title'] = u'Rotas de Saída'
    context['operation'] = u'Adicionar Rota de Saída'
    return render_to_response('lcrsform.html', context) 

@login_required(login_url='/login/')
def lcrsEditar(request, id):
    list = Lcr.objects.get(pk=id)
    formset = inlineformset_factory(Lcr, LcrProviders, form=LcrProvidersForm, extra=5)
    form = LcrForm(instance=list)
    
    if request.method == 'POST':
        #return HttpResponse(request.POST.lists())
        
        inline = formset(request.POST, instance=list)
        form = LcrForm(request.POST, instance=list)
        if form.is_valid() and inline.is_valid():                    
            form.save()
            inline.save()
            
            return HttpResponseRedirect('/lcrs/')
    else:
        inline = formset(instance=list)
        
    context = RequestContext(request, {'form': form, 'inline': inline, 'id': id})
    context['title'] = u'Rotas de Saída'
    context['operation'] = u'Editar Rota de Saída #' + id
    return render_to_response('lcrsform.html', context)

@login_required(login_url='/login/')
def lcrsDeletar(request, id):
    list = Lcr.objects.get(pk=id)
    list.delete()
    return HttpResponseRedirect('/lcrs/')

#######################################################################################
#######################################################################################

@login_required(login_url='/login/')
def regrasdiscagem(request):
    context = {}
    list = DialrulesGroups.objects.all().values('id', 'name')
    context['header'] = ['Descrição']
    context['list'] = list
    context['title'] = u'Regras de Discagem'
    return render(request, 'defaultlist.html', context)
 
@login_required(login_url='/login/')
def regrasdiscagemAdicionar(request):
    form = DialrulesGroupsForm()
    inline = inlineformset_factory(DialrulesGroups, Dialrules, form=DialrulesForm, extra=5)

    if request.method == 'POST':
        form = DialrulesGroupsForm(request.POST, request.FILES)
        form.instance.user = request.user
        if form.is_valid():
            instance = form.save()
            formset = inline(request.POST, request.FILES, instance=instance)
            if formset.is_valid():
                formset.save()
                return HttpResponseRedirect('/regrasdiscagem/')
    
    context = RequestContext(request, {'form': form, 'inline' : inline})
    context['title'] = u'Regras de Discagem'
    context['operation'] = u'Adicionar Regra'
    return render_to_response('dialrulesform.html', context)

@login_required(login_url='/login/')
def regrasdiscagemEditar(request, id):

    list = DialrulesGroups.objects.get(pk=id)
    formset = inlineformset_factory(DialrulesGroups, Dialrules, form=DialrulesForm, extra=5)
    form = DialrulesGroupsForm(instance=list)
    
    if request.method == 'POST':
        inline = formset(request.POST, instance=list)
        form = DialrulesGroupsForm(request.POST, instance=list)
        if form.is_valid() and inline.is_valid():                    
            form.save()
            inline.save()
            
            return HttpResponseRedirect('/regrasdiscagem/')
    else:
        inline = formset(instance=list)

    context = RequestContext(request, {'form': form, 'inline': inline, 'id': id})
    context['title'] = u'Regras de Discagem'
    context['operation'] = u'Editar Regra #' + id
    return render_to_response('dialrulesform.html', context)

@login_required(login_url='/login/')
def regrasdiscagemDeletar(request, id):
    list = DialrulesGroups.objects.get(pk=id)
    list.delete()
    return HttpResponseRedirect('/regrasdiscagem/')


#######################################################################################
#######################################################################################
@login_required(login_url='/login/')
def tarifas(request):
    context = {}
    list = RatesGroups.objects.all().values('id', 'name',)
    context['header'] = [u'Descrição']
    context['list'] = list
    context['title'] = u'Tarifas'
    return render(request, 'defaultlist.html', context)
 
@login_required(login_url='/login/')
def tarifasAdicionar(request):
    form = RatesGroupsForm()
    inline = inlineformset_factory(RatesGroups, Rates, form=RatesForm, extra=5)

    if request.method == 'POST':
        form = RatesGroupsForm(request.POST, request.FILES)
        form.instance.user = request.user
        if form.is_valid():
            instance = form.save()
            formset = inline(request.POST, request.FILES, instance=instance)
            if formset.is_valid():
                formset.save()
                return HttpResponseRedirect('/tarifas/')
    
    context = RequestContext(request, {'form': form, 'inline' : inline})
    context['title'] = u'Tarifas'
    context['operation'] = u'Adicionar Tarifa'
    return render_to_response('ratesform.html', context) 

@login_required(login_url='/login/')
def tarifasEditar(request, id):
    list = RatesGroups.objects.get(pk=id)
    formset = inlineformset_factory(RatesGroups, Rates, form=RatesForm, extra=5)
    form = RatesGroupsForm(instance=list)
    
    if request.method == 'POST':
        inline = formset(request.POST, instance=list)
        form = RatesGroupsForm(request.POST, instance=list)
        if form.is_valid() and inline.is_valid():                    
            form.save()
            inline.save()
            
            return HttpResponseRedirect('/tarifas/')
    else:
        inline = formset(instance=list)
        
    context = RequestContext(request, {'form': form, 'inline': inline, 'id': id})
    context['title'] = u'Tarifas'
    context['operation'] = u'Editar Tarifa #' + id
    return render_to_response('ratesform.html', context)

@login_required(login_url='/login/')
def tarifasDeletar(request, id):
    list = Rates.objects.get(pk=id)
    list.delete()
    return HttpResponseRedirect('/tarifas/')

#######################################################################################
#######################################################################################

@login_required(login_url='/login/')
def rotasentrada(request):
    context = {}
    list = InboundRoutes.objects.all().values('id', 'did', 'description',)
    context['header'] = [u'Número (DID)','Descrição','Regras']
    context['list'] = list
    context['title'] = u'Rota de Entrada'
    return render(request, 'inboundrouteslist.html', context)
 
@login_required(login_url='/login/')
def rotasentradaAdicionar(request):
    form = InboundRoutesForm()
    inline = {}
    if request.method == 'POST':
        form = InboundRoutesForm(request.POST, request.FILES)
        form.instance.user = request.user
        if form.is_valid():
            instance = form.save()
            return HttpResponseRedirect('/rotasentrada/')
    
    context = RequestContext(request, {'form': form, 'inline' : inline})
    context['title'] = u'Rota de Entrada'
    context['operation'] = u'Adicionar Rota de Entrada'
    return render_to_response('inboundroutesform.html', context) 

@login_required(login_url='/login/')
def rotasentradaEditar(request, id):
    list = InboundRoutes.objects.get(pk=id)
    if request.method == 'POST':
        form = InboundRoutesForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rotasentrada/')
    else:
        form = InboundRoutesForm(instance=list)

    context = RequestContext(request, {'form': form, 'id': id})
    context['title'] = 'Rotas de Entrada'
    context['operation'] = 'Editar Rota de Entrada #' + id
    return render_to_response('inboundroutesform.html', context)

@login_required(login_url='/login/')
def rotasentradaDeletar(request, id):
    list = InboundRoutes.objects.get(pk=id)
    list.delete()
    return HttpResponseRedirect('/rotasentrada/')


#######################################################################################
#######################################################################################

@login_required(login_url='/login/')
def regrasentrada(request, id):
    context = {}
    list = InboundRules.objects.all().values('id', 'description','destination').filter(inbound_routes=id)
    context['header'] = [u'Desvio', 'Descrição',]
    context['list'] = list
    context['id'] = id
    context['title'] = u'Regras de Entrada'
    return render(request, 'inboundruleslist.html', context)

@login_required(login_url='/login/')
def regrasentradaAdicionar(request, id):
    context = {}
    form = InboundRulesForm(request.POST or None, initial={'inbound_routes': id})
    
    if request.method == 'POST' and form.is_valid():
        form.instance.user = request.user
        form.save()
        return HttpResponseRedirect('/regrasentrada/' + id)

    context = RequestContext(request, {'form': form, 'id': id})
    context['title'] = 'Regras de Entrada'
    context['operation'] = 'Adicionar Regra de Entrada'
    return render_to_response('inboundrulesform.html', context) 

@login_required(login_url='/login/')
def regrasentradaEditar(request, id):
    list = InboundRules.objects.get(pk=id)
    if request.method == 'POST':
        form = InboundRulesForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/regrasentrada/' + list.inbound_routes.id.__str__())
    else:
        form = InboundRulesForm(instance=list)

    context = RequestContext(request, {'form': form, 'id': id})
    context['title'] = 'Regras de Entrada'
    context['operation'] = 'Editar Regra de Entrada #' + id
    return render_to_response('inboundrulesform.html', context)

@login_required(login_url='/login/')
def regrasentradaDeletar(request, rid, id):
    list = InboundRules.objects.get(pk=id)
    list.delete()
    return HttpResponseRedirect('/regrasentrada/' + rid)

#######################################################################################
#######################################################################################


@login_required(login_url='/login/')
def report(request):
    context = {}
    return render(request, 'reportform.html', context)

@login_required(login_url='/login/')
def reportResults(request):
    context = {}
    cdr = {}
    cdrQueue = {}
    template_name = 'report.html'

    if request.POST:
        request.session['qs'] = request.POST

    postData = request.session['qs']

    ''' CDR QUERY '''
    
    args = []
    if (postData['initdate'] != ''):
        args.append(Q(calldate__gte = datetime.strptime(postData['initdate'], '%d/%m/%Y %H:%M:%S')),)
        context['initdate'] = postData['initdate']
    else:
        args.append(Q(calldate__gte = date.today()),)
        context['initdate'] = str(date.today())
            
    if (postData['enddate'] != ''):
        args.append(Q(calldate__lte = datetime.strptime(postData['enddate'], '%d/%m/%Y %H:%M:%S')),)
        context['enddate'] = postData['enddate']     

    if (postData['origin'] != ''):
        args.append(Q(origin__contains = postData['origin']))     

    if (postData['destination'] != ''):
        args.append(Q(destination__contains = postData['destination']))     

    if (postData['forward'] != ''):
        args.append(Q(forward__contains = postData['forward']))     

    if (postData['call_type'] == '1'):
        args.append(Q(call_type__contains = 'Outbound'))     

    if (postData['call_type'] == '2'):
        args.append(Q(call_type__contains = 'Inbound'))

    if (postData['call_type'] == '3'):
        args.append(Q(call_type__contains = 'Internal'))
        
    cdr = Report.objects.filter(*args)
    #return HttpResponse(cdr.query)
    
    ''' END QUERY CDR '''    
    
    for obj in cdr:
        obj.duration = str(timedelta(seconds=obj.duration))

        if (obj.duration_billing != None):
            obj.duration_billing = str(timedelta(seconds=obj.duration_billing))
        else:
            obj.duration_billing = '-'
        
        if (obj.agent == None):
            obj.agent = '-'
            
        if (obj.value == None):
            obj.value = '-'
            
        if (obj.provider == None):
            obj.provider = '-'
            
        ''' SEARCH RESULTS QUEUE LOG '''
            
        if 'Queue' in obj.observation:
            argsQueue = []
            argsQueue.append(Q(callid__contains = obj.uniqueid))
            argsQueue.append(Q(time__gte = obj.calldate))
            argsQueue.append(Q(time__lte = (obj.calldate + timedelta(minutes=20))))
            cdrQueue = QueueLog.objects.filter(*argsQueue)
            
            for objFila in cdrQueue:
                
                if objFila.event == 'ENTERQUEUE':
                    objFila.event = u'INICIO'
                    objFila.agent = ''
                
                if objFila.event == 'TRANSFER':
                    objFila.event = u'TRANSFERÊNCIA'
                    
                if objFila.event == 'RINGNOANSWER':
                    objFila.event = 'SEM RESPOSTA'
                    
                if objFila.event == 'EXITWITHTIMEOUT':
                    objFila.event = 'TEMPO EXPIRADO'
                    objFila.agent = ''
                    
                if objFila.event == 'CONNECT':
                    objFila.event = 'CONECTADO'
                
                if objFila.event == 'COMPLETECALLER':
                    objFila.event = 'COMPLETADA'
                        
                if objFila.event == 'ABANDON':
                    objFila.event = u'LIGAÇÃO DESCONECTADA'
                    objFila.agent = ''
                
            obj.cdrQueue = cdrQueue

    ''' END - RESULTS QUEUE LOG '''
    context['cdr'] = cdr

    '''

    EXPORT CSV FILE
    
    '''
    if 'csv' in request.GET:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="relatorio.csv"'
        template_name = 'csv.html'
        t = loader.get_template('csv.html')
        c = Context({
            'cdr': cdr,
            })
        response.write(t.render(c))
        return response
    
    '''
    END - EXPORT CSV
    '''
    
    return render(request, template_name, context)
#######################################################################################
####################################################################################### 

@login_required(login_url='/login/')
def chamadasativas(request):
    context = {}
    list = ActiveCalls.objects.all().values('id', 'calldate','origin', 'destination')
    context['list'] = list
    context['id'] = id
    return render(request, 'activecalls.html', context)