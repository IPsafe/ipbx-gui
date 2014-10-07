from django.conf.urls import patterns, include, url
from django.contrib import admin
from core.views import *

from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'ipbx.core.views.home', name='home'),
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'},),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'login.html'}),

    url(r'^blacklists/adicionar/$', 'ipbx.core.views.blacklistsAdicionar', name='blacklistsAdicionar'),
    url(r'^blacklists/deletar/(?P<id>\d+)$', 'ipbx.core.views.blacklistsDeletar', name='blacklistsDeletar'),
    url(r'^blacklists/editar/(?P<id>\d+)$', 'ipbx.core.views.blacklistsEditar', name='blacklistsEditar'),
    url(r'^blacklists/$', 'ipbx.core.views.blacklists', name='blacklists'),
        
    url(r'^conferencias/adicionar/$', 'ipbx.core.views.conferenciasAdicionar', name='conferenciasAdicionar'),
    url(r'^conferencias/deletar/(?P<id>\d+)$', 'ipbx.core.views.conferenciasDeletar', name='conferenciasDeletar'),
    url(r'^conferencias/editar/(?P<id>\d+)$', 'ipbx.core.views.conferenciasEditar', name='conferenciasEditar'),
    url(r'^conferencias/$', 'ipbx.core.views.conferencias', name='conferencias'),

    url(r'^ramais/adicionar/$', 'ipbx.core.views.ramaisAdicionar', name='ramaisAdicionar'),
    url(r'^ramais/deletar/(?P<id>\d+)$', 'ipbx.core.views.ramaisDeletar', name='ramaisDeletar'),
    url(r'^ramais/editar/(?P<id>\d+)$', 'ipbx.core.views.ramaisEditar', name='ramaisEditar'),
    url(r'^ramais/$', 'ipbx.core.views.ramais', name='ramais'),

    url(r'^provedores/adicionar/$', 'ipbx.core.views.provedoresAdicionar', name='provedoresAdicionar'),
    url(r'^provedores/deletar/(?P<id>\d+)$', 'ipbx.core.views.provedoresDeletar', name='provedoresDeletar'),
    url(r'^provedores/editar/(?P<id>\d+)$', 'ipbx.core.views.provedoresEditar', name='provedoresEditar'),
    url(r'^provedores/$', 'ipbx.core.views.provedores', name='provedores'),
    
    url(r'^filas/adicionar/$', 'ipbx.core.views.filasAdicionar', name='filasAdicionar'),
    url(r'^filas/deletar/(?P<id>\d+)$', 'ipbx.core.views.filasDeletar', name='filasDeletar'),
    url(r'^filas/editar/(?P<id>\d+)$', 'ipbx.core.views.filasEditar', name='filasEditar'),
    url(r'^filas/$', 'ipbx.core.views.filas', name='filas'),

    url(r'^gruposcaptura/adicionar/$', 'ipbx.core.views.gruposcapturaAdicionar', name='gruposcapturaAdicionar'),
    url(r'^gruposcaptura/deletar/(?P<id>\d+)$', 'ipbx.core.views.gruposcapturaDeletar', name='gruposcapturaDeletar'),
    url(r'^gruposcaptura/editar/(?P<id>\d+)$', 'ipbx.core.views.gruposcapturaEditar', name='gruposcapturaEditar'),
    url(r'^gruposcaptura/$', 'ipbx.core.views.gruposcaptura', name='gruposcaptura'),
    
    url(r'^lcrs/adicionar/$', 'ipbx.core.views.lcrsAdicionar', name='lcrsAdicionar'),
    url(r'^lcrs/deletar/(?P<id>\d+)$', 'ipbx.core.views.lcrsDeletar', name='lcrsDeletar'),
    url(r'^lcrs/editar/(?P<id>\d+)$', 'ipbx.core.views.lcrsEditar', name='lcrsEditar'),
    url(r'^lcrs/$', 'ipbx.core.views.lcrs', name='lcrs'),

    url(r'^regrasdiscagem/adicionar/$', 'ipbx.core.views.regrasdiscagemAdicionar', name='regrasdiscagemAdicionar'),
    url(r'^regrasdiscagem/deletar/(?P<id>\d+)$', 'ipbx.core.views.regrasdiscagemDeletar', name='regrasdiscagemDeletar'),
    url(r'^regrasdiscagem/editar/(?P<id>\d+)$', 'ipbx.core.views.regrasdiscagemEditar', name='regrasdiscagemEditar'),
    url(r'^regrasdiscagem/$', 'ipbx.core.views.regrasdiscagem', name='regrasdiscagem'),

    url(r'^tarifas/adicionar/$', 'ipbx.core.views.tarifasAdicionar', name='tarifasAdicionar'),
    url(r'^tarifas/deletar/(?P<id>\d+)$', 'ipbx.core.views.tarifasDeletar', name='tarifasDeletar'),
    url(r'^tarifas/editar/(?P<id>\d+)$', 'ipbx.core.views.tarifasEditar', name='tarifasEditar'),
    url(r'^tarifas/$', 'ipbx.core.views.tarifas', name='tarifas'),

    url(r'^rotasentrada/adicionar/$', 'ipbx.core.views.rotasentradaAdicionar', name='rotasentradaAdicionar'),
    url(r'^rotasentrada/deletar/(?P<id>\d+)$', 'ipbx.core.views.rotasentradaDeletar', name='rotasentradaDeletar'),
    url(r'^rotasentrada/editar/(?P<id>\d+)$', 'ipbx.core.views.rotasentradaEditar', name='rotasentradaEditar'),
    url(r'^rotasentrada/$', 'ipbx.core.views.rotasentrada', name='rotasentrada'),

    url(r'^regrasentrada/(?P<id>\d+)$', 'ipbx.core.views.regrasentrada', name='regrasentrada'),
    url(r'^regrasentrada/adicionar/(?P<id>\d+)$', 'ipbx.core.views.regrasentradaAdicionar', name='regrasentradaAdicionar'),
    url(r'^regrasentrada/deletar/(?P<rid>\d+)/(?P<id>\d+)/$', 'ipbx.core.views.regrasentradaDeletar', name='regrasentradaDeletar'),
    url(r'^regrasentrada/editar/(?P<id>\d+)$', 'ipbx.core.views.regrasentradaEditar', name='regrasentradaEditar'),
    

    url(r'^report$', 'ipbx.core.views.report', name='report'),
    url(r'^report/results/$', 'ipbx.core.views.reportResults', name='reportResults'),

    url(r'^chamadasativas/$', 'ipbx.core.views.chamadasativas', name='chamadasAtivas'),

	url(r'^admin/', include(admin.site.urls)),
	(r'^grappelli/', include('grappelli.urls')),
    

)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
   urlpatterns += patterns('',
       (r'^static/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root': settings.STATIC_ROOT}),
   )
