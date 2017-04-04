from distutils.core import setup

setup(
    name="django-blogsimple",
    version="0.6.2",
    packages=['blogsimple',
              'blogsimple/conf',
              'blogsimple/management',
              'blogsimple/management/commands',
              'blogsimple/templatetags'
              ],
    package_dir={'blogsimple': 'blogsimple'},
    package_data={'blogsimple': ['templates/*.html',
                               'templates/blogsimple/*.html',
                               'templates/blogsimple/admin/*.html',
                               'templates/blogsimple/admin/*.js',
                               'static/blogsimple/admin/*.css',
                               'static/blogsimple/admin/img/*.png',
                               'static/blogsimple/css/*.css',
                               'static/blogsimple/images/*.png',
                               'static/blogsimple/images/*.jpg',
                               'static/blogsimple/images/*.gif',
                               'static/blogsimple/js/*.js',
                               ]
    },
    author="Wayne Vo",
    author_email="wayne@melavo.com",
    description="A django based blog",
    long_description=
    """
        Blogsimple is a simple but robust blogging application written with django

        Some of the features include comments using contrib.comments framework,
        backtype and pingback support, rich text using django-markupfield,
        month based archiving, tagging using django-taggit and categorization
    """,
    classifiers = ['Development Status :: 5 - Production/Stable',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Internet :: WWW/HTTP',
                   'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                   'Topic :: Internet :: WWW/HTTP :: WSGI',
                   'Topic :: Software Development :: Libraries :: Application Frameworks',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   ],
    url="http://blogsimple.melavo.com/",
    license="Dual Licenced under GPL and BSD",
    platforms=["all"],
)
