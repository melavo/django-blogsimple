from datetime import datetime
from django.conf.urls import patterns, url
from django.contrib.sitemaps import GenericSitemap
from blogsimple import feeds
from blogsimple.models import BlogEntry

blog_info_dict = {
    'queryset': BlogEntry.objects.all(),
    'date_field': 'publish_date',
}
sitemaps = {
    'blog': GenericSitemap(blog_info_dict, priority=0.5)
}

urlpatterns = patterns('blogsimple.views',
    url(r'^$', 'index', name="blogsimple_index"),
    url(r'^install/$', 'install_blog', name='blogsimple_install'),
    url(r'^page/(?P<page>\d+)/$', 'index',  name='blogsimple_page'),
    url(r'^(?P<year>\d{4})/(?P<month>\d+)/(?P<slug>[-\w]+)/$', 'details',
        name='blogsimple_details'),
    url(r'^blogroll/$', 'create_blogroll', name='blogsimple_blogroll'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', 'tag_details',
        name='blogsimple_tag_details'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/(?P<page>\d+)/$', 'tag_details',
        name='blogsimple_tag_details_page'),
    url(r'^author/(?P<username>[\w.@+-]+)/$', 'author', name='blogsimple_author_page'),

    url(r'^admin/$', 'admin_dashboard', name='blogsimple_admin_dashboard'),
    url(r'^admin/entry/new/$', 'admin_entry',
        name='blogsimple_admin_entry_new'),
    url(r'^admin/entry/edit/(?P<pk>\d+)/$', 'admin_edit',
        name='blogsimple_admin_entry_edit'),
    url(r'^admin/entry/manage/$', 'admin_manage_entries',
        name='blogsimple_admin_entry_manage'),
    url(r'^admin/entry/manage/(?P<username>[\w.@+-]+)/$',
        'admin_manage_entries', name='blogsimple_admin_author_entry_manage'),
    url(r'^admin/comments/manage/$', 'admin_manage_comments',
        name='blogsimple_admin_comments_manage'),
    url(r'^admin/comments/manage/(?P<entry_id>\d+)/$',
        'admin_manage_comments', name='blogsimple_admin_entry_comments_manage'),
    url(r'^admin/preferences/edit/$', 'admin_edit_preferences',
        name='blogsimple_admin_edit_preferences'),
    url(r'^admin/comment/approve/$', 'admin_comment_approve',
        name='blogsimple_admin_comment_approve'),
    url(r'^admin/comment/block/$', 'admin_comment_block',
        name='blogsimple_admin_comment_block'),
)

# sitemap.xml
urlpatterns += patterns('django.contrib.sitemaps.views',
    url(r'^sitemap\.xml$', 'sitemap', {'sitemaps': sitemaps}),
)

# Archive view
urlpatterns += patterns('blogsimple.views',
    url(r'^archive/(?P<year>\d+)/(?P<month>\w+)/$', 'monthly_view', name='blogsimple_archives')
)

urlpatterns += patterns('django_xmlrpc.views',
    url(r'^xmlrpc/$', 'handle_xmlrpc', {}, name='xmlrpc'),
)

urlpatterns += patterns('',
    url(r'^rss/latest/$', feeds.main_feed(), name='blogsimple_feed')
)

urlpatterns += patterns('',
    url(r'^rss/latest/(?P<tag>[-\w]+)/$', feeds.CatFeed(), name='blogsimple_tag_feed')
)

urlpatterns += patterns('blogsimple.views',
    url(r'^(?P<slug>[-\w]+)/$', 'details', name='blogsimple_page_details'),
)
