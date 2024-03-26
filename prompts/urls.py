from rest_framework import renderers
from rest_framework.routers import path
from rest_framework.urlpatterns import format_suffix_patterns

from prompts.views import  PromptViewSet, CategoryViewSet

prompt_list = PromptViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
prompt_detail = PromptViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


category_list = CategoryViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
category_detail = CategoryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


# urlpatterns = format_suffix_patterns([
#     path('', prompt_list, name='prompt-list'),
#     path('category/<int:pk>/', prompt_list, name='category-detail'),
#     path('category/', prompt_list, name='category-list'),
#     path('<int:pk>/', prompt_detail, name='prompt-detail'),
# ])