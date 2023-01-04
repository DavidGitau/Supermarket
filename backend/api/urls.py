from django.urls import path
from api.views import CustomDetail, CustomList
from api.models import *
from api.serializers import *

namespace = 'api'

urlpatterns = []

l1 = [
    Category,
    Order,
    Product,
    User
]

l2 = [
    CategorySerializer,
    OrderSerializer,
    ProductSerializer,
    UserSerializer
]

l3 = [
    'cg',
    'od',
    'pr',
    'us'
]

for i in range(len(l3)):
    urlpatterns.append(
        path(
            l3[i]+'/<int:pk>',
            CustomDetail.as_view(
                queryset=l1[i].objects.all(),
                serializer_class=l2[i]
            ),
            name=l3[i]+'-single'
        )
    ),
    urlpatterns.append(
        path(
            l3[i],
            CustomList.as_view(
                queryset=l1[i].objects.all(),
                serializer_class=l2[i]
            ),
            name=l3[i]
        )
    )
