from django.urls import path,include
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('login', login, name='login'),
    path('users',users,name='users'),
    path('ref',ref,name='ref'),
    path('refcreate',refcreate,name='refcreate'),
    path('refedit',refedit,name='refedit'),
    path('reft',reft,name='reft'),
    path('tc',tc,name='tc'),
    path('manifest',manifest,name='manifest'),
    path('manifestcreate',manifestcreate,name='manifestcreate'),
    path('manifestedit',manifestedit,name='manifestedit'),
    path('sms',sms,name='sms'),
    path('booking',booking,name='booking'),
    path('service',service,name='service'),
    path('servicetypes',servicetypes,name='servicetypes'),
    path('reports',reports,name='reports'),
    path('reftwords',reftwords,name='reftwords'),
    path('scheduled',scheduled,name='scheduled'),
    path('station',station,name='station'),
    path('usergroup',usergroup,name='usergroup'),
    path('users',users,name='users'),
    path('createuser',createuser,name='createuser'),
    path('edituser',edituser,name='edituser'),
    path('permission',permission,name='permission'),

    path('serviceload',serviceload,name='serviceload'),
    path('aircraft',aircraft,name='aircraft'),
    path('savedroutes',savedroutes,name='savedroutes'),
    path('dstnotifications',dstnotifications,name='dstnotifications'),
    path('dstrestrict',dstrestrict,name='dstrestrict'),
    path('dsttimeaddon',dsttimeaddon,name='dsttimeaddon'),
    path('acavailability',acavailability,name='acavailability'),
    path('acavailabilitytype',acavailabilitytype,name='acavailabilitytype'),
    path('ssr',ssr,name='ssr'),
    path('queues',queues,name='queues'),
    path('destination',destination,name='destination'),
    path('createpage',createpage,name='createpage'),
    path('edit',edit,name='edit'),
    
  
  



]