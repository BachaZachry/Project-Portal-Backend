from django.contrib import admin
from django.urls import path,include
from rest_framework.documentation import include_docs_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('users.api.urls')),
    path('promo/',include('promo.api.urls')),
    path('professor/',include('professors.api.urls')),
    path('student/',include('students.api.urls')),
    path('docs/',include_docs_urls(title="Project Portal")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('debug/',include(debug_toolbar.urls)),
    ]

