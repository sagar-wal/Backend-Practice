from django.urls import path,reverse
from . import views
urlpatterns=[
    path('',views.home, name='home'),
    path('create',views.create,name='create'),
    path('view',views.view,name='view'),
    path('delete',views.view,name='delete'),
    path('editview',views.view,name='editview'),
    path('tru/(?P<note>\d+)/(?P<time>\d+)/$',views.tru,name='tru'),
    path('edit/(?P<note>\d+)/(?P<time>\d+)/$',views.edit,name='edit'),
    path('input',views.input,name='create note'),
    path('edit/(?P<note>\d+)/(?P<time>\d+)/editsave',views.editsave,name='save edits')

    
]
#reverse(views.tru)
#/<int:id1>
#edit/(?P<note>\d+)/(?P<time>\d+)/$