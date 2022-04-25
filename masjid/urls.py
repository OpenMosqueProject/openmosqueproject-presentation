from django.contrib import admin
from django.urls import include
from django.urls import path

from .views import MasjidCreate
from .views import MasjidDelete
from .views import MasjidDetail
from .views import MasjidEdit
from .views import MasjidList


urlpatterns = [
	
	path('', MasjidList.as_view(), name='masjid_list'),
	path('detail/<int:pk>', MasjidDetail.as_view(), name='masjid_detail'),
	path('create/', MasjidCreate.as_view(), name='masjid_create'),
	path('edit/<int:pk>', MasjidEdit.as_view(), name='masjid_edit'),
	path('delete/<int:pk>', MasjidDelete.as_view(), name='masjid_delete')
]
