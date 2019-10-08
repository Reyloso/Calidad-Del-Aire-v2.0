from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class PaginationPageNumber(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'limit': self.page_size,
            'message': 'lista de datos',
            'code': 1,
            'draw': 0,
            'recordsTotal': self.page.paginator.count,
            'recordsFiltered': self.page.paginator.count,
            'data': data,
        })


class PaginationLimitOffset (LimitOffsetPagination):
    limit_query_param = 'length'
    offset_query_param = "start"

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'message': 'lista de datos',
            'code': 1,
            'recordsTotal': self.count,
            'recordsFiltered': self.count,
            'data': data,
        })
