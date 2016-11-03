# -*- coding: utf-8 -*-

from django.conf.urls import *


from blog.views import (PostsListView, PostDetailView, submit_ajax, submit,
 delete_all_objects, search_posts)

urlpatterns = [
    url(r'search_posts/',search_posts),
    url(r'delete_all_objects/',delete_all_objects),
    url(r'form_submit', submit),
    url(r'submit/',submit_ajax),
    url(r'^$',PostsListView.as_view(),name='list'),  # вывод списка постов
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()),  # вывод поста с определенным номером
]
