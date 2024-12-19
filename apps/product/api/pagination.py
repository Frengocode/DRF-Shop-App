from rest_framework.pagination import BasePagination


class GetProductsPagination(BasePagination):
    def paginate_queryset(self, queryset, request, view=None):
        if len(queryset) < 20:
            return queryset

        page_size = request.query_params.get("page_size", 10)
        offset = int(request.query_params.get("offset", 0))
        limit = offset + int(page_size)

        return queryset[offset:limit]

    def get_paginated_response(self, data):
        return {"count": len(data), "results": data}
