from rest_framework.pagination import BasePagination, PageNumberPagination


class BaseProductsPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 1000
