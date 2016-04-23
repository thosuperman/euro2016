from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'posts.views.list_post', name = "list_post"),
    url(r'^create/$', 'posts.views.create_post', name = "create_post"),
    url(r'^(?P<id>\d+)/delete/$', 'posts.views.delete_post', name = "delete_post"),
    url(r'^(?P<id>\d+)/edit/$', 'posts.views.update_post', name = "update"),
    url(r'^(?P<id>\d+)/$', 'posts.views.detail_post', name = "detail"),
]
