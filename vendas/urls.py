from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from shop import urls as shopUrls
from order import urls as orderUrls

routeLists = [
    shopUrls.routeList,
    orderUrls.routeList,
]


router = routers.DefaultRouter()
for routeList in routeLists:
    for route in routeList:
        router.register(route[0], route[1])


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include_docs_urls(title='Vendas Web Usesoft'))
]