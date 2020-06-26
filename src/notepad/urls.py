from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from notes.views import note_list_view, finished_task, deleted_task, recover_item


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', note_list_view, name="note-list"),
    path('finished/<id>/', finished_task, name="finished-task"),
    path('deleted/<id>/', deleted_task, name="delete-task"),
    path('recover/<id>/', recover_item, name="recover-item")


]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)