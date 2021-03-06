# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Conference.adminpin'
        db.alter_column(u'conference', 'adminpin', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'Conference.pin'
        db.alter_column(u'conference', 'pin', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'Conference.opts'
        db.alter_column(u'conference', 'opts', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Conference.adminopts'
        db.alter_column(u'conference', 'adminopts', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

    def backwards(self, orm):

        # Changing field 'Conference.adminpin'
        db.alter_column(u'conference', 'adminpin', self.gf('django.db.models.fields.CharField')(default='', max_length=20))

        # Changing field 'Conference.pin'
        db.alter_column(u'conference', 'pin', self.gf('django.db.models.fields.CharField')(default='', max_length=20))

        # Changing field 'Conference.opts'
        db.alter_column(u'conference', 'opts', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'Conference.adminopts'
        db.alter_column(u'conference', 'adminopts', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.blacklist': {
            'Meta': {'object_name': 'Blacklist', 'db_table': "u'blacklist'"},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'did': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'core.conference': {
            'Meta': {'object_name': 'Conference', 'db_table': "u'conference'"},
            'adminopts': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'adminpin': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'confno': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'endtime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maxusers': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'members': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'opts': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pin': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'starttime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'core.dayoff': {
            'Meta': {'object_name': 'Dayoff', 'db_table': "u'dayoff'"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'area_id': ('django.db.models.fields.IntegerField', [], {}),
            'day': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'month': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'core.dayoffarea': {
            'Meta': {'object_name': 'DayoffArea', 'db_table': "u'dayoff_area'"},
            'area_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'core.devices': {
            'Meta': {'object_name': 'Devices', 'db_table': "u'devices'"},
            'accountcode': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'allow': ('django.db.models.fields.CharField', [], {'default': "u'alaw,ulaw,g729'", 'max_length': '200', 'null': 'True'}),
            'amaflags': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True'}),
            'callbackextension': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'callerid': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True'}),
            'callgroup': ('django.db.models.fields.CharField', [], {'default': "u'1'", 'max_length': '10', 'null': 'True'}),
            'cancallforward': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'canreinvite': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'context': ('django.db.models.fields.CharField', [], {'default': "u'default'", 'max_length': '80', 'null': 'True'}),
            'defaultip': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'defaultuser': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True'}),
            'deny': ('django.db.models.fields.CharField', [], {'max_length': '95', 'null': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'device_type': ('django.db.models.fields.CharField', [], {'default': "u'extension'", 'max_length': '20', 'blank': 'True'}),
            'dialrules_groups': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.DialrulesGroups']", 'null': 'True', 'blank': 'True'}),
            'dnd': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dtmfmode': ('django.db.models.fields.CharField', [], {'default': "u'rfc2833'", 'max_length': '7', 'null': 'True'}),
            'followme': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'followme_busy': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'followme_noanswer': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'force_monitor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fromdomain': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True'}),
            'fromuser': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True'}),
            'fullcontact': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True'}),
            'host': ('django.db.models.fields.CharField', [], {'default': "u'dynamic'", 'max_length': '31', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insecure': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'ipaddr': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "u'br'", 'max_length': '2', 'null': 'True'}),
            'lastms': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'lcr': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Lcr']", 'null': 'True', 'blank': 'True'}),
            'mailbox': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'mask': ('django.db.models.fields.CharField', [], {'max_length': '95', 'null': 'True'}),
            'md5secret': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True'}),
            'monitor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'musiconhold': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'nat': ('django.db.models.fields.CharField', [], {'default': "u'force_rport,comedia'", 'max_length': '20', 'null': 'True'}),
            'overflow': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'permit': ('django.db.models.fields.CharField', [], {'max_length': '95', 'null': 'True'}),
            'pickupgroup': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.PickupGroups']", 'null': 'True', 'db_column': "u'pickupgroup'", 'blank': 'True'}),
            'port': ('django.db.models.fields.CharField', [], {'default': "u'5060'", 'max_length': '5', 'null': 'True'}),
            'qualify': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'rate_groups': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.RatesGroups']", 'null': 'True', 'blank': 'True'}),
            'regexten': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True'}),
            'register': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'regseconds': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'regserver': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'restrictcid': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'rtautoclear': ('django.db.models.fields.CharField', [], {'default': "u'no'", 'max_length': '30', 'null': 'True'}),
            'rtcachefriends': ('django.db.models.fields.CharField', [], {'default': "u'yes'", 'max_length': '30', 'null': 'True'}),
            'rtpholdtimeout': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'rtptimeout': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "u'friend'", 'max_length': '30', 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'useragent': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'})
        },
        u'core.dialrules': {
            'Meta': {'object_name': 'Dialrules', 'db_table': "u'dialrules'"},
            'add': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'cut': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'dialrules_groups': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.DialrulesGroups']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_len': ('django.db.models.fields.IntegerField', [], {}),
            'min_len': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'core.dialrulesgroups': {
            'Meta': {'object_name': 'DialrulesGroups', 'db_table': "u'dialrules_groups'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'core.extensionsconf': {
            'Meta': {'object_name': 'ExtensionsConf', 'db_table': "u'extensions_conf'"},
            'app': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'appdata': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'context': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'exten': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {})
        },
        u'core.inboundroutes': {
            'Meta': {'object_name': 'InboundRoutes', 'db_table': "u'inbound_routes'"},
            'area_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'did': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'providers': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Providers']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'core.inboundrules': {
            'Meta': {'object_name': 'InboundRules', 'db_table': "u'inbound_rules'"},
            'dayoff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'destination': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inbound_routes': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.InboundRoutes']"}),
            'specific_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'start': ('django.db.models.fields.TimeField', [], {'default': "u'00:00:00'"}),
            'stop': ('django.db.models.fields.TimeField', [], {'default': "u'23:59:59'"}),
            'weekdays': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'})
        },
        u'core.lcr': {
            'Meta': {'object_name': 'Lcr', 'db_table': "u'lcr'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'order': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'core.lcrproviders': {
            'Meta': {'ordering': "[u'priority']", 'object_name': 'LcrProviders', 'db_table': "u'lcr_providers'"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lcr': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Lcr']"}),
            'priority': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'provider': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Providers']"})
        },
        u'core.musiconhold': {
            'Meta': {'object_name': 'Musiconhold', 'db_table': "u'musiconhold'"},
            'application': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'digit': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True'}),
            'directory': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'format': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mode': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'sort': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'})
        },
        u'core.pickupgroups': {
            'Meta': {'object_name': 'PickupGroups', 'db_table': "u'pickup_groups'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'core.providers': {
            'Meta': {'object_name': 'Providers', 'db_table': "u'devices'", 'managed': 'False'},
            'accountcode': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'allow': ('django.db.models.fields.CharField', [], {'default': "u'alaw,ulaw,g729'", 'max_length': '200', 'blank': 'True'}),
            'amaflags': ('django.db.models.fields.CharField', [], {'max_length': '7', 'blank': 'True'}),
            'callbackextension': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'callerid': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'callgroup': ('django.db.models.fields.CharField', [], {'default': "u'1'", 'max_length': '10', 'blank': 'True'}),
            'cancallforward': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'canreinvite': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'context': ('django.db.models.fields.CharField', [], {'default': "u'provider'", 'max_length': '80', 'blank': 'True'}),
            'defaultip': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'defaultuser': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'deny': ('django.db.models.fields.CharField', [], {'max_length': '95', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'device_type': ('django.db.models.fields.CharField', [], {'default': "u'provider'", 'max_length': '20', 'blank': 'True'}),
            'dialrules_groups': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.DialrulesGroups']", 'null': 'True', 'blank': 'True'}),
            'dnd': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dtmfmode': ('django.db.models.fields.CharField', [], {'default': "u'rfc2833'", 'max_length': '7', 'blank': 'True'}),
            'followme': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'followme_busy': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'followme_noanswer': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'force_monitor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fromdomain': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'fromuser': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'fullcontact': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'host': ('django.db.models.fields.CharField', [], {'default': "u'dynamic'", 'max_length': '31', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insecure': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'ipaddr': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "u'br'", 'max_length': '2', 'blank': 'True'}),
            'lastms': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'lcr': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Lcr']", 'null': 'True', 'blank': 'True'}),
            'mailbox': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'mask': ('django.db.models.fields.CharField', [], {'max_length': '95', 'blank': 'True'}),
            'md5secret': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'monitor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'musiconhold': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'nat': ('django.db.models.fields.CharField', [], {'default': "u'no'", 'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'overflow': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'permit': ('django.db.models.fields.CharField', [], {'max_length': '95', 'blank': 'True'}),
            'pickupgroup': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.PickupGroups']", 'null': 'True', 'db_column': "u'pickupgroup'", 'blank': 'True'}),
            'port': ('django.db.models.fields.CharField', [], {'default': "u'5060'", 'max_length': '5', 'blank': 'True'}),
            'qualify': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'rate_groups': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.RatesGroups']", 'null': 'True', 'blank': 'True'}),
            'regexten': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'register': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'regseconds': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'regserver': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'restrictcid': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'rtautoclear': ('django.db.models.fields.CharField', [], {'default': "u'no'", 'max_length': '30', 'blank': 'True'}),
            'rtcachefriends': ('django.db.models.fields.CharField', [], {'default': "u'yes'", 'max_length': '30', 'blank': 'True'}),
            'rtpholdtimeout': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'rtptimeout': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "u'peer'", 'max_length': '30', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'useragent': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'})
        },
        u'core.queuelog': {
            'Meta': {'object_name': 'QueueLog', 'db_table': "u'queue_log'"},
            'agent': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'callid': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'data1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'data2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'data3': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'data4': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'data5': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'event': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'queuename': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 8, 7, 0, 0)', 'null': 'True'})
        },
        u'core.queuemembers': {
            'Meta': {'ordering': "[u'penalty']", 'object_name': 'QueueMembers', 'db_table': "u'queue_members'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interface': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'paused': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'penalty': ('django.db.models.fields.IntegerField', [], {}),
            'queue_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'queues': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Queues']", 'null': 'True', 'blank': 'True'}),
            'uniqueid': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        u'core.queues': {
            'Meta': {'object_name': 'Queues', 'db_table': "u'queues'"},
            'announce': ('django.db.models.fields.CharField', [], {'default': "u'0'", 'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'announce_frequency': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'announce_holdtime': ('django.db.models.fields.CharField', [], {'default': "u'no'", 'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'announce_round_seconds': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'context': ('django.db.models.fields.CharField', [], {'default': "u'default'", 'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'eventmemberstatus': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'eventwhencalled': ('django.db.models.fields.NullBooleanField', [], {'default': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'joinempty': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'leavewhenempty': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'maxlen': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'memberdelay': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'monitor_format': ('django.db.models.fields.CharField', [], {'default': "u'wav'", 'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'monitor_join': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'musiconhold': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'queue_callswaiting': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'queue_holdtime': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'queue_lessthan': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'queue_minutes': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'queue_reporthold': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'queue_seconds': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'queue_thankyou': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'queue_thereare': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'queue_youarenext': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'reportholdtime': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'retry': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'servicelevel': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'setinterfacevar': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'strategy': ('django.db.models.fields.CharField', [], {'default': "u'linear'", 'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'timeout': ('django.db.models.fields.IntegerField', [], {'default': "u'20'", 'null': 'True', 'blank': 'True'}),
            'timeoutrestart': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'weight': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wrapuptime': ('django.db.models.fields.IntegerField', [], {'default': '5', 'null': 'True', 'blank': 'True'})
        },
        u'core.rates': {
            'Meta': {'object_name': 'Rates', 'db_table': "u'rates'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'increment': ('django.db.models.fields.IntegerField', [], {}),
            'min_time': ('django.db.models.fields.IntegerField', [], {}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'rates_groups': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.RatesGroups']"})
        },
        u'core.ratesgroups': {
            'Meta': {'object_name': 'RatesGroups', 'db_table': "u'rates_groups'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'core.report': {
            'Meta': {'object_name': 'Report', 'db_table': "u'report'"},
            'agent': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'agent_type': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'call_type': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'calldate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'destination': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'duration': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'duration_billing': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'exten_description': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'extension': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'forward': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'linkedid': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'observation': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'origin': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'provider': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'provider_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sequence': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'uniqueid': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '30', 'decimal_places': '4', 'blank': 'True'})
        },
        u'core.voicemailusers': {
            'Meta': {'object_name': 'VoicemailUsers', 'db_table': "u'voicemail_users'"},
            'context': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'customer_id': ('django.db.models.fields.IntegerField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'fullname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mailbox': ('django.db.models.fields.IntegerField', [], {}),
            'pager': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'stamp': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['core']