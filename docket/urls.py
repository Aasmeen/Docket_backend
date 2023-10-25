from django.urls import path, re_path

from docket import views as docket_views

urlpatterns = [
    path("", docket_views.CreateDocket.as_view()),
    path("list/", docket_views.GetDocketList.as_view()),
    path("supplier-list/", docket_views.GetSupplierName.as_view({'get': 'list'})),
    re_path(r"^po-list/(?P<supplier_name>[\-_a-zA-Z0-9 ()\/]+)/$", docket_views.GetPOList.as_view()),
]
