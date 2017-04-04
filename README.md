### To quickly try it locally
    cd django-blogsimple/example/  
    pip install -r ../requirements.txt  
    python manage.py syncdb --migrate
    python manage.py runserver

Create a Blog instance at `/admin/blogsimple/blog/add/`. The Blog instance is required for storing blog wide settings, like, number of entries to show per page, title for the blog, tag line for the blog etc.

With Blog instance created, you will be able to access `/blog/`. At this point, no blog entries exist. Create a blog entry at `/admin/blogsimple/blogentry/add/`.

With a blog entry created, you would be able to see the entry at `/blog/`.

To integrate into your application:
-----------------------------------
0. Install the requirements.
1. Include `blogsimple`, `pingback`, `taggit`, `django.contrib.sitemaps`, `django_xmlrpc` and `google_analytics` in settings.`INSTALLED_APPS`.
2. Include blog urls in urls.py

    url(r'^blog/', include('blogsimple.urls')),

3. If the comments have to verified through AKISMET, set settings.`AKISMET_API_KEY`.
4. Enable django admin, if not already enabled.

    python manage.py syncdb

5. Create blog at `/admin/blogsimple/blog/add/`.
6. Check your blog at `/blog/`.

Features
-------------------------

* Comment
* Comment moderation
* Category
* Tagging
* RSS
* Akismet Spam Filtering
* Trackback
* Date based archives
* Multi Author
* Supports various markup types
