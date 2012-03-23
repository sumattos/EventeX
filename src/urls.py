#-*- coding: utf-8 -*-

<<<<<<< HEAD
from django.conf.urls.defaults import * 
from django.contrib            import admin
from core.views                import homepage # nome da app q eu criei
from django.contrib            import admin

admin.autodiscover()

urlpatterns = patterns('subscriptions.views',

    # pagina principal
    url(r'^$', homepage),

    # pagina do cadastro
    #url(r'^$', 'subscribe', name='subscribe'),
    url(r'^cadastro/', 'subscribe', name='subscribe'),	
 
    # retorna pagina de cadastro foi realizado com sucesso
    url(r'^(\d+)/sucesso/$', 'success', name='success'),

    #admin
    url(r'^admin/', include(admin.site.urls)),
)

#urlpatterns = patterns('subscriptions.views',)


=======
from django.conf.urls.defaults import patterns, include, url
from core.views                import homepage # nome da app q eu criei
#from django.contrib.staticfiles.urls   import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', homepage),
    # Examples:
    # url(r'^$', 'src.views.home', name='home'),
    # url(r'^src/', include('src.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
#urlpatterns += staticfiles_urlpatterns()
>>>>>>> 7e9a5f74fac19b7df090d300bcc22f8c3578a934
