from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('create/', views.posting_create, name='posting_create'),
    path('', views.posting_index, name='posting_index'),
    path('<int:posting_pk>/detail/', views.posting_detail, name='posting_detail'),
    path('<int:posting_pk>/update/', views.posting_update, name='posting_update'),
    path('<int:posting_pk>/delete/', views.posting_delete, name='posting_delete'),
    path('<int:posting_pk>/replies/create/', views.reply_create, name='reply_create'),
    path('<int:posting_pk>/replies/<int:reply_pk>/delete/', views.reply_create, name='reply_create'),
] 
# + static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)
