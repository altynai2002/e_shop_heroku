from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, CategoriesList, CommentCreate

router = DefaultRouter()
router.register('', ProductViewSet)

# products = ProductViewSet.as_view({
#     'get': 'list',
#     'put': 'update',
#     'patch': 'partial_update',
#     'post': 'create',
#     'delete': 'destroy'
# })

urlpatterns = [
    # path('', ProductsList.as_view()),
    # path('detail/<str:pk>/', ProductDetail.as_view()),
    path('categories/', CategoriesList.as_view()),

    # path('', products),
    # path('<str:pk>/', products),

    # path('create/', CreateProduct.as_view()),
    # path('update/<str:pk>/', UpdateProduct.as_view()),
    # path('delete/<str:pk>/', DeleteProduct.as_view()),

    path('', include(router.urls)),
    path('comment/create/', CommentCreate.as_view()),
]

