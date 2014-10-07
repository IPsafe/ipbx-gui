# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import random

class Blacklist(models.Model):
    user = models.ForeignKey(User)
    did = models.CharField(u'Número', max_length=30, blank=False, null=False)
    description = models.CharField(u'Descrição', max_length=255, blank=False, null=False)
    class Meta:
        db_table = 'blacklist'
        verbose_name = u"Blacklist (Números Bloqueados)"
        verbose_name_plural = u"Blacklist (Números Bloqueados)"
    def __unicode__(self):
        return self.did
    
class Conference(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(verbose_name=u'Descrição',max_length=80,null=False,blank=False)
    confno = models.CharField(verbose_name=u'Código', max_length=80,unique=True, blank=False, null=False)
    starttime = models.DateTimeField(verbose_name=u'Horário Início',null=True, blank=True)
    endtime = models.DateTimeField(verbose_name=u'Horário Fim',null=True, blank=True)
    pin = models.CharField(verbose_name=u'Senha',max_length=20, null=True, blank=True)
    opts = models.CharField(verbose_name=u'OPTS',max_length=100, null=True, blank=True)
    adminpin = models.CharField(verbose_name=u'Admin PIN', null=True, max_length=20, blank=True)
    adminopts = models.CharField(verbose_name=u'Admin OPTS',null=True, max_length=100, blank=True)
    members = models.IntegerField(verbose_name=u'Membros',null=True, blank=True)
    maxusers = models.IntegerField(verbose_name=u'Máximo de participantes',null=True, blank=True)
    class Meta:
        db_table = 'conference'
        verbose_name = u"Sala de Conferência"
        verbose_name_plural = u"Salas de Conferências"
    def __unicode__(self):
        return self.name
    
class Dayoff(models.Model):
    user = models.ForeignKey(User)
    day = models.IntegerField(null=True, blank=True)
    month = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    area_id = models.IntegerField()
    active = models.BooleanField()
    description = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'dayoff'

class DayoffArea(models.Model):
    
    area_type = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'dayoff_area'

NAT = (
    ('no', 'Desabilitado'),
    ('force_rport,comedia', 'Habilitado'),
    ('', '---------'),
    ('force_rport', 'Force RPort'),
    ('auto_force_rport', 'Auto-Force RPort'),
    ('comedia', 'Comedia'),
    ('auto_comedia', 'Auto Comedia'),
)

class Devices(models.Model):
    user = models.ForeignKey(User)
    lcr = models.ForeignKey('Lcr', null=True, blank=True,verbose_name='Rota de Saida')
    dialrules_groups = models.ForeignKey('DialrulesGroups', null=True, blank=True,verbose_name='Regras de Discagem')
    rate_groups = models.ForeignKey('RatesGroups', null=True, blank=True,verbose_name='Tarifas')
    name = models.CharField('Ramal',max_length=80,unique=True,blank=False,null=False)
    description = models.CharField(u'Descrição',max_length=80,null=False,blank=False)
    device_type = models.CharField(max_length=20, blank=True,default='extension')
    register = models.BooleanField(u'Enviar register(?)',null=False, blank=True)
    accountcode = models.CharField(max_length=20, null=True)
    amaflags = models.CharField(max_length=7, null=True)
    callgroup = models.CharField(max_length=10, null=True,default='1')
    callerid = models.CharField(u'CallerID',max_length=80, null=True)
    canreinvite = models.CharField(max_length=3, null=True)
    context = models.CharField(max_length=80, null=True,default='default')
    defaultip = models.CharField(max_length=15, null=True)
    dtmfmode = models.CharField(max_length=7, null=True,default='rfc2833')
    fromuser = models.CharField(max_length=80, null=True)
    fromdomain = models.CharField(max_length=80, null=True)
    host = models.CharField(max_length=31, blank=True,default='dynamic')
    insecure = models.CharField(max_length=20, null=True)
    language = models.CharField(max_length=2, null=True,default='br')
    mailbox = models.CharField('Caixa de Mensagens',max_length=50, null=True)
    md5secret = models.CharField(max_length=80, null=True)
    nat = models.CharField('NAT',max_length=20, null=True,default='force_rport,comedia',choices=NAT)
    permit = models.CharField(max_length=95, null=True)
    deny = models.CharField(max_length=95, null=True)
    mask = models.CharField(max_length=95, null=True)
    pickupgroup = models.ForeignKey('PickupGroups', null=True, db_column='pickupgroup', blank=True,verbose_name='Grupo de Captura')
    port = models.CharField('Porta',max_length=5, null=True,default='5060')
    qualify = models.CharField(max_length=20, null=True)
    restrictcid = models.CharField(max_length=10, null=True)
    rtptimeout = models.CharField(max_length=3, null=True)
    rtpholdtimeout = models.CharField(max_length=3, null=True)
    secret = models.CharField('Senha',max_length=80, null=True)
    type = models.CharField(max_length=30, null=True,default='friend')
    allow = models.CharField(max_length=200, null=True,default='alaw,ulaw,g729')
    musiconhold = models.CharField(max_length=100, null=True)
    regseconds = models.IntegerField(null=True)
    ipaddr = models.CharField(max_length=45, null=True)
    regexten = models.CharField(max_length=80, null=True)
    cancallforward = models.CharField(max_length=3, null=True)
    lastms = models.IntegerField(null=True)
    defaultuser = models.CharField(max_length=80, null=True)
    fullcontact = models.CharField(max_length=80, null=True)
    regserver = models.CharField(max_length=30, null=True)
    useragent = models.CharField(max_length=40, null=True)
    callbackextension = models.CharField(max_length=40, null=True)
    dnd = models.BooleanField(u'Não perturbe',null=False,blank=True)
    followme = models.CharField('Siga-me',max_length=30, null=True, blank=True)
    followme_busy = models.CharField('Siga-me Ocupado',max_length=30, null=True)
    followme_noanswer = models.CharField(u'Siga-me Não Atende',max_length=30, null=True)
    overflow = models.CharField('Transbordo',max_length=30, null=True,blank=True)
    monitor = models.BooleanField(u'Gravação',null=False, blank=True)
    force_monitor = models.BooleanField(u'Forçar gravação',null=False, blank=True)
    rtcachefriends = models.CharField(max_length=30, null=True,default='yes')
    rtautoclear = models.CharField(max_length=30, null=True,default='no')
    class Meta:
        db_table = 'devices'
        verbose_name = u"Ramal"
        verbose_name_plural = u"Ramais"
    def __unicode__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.mailbox = self.name
        super(Devices, self).save(*args, **kwargs)

class Providers(models.Model):
    user = models.ForeignKey(User)
    lcr = models.ForeignKey('Lcr', null=True, blank=True,verbose_name='Rota de Saida')
    dialrules_groups = models.ForeignKey('DialrulesGroups', null=True, blank=True,verbose_name='Regras de Discagem')
    rate_groups = models.ForeignKey('RatesGroups', null=True, blank=True,verbose_name='Tarifas')
    name = models.CharField(u'Usuário de Autenticação',max_length=80,unique=True,blank=False,null=False)
    description = models.CharField(u'Descrição',max_length=80,null=False,blank=False,unique=True)
    device_type = models.CharField(max_length=20, blank=True,default='provider')
    register = models.BooleanField(u'Enviar register(?)',null=False, blank=True)
    accountcode = models.CharField(max_length=20, blank=True)
    amaflags = models.CharField(max_length=7, blank=True)
    callgroup = models.CharField(max_length=10, blank=True,default='1')
    callerid = models.CharField(u'CallerID',max_length=80, blank=True)
    canreinvite = models.CharField(max_length=3, blank=True)
    context = models.CharField(max_length=80, blank=True,default='provider')
    defaultip = models.CharField(max_length=15, blank=True)
    dtmfmode = models.CharField(max_length=7, blank=True,default='rfc2833')
    fromuser = models.CharField(max_length=80, blank=True, verbose_name='From User')
    fromdomain = models.CharField(max_length=80, blank=True,verbose_name='From Domain')
    host = models.CharField(max_length=31, blank=True,default='dynamic')
    insecure = models.CharField(max_length=20, blank=True)
    language = models.CharField(max_length=2, blank=True,default='br')
    mailbox = models.CharField('Caixa de Mensagens',max_length=50, null=True)
    md5secret = models.CharField(max_length=80, blank=True)
    nat = models.CharField('NAT',max_length=5, blank=True,null=True,default='no',choices=NAT)
    permit = models.CharField(max_length=95, blank=True)
    deny = models.CharField(max_length=95, blank=True)
    mask = models.CharField(max_length=95, blank=True)
    pickupgroup = models.ForeignKey('PickupGroups', null=True, db_column='pickupgroup', blank=True,verbose_name='Grupo de Captura')
    port = models.CharField('Porta',max_length=5, blank=True,default='5060')
    qualify = models.CharField(max_length=20, blank=True)
    restrictcid = models.CharField(max_length=10, blank=True)
    rtptimeout = models.CharField(max_length=3, blank=True)
    rtpholdtimeout = models.CharField(max_length=3, blank=True)
    secret = models.CharField('Senha',max_length=80, null=True)
    type = models.CharField(max_length=30, blank=True,default='peer')
    allow = models.CharField(max_length=200, blank=True,default='alaw,ulaw,g729')
    musiconhold = models.CharField(max_length=100, blank=True)
    regseconds = models.IntegerField(null=True, blank=True)
    ipaddr = models.CharField(max_length=45, blank=True)
    regexten = models.CharField(max_length=80, blank=True)
    cancallforward = models.CharField(max_length=3, blank=True)
    lastms = models.IntegerField(null=True, blank=True)
    defaultuser = models.CharField(max_length=80, blank=True)
    fullcontact = models.CharField(max_length=80, blank=True)
    regserver = models.CharField(max_length=30, blank=True)
    useragent = models.CharField(max_length=40, blank=True)
    callbackextension = models.CharField(max_length=40, blank=True)
    dnd = models.BooleanField(u'Não perturbe',null=False, blank=True)
    followme = models.CharField('Siga-me',max_length=30, blank=True)
    followme_busy = models.CharField('Siga-me Ocupado',max_length=30, blank=True)
    followme_noanswer = models.CharField(u'Siga-me Não Atende',max_length=30, blank=True)
    overflow = models.CharField('Transbordo',max_length=30, blank=True)
    monitor = models.BooleanField(u'Gravação',null=False, blank=True)
    force_monitor = models.BooleanField(u'Forçar gravação',null=False, blank=True)
    rtcachefriends = models.CharField(max_length=30, blank=True,default='yes')
    rtautoclear = models.CharField(max_length=30, blank=True,default='no')
    class Meta:
        db_table = 'devices'
        verbose_name = u"Provedor"
        verbose_name_plural = u"Provedores"
        managed = False
        
    def __unicode__(self):
        return self.description

    def save(self, *args, **kwargs):
        self.defaultuser = self.fromuser
        super(Providers, self).save(*args, **kwargs)


class Dialrules(models.Model):
    
    dialrules_groups = models.ForeignKey('DialrulesGroups')
    name = models.CharField('Nome',max_length=100,unique=True,blank=False,null=False)
    cut = models.CharField('Cortar',max_length=100, blank=True)
    add = models.CharField('Adicionar',max_length=100, blank=True)
    min_len = models.IntegerField(u'Mínimo de dígitos',null=False, blank=False)
    max_len = models.IntegerField(u'Máximo de dígitos',null=False, blank=False)
    class Meta:
        db_table = 'dialrules'
        verbose_name = u"Regras de Discagem"
        verbose_name_plural = u"Regras de Discagem"
    def __unicode__(self):
        return self.name

class DialrulesGroups(models.Model):
    
    name = models.CharField('Nome',max_length=100,unique=True,blank=False,null=False)
    user = models.ForeignKey(User)
    class Meta:
        db_table = 'dialrules_groups'
        verbose_name = u"Regras de Discagem"
        verbose_name_plural = u"Regras de Discagem"
    def __unicode__(self):
        return self.name
    
class ExtensionsConf(models.Model):
    context = models.CharField(max_length=20)
    exten = models.CharField(max_length=20)
    priority = models.IntegerField()
    app = models.CharField(max_length=20)
    appdata = models.CharField(max_length=128, blank=True)
    class Meta:
        db_table = 'extensions_conf'

class InboundRoutes(models.Model):
    user = models.ForeignKey(User)
    description = models.CharField(max_length=255, blank=False,null=False,verbose_name=u'Descrição')
    providers = models.ForeignKey(Providers,verbose_name='Provedor',null=False, blank=False,limit_choices_to = {'device_type': 'provider'})
    area_id = models.IntegerField(verbose_name='Provedor', default=0)
    did = models.CharField(max_length=25,unique=True,verbose_name=u'Número de Entrada (DID)',null=False, blank=False)
    class Meta:
        db_table = 'inbound_routes'
        verbose_name = u"Regra de Entrada"
        verbose_name_plural = u"Regras de Entrada"
    def __unicode__(self):
        return self.description

WEEKDAYS = (
         ('0','Segunda'),
         ('1',u'Terça'),
         ('2','Quarta'),
         ('3','Quinta'),
         ('4','Sexta'),
         ('5',u'Sábado'),
         ('6','Domingo'),
)

class InboundRules(models.Model):
    inbound_routes = models.ForeignKey(InboundRoutes,verbose_name='Rota de Entrada',null=False, blank=False)
    description = models.CharField(max_length=255,verbose_name=u'Descrição',null=False, blank=False)
    destination = models.CharField(max_length=25, verbose_name=u'Desvio',null=False, blank=False)
    weekdays = models.CharField(max_length=80, blank=True,verbose_name=u'Dias da Semana',)
    start = models.TimeField(null=False, blank=False,verbose_name=u'Início',default='00:00:00',)
    stop = models.TimeField(null=False, blank=False,verbose_name=u'Fim',default='23:59:59',)
    dayoff = models.BooleanField(null=False, blank=True,verbose_name=u'Feriados')
    specific_date = models.DateField(null=True, blank=True,verbose_name=u'Data Específica')
    class Meta:
        db_table = 'inbound_rules'


TITLE_CHOICES = (
    ('priority', 'Prioridade'),
    ('price', 'Custo'),
)

class Lcr(models.Model):
    name = models.CharField('Nome',max_length=80,unique=True,blank=False,null=False)
    order = models.CharField('Ordem',max_length=40, blank=False,null=False,choices=TITLE_CHOICES)
    user = models.ForeignKey(User)
    class Meta:
        db_table = 'lcr'
        verbose_name = u"LCR - Rota de Saida"
        verbose_name_plural = u"LCR - Rotas de Saida"
    def __unicode__(self):
        return self.name

class LcrProviders(models.Model):
    
    lcr = models.ForeignKey(Lcr, null=False, blank=False)
    provider = models.ForeignKey(Providers,verbose_name='Provedor',limit_choices_to = {'device_type': 'provider'},null=False, blank=False)
    active = models.BooleanField(verbose_name='Ativo?',null=False, blank=True)
    priority = models.PositiveSmallIntegerField(verbose_name='Prioridade',null=False, blank=False)
    class Meta:
        db_table = 'lcr_providers'
        verbose_name = u"Rota de Saida - Provedor"
        verbose_name_plural = u"Rota de Saida - Provedores"
        ordering = ['priority']
        
    def __unicode__(self):
        return 'Grupo: %s / Provedor: %s' % (self.lcr, self.provider)

class Musiconhold(models.Model):
    user = models.ForeignKey(User,null=True)
    name = models.CharField(max_length=80,unique=True,blank=False,null=False)
    directory = models.CharField(max_length=255,null=True)
    application = models.CharField(max_length=255,null=True)
    mode = models.CharField(max_length=80,null=True)
    digit = models.CharField(max_length=5,null=True)
    sort = models.CharField(max_length=16,null=True)
    format = models.CharField(max_length=16,null=True)
    class Meta:
        db_table = 'musiconhold'

class PickupGroups(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField('Nome',max_length=100,unique=True,blank=False,null=False)
    class Meta:
        db_table = 'pickup_groups'
        verbose_name = u"Grupo de Captura"
        verbose_name_plural = u"Grupos de Captura"
    def __unicode__(self):
        return self.name

class QueueMembers(models.Model):
    queues = models.ForeignKey('Queues', null=True, blank=True)
    queue_name = models.CharField(max_length=128)
    interface = models.CharField('Ramal',max_length=128,null=False, blank=False,)
    penalty = models.IntegerField(null=False, blank=False,verbose_name='Ordem',)
    paused = models.CharField(max_length=5, null=True, blank=True,verbose_name='Desativar?', default=None)
    uniqueid = models.CharField(max_length=20, blank=True,)
    class Meta:
        db_table = 'queue_members'
        verbose_name = u"Membros"
        verbose_name_plural = u"Membros"
        ordering = ['penalty']

    def save(self, *args, **kwargs):
        self.uniqueid = random.randint(1000000,9999999)
        self.queue_name = self.queues.name
        if (self.paused == 'True'):
            self.paused = '1'
        else:
            self.paused = None
        super(QueueMembers, self).save(*args, **kwargs)

class Queues(models.Model):
    user = models.ForeignKey(User)
    description = models.CharField(u'Descrição', max_length=100, blank=False,null=False)
    name = models.CharField(u'Código',max_length=128,unique=True,blank=False,null=False)
    musiconhold = models.CharField(u'Música de Espera',max_length=128, blank=True,null=True)
    announce = models.CharField(max_length=128, blank=True,null=True,default='0')
    context = models.CharField(max_length=128, blank=True,null=True,default='default')
    timeout = models.IntegerField(null=True, blank=True,default='20')
    monitor_join = models.NullBooleanField(null=True, blank=True)
    monitor_format = models.CharField(max_length=128, blank=True,null=True,default='wav')
    queue_youarenext = models.CharField(max_length=128, blank=True,null=True,)
    queue_thereare = models.CharField(max_length=128, blank=True,null=True,)
    queue_callswaiting = models.CharField(max_length=128, blank=True,null=True,)
    queue_holdtime = models.CharField(max_length=128, blank=True,null=True,)
    queue_minutes = models.CharField(max_length=128, blank=True,null=True,)
    queue_seconds = models.CharField(max_length=128, blank=True,null=True,)
    queue_lessthan = models.CharField(max_length=128, blank=True,null=True,)
    queue_thankyou = models.CharField(max_length=128, blank=True,null=True,)
    queue_reporthold = models.CharField(max_length=128, blank=True,null=True,)
    announce_frequency = models.IntegerField(null=True, blank=True,)
    announce_round_seconds = models.IntegerField(null=True, blank=True,)
    announce_holdtime = models.CharField(max_length=128, blank=True,null=True,default='no')
    retry = models.IntegerField(null=True,default=100)
    wrapuptime = models.IntegerField(null=True, blank=True,default=5)
    maxlen = models.IntegerField(null=True, blank=True)
    servicelevel = models.IntegerField(null=True, blank=True)
    strategy = models.CharField(max_length=128, blank=True,null=True,default='linear')
    joinempty = models.CharField(max_length=128, blank=True,null=True,)
    leavewhenempty = models.CharField(max_length=128, blank=True,null=True,)
    eventmemberstatus = models.NullBooleanField(null=True, blank=True)
    eventwhencalled = models.NullBooleanField(null=True, blank=True,default=True)
    reportholdtime = models.NullBooleanField(null=True, blank=True)
    memberdelay = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    timeoutrestart = models.NullBooleanField(null=True, blank=True)
    setinterfacevar = models.NullBooleanField(null=True, blank=True)
    ringinuse = models.CharField(max_length=10,null=True,default='no')
    class Meta:
        db_table = 'queues'
        verbose_name = u"Fila"
        verbose_name_plural = u"Filas"
    def __unicode__(self):
        return self.description
    def save(self, *args, **kwargs):
        QueueMembers.objects.filter(queues=self.id).update(queue_name=self.name)
        super(Queues, self).save(*args, **kwargs)


class Rates(models.Model):
    rates_groups = models.ForeignKey('RatesGroups',verbose_name='Grupo de tarifas')
    prefix = models.CharField('Prefixo',max_length=50,blank=False,null=False)
    price = models.DecimalField(u'Preço',null=True, max_digits=10, decimal_places=2, blank=True)
    min_time = models.IntegerField('Tempo mínimo',blank=False,null=False)
    increment = models.IntegerField('Incremento',blank=False,null=False)
    class Meta:
        db_table = 'rates'
        verbose_name = u"Tarifa"
        verbose_name_plural = u"Tarifas"
    def __unicode__(self):
        return self.prefix

class RatesGroups(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(u'Descrição',max_length=80,unique=True,blank=False,null=False)
    class Meta:
        db_table = 'rates_groups'
        verbose_name = u"Tarifas"
        verbose_name_plural = u"Tarifas"
    def __unicode__(self):
        return self.name

class Report(models.Model):
    user_id = models.CharField(max_length=10, blank=True, null=True)
    exten_description = models.CharField(max_length=50, blank=True, null=True)
    origin = models.CharField(max_length=30, blank=True, null=True)
    extension = models.CharField(max_length=30, blank=True, null=True)
    agent = models.CharField(max_length=30, blank=True, null=True)
    agent_type = models.CharField(max_length=40, blank=True, null=True)
    destination = models.CharField(max_length=30, blank=True, null=True)
    forward = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=40, null=True)
    duration = models.IntegerField(blank=True, null=True)
    calldate = models.DateTimeField(blank=True, null=True)
    provider = models.CharField(max_length=60, blank=True, null=True)
    name = models.CharField(max_length=80, blank=True, null=True)
    value = models.DecimalField(null=True, max_digits=30, decimal_places=4, blank=True)
    call_type = models.CharField(max_length=30, blank=True, null=True)
    observation = models.CharField(max_length=60, null=True,blank=True)
    uniqueid = models.CharField(max_length=32, blank=True, null=True)
    linkedid = models.CharField(max_length=32, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    duration_billing = models.IntegerField(null=True,blank=True,default=0)
    uri = models.CharField(max_length=80, blank=True, null=True)
    provider_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'report'
        verbose_name = u'Relatório'
        verbose_name_plural = u'Relatórios'
   
class VoicemailUsers(models.Model):
    user = models.ForeignKey(User)
    customer_id = models.IntegerField()
    context = models.CharField(max_length=50)
    mailbox = models.IntegerField()
    password = models.CharField(max_length=4)
    fullname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    pager = models.CharField(max_length=50)
    stamp = models.DateTimeField()
    class Meta:
        db_table = 'voicemail_users'

class QueueLog(models.Model):
  time = models.DateTimeField(default=datetime.now(),null=True)
  callid = models.CharField(max_length=32, null=True)
  queuename = models.CharField(max_length=32, null=True)
  agent = models.CharField(max_length=32, null=True)
  event = models.CharField(max_length=32, null=True)
  data1 = models.CharField(max_length=100, null=True)
  data2 = models.CharField(max_length=100, null=True)
  data3 = models.CharField(max_length=100, null=True)
  data4 = models.CharField(max_length=100, null=True)
  data5 = models.CharField(max_length=100, null=True)
  class Meta:
    db_table = 'queue_log'


class ActiveCalls(models.Model):
  calldate = models.DateTimeField(default=datetime.now(),null=True)
  channel = models.CharField(max_length=50, null=True)
  origin = models.CharField(max_length=50, null=True)
  destination = models.CharField(max_length=80, null=True)
  forward = models.CharField(max_length=32, null=True)
  provider = models.CharField(max_length=100, null=True)
  call_type = models.CharField(max_length=100, null=True)
  callerid = models.CharField(max_length=100, null=True)
  uniqueid = models.CharField(max_length=100, null=True)
  class Meta:
    db_table = 'active_calls'
