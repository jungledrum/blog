from django.conf.urls import patterns, include, url


urlpatterns = patterns('posts.views.post_views',
    url(r'^$', 'index'),
    url(r'^posts/new', 'new'),
    url(r'^posts/create', 'create'),
    url(r'^posts/(?P<id>\w+)/edit', 'edit'),
    url(r'^posts/(?P<id>\w+)/update', 'update'),
    url(r'^posts/(?P<id>\w+)/$', 'show'),
    url(r'^posts/(?P<id>\w+)/destroy', 'destroy')
)

urlpatterns += patterns('posts.views.comment_views',
    url(r'^posts/(?P<post_id>\w+)/comments/create$', 'create'),
    url(r'^posts/(?P<post_id>\w+)/comments/(?P<comment_id>\w+)/destroy$', 'destroy')
)

urlpatterns += patterns('posts.views.category_views',
    url(r'^categories/$', 'index'),
    url(r'^categories/create$', 'create'),
    url(r'^categories/(?P<name>\w+)/$', 'show'),
    url(r'^categories/(?P<id>\w+)/destroy$', 'destroy'),
)

urlpatterns += patterns('admin.views',
    url(r'^admin/$', 'new'),
    url(r'^admin/login$', 'login'),
    url(r'^admin/logout$', 'logout'),
)
