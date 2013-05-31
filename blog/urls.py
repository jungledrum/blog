from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'posts.views.post_views.index'),
    url(r'^posts/new', 'posts.views.post_views.new'),
    url(r'^posts/create', 'posts.views.post_views.create'),
    url(r'^posts/(?P<id>\w+)/edit', 'posts.views.post_views.edit'),
    url(r'^posts/(?P<id>\w+)/update', 'posts.views.post_views.update'),
    url(r'^posts/(?P<id>\w+)/$', 'posts.views.post_views.show'),
    url(r'^posts/(?P<id>\w+)/destroy', 'posts.views.post_views.destroy'),

    url(r'^categories/$', 'posts.views.category_views.index'),
    url(r'^categories/create$', 'posts.views.category_views.create'),
    url(r'^categories/(?P<name>\w+)/$', 'posts.views.category_views.show'),

    url(r'^posts/(?P<post_id>\w+)/comments/create$', 'posts.views.comment_views.create'),

    url(r'^admin/$', 'admin.views.new'),
    url(r'^admin/login$', 'admin.views.login'),
)
