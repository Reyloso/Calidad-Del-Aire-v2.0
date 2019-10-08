from django.db import models
from model_utils import Choices


# Departament, Country
def query_by_args(queryset, **kwargs):
    ORDER_COLUMN = Choices(
        ('0', 'id'),
        ('1', 'name'),
        ('2', 'indicative'),
        ('3', 'status'),
    )

    if 'draw' in kwargs:
        draw = int(kwargs.get('draw', None)[0])
    else:
        draw = 0

    if 'length' in kwargs:
        length = int(kwargs.get('length', None)[0])
    else:
        length = queryset.count()

    if 'start' in kwargs:
        start = int(kwargs.get('start', None)[0])
    else:
        start = 0

    if 'search[value]' in kwargs:
        search_value = kwargs.get('search[value]', None)[0]
    else:
        search_value = ''

    if 'order[0][column]' in kwargs:
        order_column = kwargs.get('order[0][column]', None)[0]
    else:
        order_column = '0'

    if 'order[0][dir]' in kwargs:
        order = kwargs.get('order[0][dir]', None)[0]
    else:
        order = 'asc'

    order_column = ORDER_COLUMN[order_column]

    # # django orm '-' -> desc
    if order == 'desc':
        order_column = '-' + order_column

    total = queryset.count()

    if search_value:
        queryset = queryset.filter(models.Q(id__icontains=search_value) |
                                   models.Q(name__icontains=search_value) |
                                   models.Q(indicative__icontains=search_value) |
                                   models.Q(status__icontains=search_value))

    count = queryset.count()
    queryset = queryset.order_by(order_column)[start:start + length]
    return {
        'items': queryset,
        'count': count,
        'total': total,
        'draw': draw
    }


# Eps, Arl, Neighborhood
def query_others_by_args(queryset, **kwargs):
    ORDER_COLUMN = Choices(
        ('0', 'id'),
        ('1', 'name'),
        ('2', 'status'),
    )

    if 'draw' in kwargs:
        draw = int(kwargs.get('draw', None)[0])
    else:
        draw = 0

    if 'length' in kwargs:
        length = int(kwargs.get('length', None)[0])
    else:
        length = queryset.count()

    if 'start' in kwargs:
        start = int(kwargs.get('start', None)[0])
    else:
        start = 0

    if 'search[value]' in kwargs:
        search_value = kwargs.get('search[value]', None)[0]
    else:
        search_value = ''

    if 'order[0][column]' in kwargs:
        order_column = kwargs.get('order[0][column]', None)[0]
    else:
        order_column = '0'

    if 'order[0][dir]' in kwargs:
        order = kwargs.get('order[0][dir]', None)[0]
    else:
        order = 'asc'

    order_column = ORDER_COLUMN[order_column]

    # # django orm '-' -> desc
    if order == 'desc':
        order_column = '-' + order_column

    total = queryset.count()

    if search_value:
        queryset = queryset.filter(models.Q(id__icontains=search_value) |
                                   models.Q(name__icontains=search_value) |
                                   models.Q(status__icontains=search_value))

    count = queryset.count()
    queryset = queryset.order_by(order_column)[start:start + length]
    return {
        'items': queryset,
        'count': count,
        'total': total,
        'draw': draw
    }


# # Vehicles
# def query_vehicles_by_args(queryset, **kwargs):
#     ORDER_COLUMN = Choices(
#         ('0', 'id'),
#         ('1', 'name'),
#         ('2', 'description'),
#         ('3', 'status'),
#     )

#     if 'draw' in kwargs:
#         draw = int(kwargs.get('draw', None)[0])
#     else:
#         draw = 0

#     if 'length' in kwargs:
#         length = int(kwargs.get('length', None)[0])
#     else:
#         length = queryset.count()

#     if 'start' in kwargs:
#         start = int(kwargs.get('start', None)[0])
#     else:
#         start = 0

#     if 'search[value]' in kwargs:
#         search_value = kwargs.get('search[value]', None)[0]
#     else:
#         search_value = ''

#     if 'order[0][column]' in kwargs:
#         order_column = kwargs.get('order[0][column]', None)[0]
#     else:
#         order_column = '0'

#     if 'order[0][dir]' in kwargs:
#         order = kwargs.get('order[0][dir]', None)[0]
#     else:
#         order = 'asc'

#     order_column = ORDER_COLUMN[order_column]

#     # # django orm '-' -> desc
#     if order == 'desc':
#         order_column = '-' + order_column

#     total = queryset.count()

#     if search_value:
#         queryset = queryset.filter(models.Q(id__icontains=search_value) |
#                                    models.Q(name__icontains=search_value) |
#                                    models.Q(description__icontains=search_value) |
#                                    models.Q(status__icontains=search_value))

#     count = queryset.count()
#     queryset = queryset.order_by(order_column)[start:start + length]
#     return {
#         'items': queryset,
#         'count': count,
#         'total': total,
#         'draw': draw
#     }


# # Vehicles
# def query_inventories_by_args(queryset, **kwargs):
#     ORDER_COLUMN = Choices(
#         ('0', 'id'),
#         ('1', 'vehicle__name'),
#         ('2', 'serial'),
#         ('3', 'station_current__name'),
#         ('4', 'status'),
#     )

#     if 'draw' in kwargs:
#         draw = int(kwargs.get('draw', None)[0])
#     else:
#         draw = 0

#     if 'length' in kwargs:
#         length = int(kwargs.get('length', None)[0])
#     else:
#         length = queryset.count()

#     if 'start' in kwargs:
#         start = int(kwargs.get('start', None)[0])
#     else:
#         start = 0

#     if 'search[value]' in kwargs:
#         search_value = kwargs.get('search[value]', None)[0]
#     else:
#         search_value = ''

#     if 'order[0][column]' in kwargs:
#         order_column = kwargs.get('order[0][column]', None)[0]
#     else:
#         order_column = '0'

#     if 'order[0][dir]' in kwargs:
#         order = kwargs.get('order[0][dir]', None)[0]
#     else:
#         order = 'asc'

#     order_column = ORDER_COLUMN[order_column]

#     # # django orm '-' -> desc
#     if order == 'desc':
#         order_column = '-' + order_column

#     total = queryset.count()

#     if search_value:
#         queryset = queryset.filter(models.Q(id__icontains=search_value) |
#                                    models.Q(vehicle__name__icontains=search_value) |
#                                    models.Q(serial__icontains=search_value) |
#                                    models.Q(station_current__name__icontains=search_value) |
#                                    models.Q(status__icontains=search_value))

#     count = queryset.count()
#     queryset = queryset.order_by(order_column)[start:start + length]
#     return {
#         'items': queryset,
#         'count': count,
#         'total': total,
#         'draw': draw
#     }


# # Vehicles
# def query_stations_by_args(queryset, **kwargs):
#     ORDER_COLUMN = Choices(
#         ('0', 'id'),
#         ('1', 'name'),
#         ('2', 'address'),
#         ('3', 'host_current__name'),
#         ('4', 'capacity'),
#         ('5', 'status'),
#     )

#     if 'draw' in kwargs:
#         draw = int(kwargs.get('draw', None)[0])
#     else:
#         draw = 0

#     if 'length' in kwargs:
#         length = int(kwargs.get('length', None)[0])
#     else:
#         length = queryset.count()

#     if 'start' in kwargs:
#         start = int(kwargs.get('start', None)[0])
#     else:
#         start = 0

#     if 'search[value]' in kwargs:
#         search_value = kwargs.get('search[value]', None)[0]
#     else:
#         search_value = ''

#     if 'order[0][column]' in kwargs:
#         order_column = kwargs.get('order[0][column]', None)[0]
#     else:
#         order_column = '0'

#     if 'order[0][dir]' in kwargs:
#         order = kwargs.get('order[0][dir]', None)[0]
#     else:
#         order = 'asc'

#     order_column = ORDER_COLUMN[order_column]

#     # # django orm '-' -> desc
#     if order == 'desc':
#         order_column = '-' + order_column

#     total = queryset.count()

#     if search_value:
#         queryset = queryset.filter(models.Q(id__icontains=search_value) |
#                                    models.Q(name__icontains=search_value) |
#                                    models.Q(address__icontains=search_value) |
#                                    models.Q(host_current__name__icontains=search_value) |
#                                    models.Q(capacity__icontains=search_value) |
#                                    models.Q(status__icontains=search_value))

#     count = queryset.count()
#     queryset = queryset.order_by(order_column)[start:start + length]
#     return {
#         'items': queryset,
#         'count': count,
#         'total': total,
#         'draw': draw
#     }


# # Peoples
# def query_peoples_by_args(queryset, **kwargs):
#     ORDER_COLUMN = Choices(
#         ('0', 'id'),
#         ('1', 'document'),
#         ('2', 'name'),
#         ('3', 'email'),
#         ('4', 'mobile'),
#         ('5', 'is_active'),
#         ('6', 'status'),
#     )

#     if 'draw' in kwargs:
#         draw = int(kwargs.get('draw', None)[0])
#     else:
#         draw = 0

#     if 'length' in kwargs:
#         length = int(kwargs.get('length', None)[0])
#     else:
#         length = queryset.count()

#     if 'start' in kwargs:
#         start = int(kwargs.get('start', None)[0])
#     else:
#         start = 0

#     if 'search[value]' in kwargs:
#         search_value = kwargs.get('search[value]', None)[0]
#     else:
#         search_value = ''

#     if 'order[0][column]' in kwargs:
#         order_column = kwargs.get('order[0][column]', None)[0]
#     else:
#         order_column = '0'

#     if 'order[0][dir]' in kwargs:
#         order = kwargs.get('order[0][dir]', None)[0]
#     else:
#         order = 'asc'

#     order_column = ORDER_COLUMN[order_column]

#     # # django orm '-' -> desc
#     if order == 'desc':
#         order_column = '-' + order_column

#     total = queryset.count()

#     if search_value:
#         queryset = queryset.filter(models.Q(id__icontains=search_value) |
#                                    models.Q(document__icontains=search_value) |
#                                    models.Q(name__icontains=search_value) |
#                                    models.Q(email__icontains=search_value) |
#                                    models.Q(mobile__icontains=search_value) |
#                                    models.Q(status__icontains=search_value))

#     count = queryset.count()
#     queryset = queryset.order_by(order_column)[start:start + length]
#     return {
#         'items': queryset,
#         'count': count,
#         'total': total,
#         'draw': draw
#     }


# # Loan
# def query_loans_by_args(queryset, **kwargs):
#     ORDER_COLUMN = Choices(
#         ('0', 'id'),
#         ('1', 'inventory__serial'),
#         ('2', 'station_origin__name'),
#         ('3', 'station_received__name'),
#         ('4', 'station_destination__name'),
#         ('5', 'client__document'),
#         ('6', 'client__name'),
#         ('7', 'received'),
#     )

#     if 'draw' in kwargs:
#         draw = int(kwargs.get('draw', None)[0])
#     else:
#         draw = 0

#     if 'length' in kwargs:
#         length = int(kwargs.get('length', None)[0])
#     else:
#         length = queryset.count()

#     if 'start' in kwargs:
#         start = int(kwargs.get('start', None)[0])
#     else:
#         start = 0

#     if 'search[value]' in kwargs:
#         search_value = kwargs.get('search[value]', None)[0]
#     elif 'search' in kwargs:
#         search_value = kwargs.get('search', None)[0]
#     else:
#         search_value = ''

#     if 'order[0][column]' in kwargs:
#         order_column = kwargs.get('order[0][column]', None)[0]
#     else:
#         order_column = '0'

#     if 'order[0][dir]' in kwargs:
#         order = kwargs.get('order[0][dir]', None)[0]
#     else:
#         order = 'asc'

#     order_column = ORDER_COLUMN[order_column]

#     # # django orm '-' -> desc
#     if order == 'desc':
#         order_column = '-' + order_column

#     total = queryset.count()

#     if search_value:
#         queryset = queryset.filter(models.Q(id__icontains=search_value)|
#                                    models.Q(inventory__serial__icontains=search_value) |
#                                    models.Q(station_origin__name__icontains=search_value) |
#                                    models.Q(station_received__name__icontains=search_value) |
#                                    models.Q(station_destination__name__icontains=search_value) |
#                                    models.Q(client__document__icontains=search_value) |
#                                    models.Q(client__name__icontains=search_value))

#     count = queryset.count()
#     queryset = queryset.order_by(order_column)[start:start + length]
#     return {
#         'items': queryset,
#         'count': count,
#         'total': total,
#         'draw': draw
#     }


# # Transfer
# def query_transfers_by_args(queryset, **kwargs):
#     ORDER_COLUMN = Choices(
#         ('0', 'id'),
#         ('1', 'station_origin__name'),
#         ('2', 'station_received__name'),
#         ('3', 'convoyer__name'),
#         ('4', 'type'),
#         ('5', 'status'),
#     )

#     if 'draw' in kwargs:
#         draw = int(kwargs.get('draw', None)[0])
#     else:
#         draw = 0

#     if 'length' in kwargs:
#         length = int(kwargs.get('length', None)[0])
#     else:
#         length = queryset.count()

#     if 'start' in kwargs:
#         start = int(kwargs.get('start', None)[0])
#     else:
#         start = 0

#     if 'search[value]' in kwargs:
#         search_value = kwargs.get('search[value]', None)[0]
#     else:
#         search_value = ''

#     if 'order[0][column]' in kwargs:
#         order_column = kwargs.get('order[0][column]', None)[0]
#     else:
#         order_column = '0'

#     if 'order[0][dir]' in kwargs:
#         order = kwargs.get('order[0][dir]', None)[0]
#     else:
#         order = 'asc'

#     order_column = ORDER_COLUMN[order_column]

#     # # django orm '-' -> desc
#     if order == 'desc':
#         order_column = '-' + order_column

#     total = queryset.count()

#     if search_value:
#         queryset = queryset.filter(models.Q(id__icontains=search_value) |
#                                    models.Q(station_origin__name__icontains=search_value) |
#                                    models.Q(station_received__name__icontains=search_value) |
#                                    models.Q(convoyer__name__icontains=search_value) |
#                                    models.Q(type__icontains=search_value) |
#                                    models.Q(status__icontains=search_value))

#     count = queryset.count()
#     queryset = queryset.order_by(order_column)[start:start + length]
#     return {
#         'items': queryset,
#         'count': count,
#         'total': total,
#         'draw': draw
#     }


# # Incident
# def query_incidents_by_args(queryset, **kwargs):
#     ORDER_COLUMN = Choices(
#         ('0', 'id'),
#         ('1', 'inventory__serial'),
#         ('2', 'station__name'),
#         ('3', 'user_report__name'),
#         ('4', 'description'),
#         ('5', 'status__name'),
#     )

#     if 'draw' in kwargs:
#         draw = int(kwargs.get('draw', None)[0])
#     else:
#         draw = 0

#     if 'length' in kwargs:
#         length = int(kwargs.get('length', None)[0])
#     else:
#         length = queryset.count()

#     if 'start' in kwargs:
#         start = int(kwargs.get('start', None)[0])
#     else:
#         start = 0

#     if 'search[value]' in kwargs:
#         search_value = kwargs.get('search[value]', None)[0]
#     else:
#         search_value = ''

#     if 'order[0][column]' in kwargs:
#         order_column = kwargs.get('order[0][column]', None)[0]
#     else:
#         order_column = '0'

#     if 'order[0][dir]' in kwargs:
#         order = kwargs.get('order[0][dir]', None)[0]
#     else:
#         order = 'asc'

#     order_column = ORDER_COLUMN[order_column]

#     # # django orm '-' -> desc
#     if order == 'desc':
#         order_column = '-' + order_column

#     total = queryset.count()

#     if search_value:
#         queryset = queryset.filter(models.Q(id__icontains=search_value) |
#                                    models.Q(inventory__serial__icontains=search_value) |
#                                    models.Q(station__name__icontains=search_value) |
#                                    models.Q(user_report__name__icontains=search_value) |
#                                    models.Q(description__icontains=search_value) |
#                                    models.Q(status__name__icontains=search_value))

#     count = queryset.count()
#     queryset = queryset.order_by(order_column)[start:start + length]
#     return {
#         'items': queryset,
#         'count': count,
#         'total': total,
#         'draw': draw
#     }


# # Workshop
# def query_repairs_by_args(queryset, **kwargs):
#     ORDER_COLUMN = Choices(
#         ('0', 'id'),
#         ('1', 'inventory__serial'),
#         ('2', 'mechanic__name'),
#         ('3', 'workshop__name'),
#         ('4', 'description'),
#         ('5', 'status'),
#     )

#     if 'draw' in kwargs:
#         draw = int(kwargs.get('draw', None)[0])
#     else:
#         draw = 0

#     if 'length' in kwargs:
#         length = int(kwargs.get('length', None)[0])
#     else:
#         length = queryset.count()

#     if 'start' in kwargs:
#         start = int(kwargs.get('start', None)[0])
#     else:
#         start = 0

#     if 'search[value]' in kwargs:
#         search_value = kwargs.get('search[value]', None)[0]
#     else:
#         search_value = ''

#     if 'order[0][column]' in kwargs:
#         order_column = kwargs.get('order[0][column]', None)[0]
#     else:
#         order_column = '0'

#     if 'order[0][dir]' in kwargs:
#         order = kwargs.get('order[0][dir]', None)[0]
#     else:
#         order = 'asc'

#     order_column = ORDER_COLUMN[order_column]

#     # # django orm '-' -> desc
#     if order == 'desc':
#         order_column = '-' + order_column

#     total = queryset.count()

#     if search_value:
#         queryset = queryset.filter(models.Q(id__icontains=search_value) |
#                                    models.Q(inventory__serial__icontains=search_value) |
#                                    models.Q(mechanic__name__icontains=search_value) |
#                                    models.Q(workshop__name__icontains=search_value) |
#                                    models.Q(description__icontains=search_value) |
#                                    models.Q(status__icontains=search_value))

#     count = queryset.count()
#     queryset = queryset.order_by(order_column)[start:start + length]
#     return {
#         'items': queryset,
#         'count': count,
#         'total': total,
#         'draw': draw
#     }


# # Auth
# def query_groups_by_args(queryset, **kwargs):
#     ORDER_COLUMN = Choices(
#         ('0', 'id'),
#         ('1', 'name'),
#     )

#     if 'draw' in kwargs:
#         draw = int(kwargs.get('draw', None)[0])
#     else:
#         draw = 0

#     if 'length' in kwargs:
#         length = int(kwargs.get('length', None)[0])
#     else:
#         length = queryset.count()

#     if 'start' in kwargs:
#         start = int(kwargs.get('start', None)[0])
#     else:
#         start = 0

#     if 'search[value]' in kwargs:
#         search_value = kwargs.get('search[value]', None)[0]
#     else:
#         search_value = ''

#     if 'order[0][column]' in kwargs:
#         order_column = kwargs.get('order[0][column]', None)[0]
#     else:
#         order_column = '0'

#     if 'order[0][dir]' in kwargs:
#         order = kwargs.get('order[0][dir]', None)[0]
#     else:
#         order = 'asc'

#     order_column = ORDER_COLUMN[order_column]

#     # # django orm '-' -> desc
#     if order == 'desc':
#         order_column = '-' + order_column

#     total = queryset.count()

#     if search_value:
#         queryset = queryset.filter(models.Q(id__icontains=search_value) |
#                                    models.Q(name__icontains=search_value))

#     count = queryset.count()
#     queryset = queryset.order_by(order_column)[start:start + length]
#     return {
#         'items': queryset,
#         'count': count,
#         'total': total,
#         'draw': draw
#     }


# # Vehicles -> InventoryCurrentList (Mobile)
# def query_inventory_current_by_args(queryset, **kwargs):
#     if 'length' in kwargs:
#         length = int(kwargs.get('length', None)[0])
#     else:
#         length = queryset.count()

#     if 'start' in kwargs:
#         start = int(kwargs.get('start', None)[0])
#     else:
#         start = 0

#     if 'search' in kwargs:
#         search = kwargs.get('search', None)[0]
#     else:
#         search = ''

#     total = queryset.count()

#     if search:
#         queryset = queryset.filter(models.Q(id__icontains=search) |
#                                    models.Q(vehicle__name__icontains=search) |
#                                    models.Q(serial__icontains=search))

#     count = queryset.count()
#     queryset = queryset[start:start + length]
#     return {
#         'items': queryset,
#         'count': count,
#         'total': total
#     }


# # Peoples -> ClientListMobile (Mobile)
# def query_clients_by_args(queryset, **kwargs):
#     if 'length' in kwargs:
#         length = int(kwargs.get('length', None)[0])
#     else:
#         length = queryset.count()

#     if 'start' in kwargs:
#         start = int(kwargs.get('start', None)[0])
#     else:
#         start = 0

#     if 'search' in kwargs:
#         search = kwargs.get('search', None)[0]
#     else:
#         search = ''

#     total = queryset.count()

#     if search:
#         queryset = queryset.filter(models.Q(id__icontains=search) |
#                                    models.Q(document__icontains=search) |
#                                    models.Q(name__icontains=search) |
#                                    models.Q(first_surname__icontains=search) |
#                                    models.Q(second_surname__icontains=search))

#     count = queryset.count()
#     queryset = queryset[start:start + length]
#     return {
#         'items': queryset,
#         'count': count,
#         'total': total
#     }


# # Renew
# def query_renew_by_args(queryset, **kwargs):
#     ORDER_COLUMN = Choices(
#         ('0', 'id'),
#         ('1', 'loan_vehicle__inventory__serial'),
#         ('2', 'station_renew__name'),
#         ('3', 'station_origin_old__name'),
#         ('4', 'station_received_old__name'),
#         ('5', 'loan_vehicle__station_received__name'),
#         ('6', 'loan_vehicle__client__document'),
#         ('7', 'loan_vehicle__client__name'),
#         ('8', 'loan_vehicle__received')
#     )

#     if 'draw' in kwargs:
#         draw = int(kwargs.get('draw', None)[0])
#     else:
#         draw = 0

#     if 'length' in kwargs:
#         length = int(kwargs.get('length', None)[0])
#     else:
#         length = queryset.count()

#     if 'start' in kwargs:
#         start = int(kwargs.get('start', None)[0])
#     else:
#         start = 0

#     if 'search[value]' in kwargs:
#         search_value = kwargs.get('search[value]', None)[0]
#     elif 'search' in kwargs:
#         search_value = kwargs.get('search', None)[0]
#     else:
#         search_value = ''

#     if 'order[0][column]' in kwargs:
#         order_column = kwargs.get('order[0][column]', None)[0]
#     else:
#         order_column = '0'

#     if 'order[0][dir]' in kwargs:
#         order = kwargs.get('order[0][dir]', None)[0]
#     else:
#         order = 'asc'

#     order_column = ORDER_COLUMN[order_column]

#     # # django orm '-' -> desc
#     if order == 'desc':
#         order_column = '-' + order_column

#     total = queryset.count()

#     if search_value:
#         queryset = queryset.filter(models.Q(id__icontains=search_value)|
#                                    models.Q(loan_vehicle__inventory__serial__icontains=search_value) |
#                                    models.Q(station_renew__name__icontains=search_value) |
#                                    models.Q(station_origin_old__name__icontains=search_value) |
#                                    models.Q(station_received_old__name__icontains=search_value) |
#                                    models.Q(loan_vehicle__station_received__name__icontains=search_value) |
#                                    models.Q(loan_vehicle__client__document__icontains=search_value) |
#                                    models.Q(loan_vehicle__client__name__icontains=search_value))

#     count = queryset.count()
#     queryset = queryset.order_by(order_column)[start:start + length]
#     return {
#         'items': queryset,
#         'count': count,
#         'total': total,
#         'draw': draw
#     }


# # RenewLoan 
# def query_alarm_by_args(queryset, **kwargs):
#     ORDER_COLUMN = Choices(
#         ('0', 'id'),
#         ('1', 'user__name'),
#         ('2', 'user__document'),
#         ('3', 'user_received__document'),
#         ('4', 'user_received__name'),
#         ('5', 'disabled_coordinates')
#     )

#     if 'draw' in kwargs:
#         draw = int(kwargs.get('draw', None)[0])
#     else:
#         draw = 0

#     if 'length' in kwargs:
#         length = int(kwargs.get('length', None)[0])
#     else:
#         length = queryset.count()

#     if 'start' in kwargs:
#         start = int(kwargs.get('start', None)[0])
#     else:
#         start = 0

#     if 'search[value]' in kwargs:
#         search = kwargs.get('search[value]', None)[0]
#     else:
#         search = ''

#     if 'order[0][column]' in kwargs:
#         order_column = kwargs.get('order[0][column]', None)[0]
#     else:
#         order_column = '0'

#     if 'order[0][dir]' in kwargs:
#         order = kwargs.get('order[0][dir]', None)[0]
#     else:
#         order = 'asc'

#     order_column = ORDER_COLUMN[order_column]

#     # # django orm '-' -> desc
#     if order == 'desc':
#         order_column = '-' + order_column

#     total = queryset.count()

#     if search:
#         queryset = queryset.filter(models.Q(id__icontains=search)|
#                                 models.Q(user__document__icontains=search)|
#                                 models.Q(user__name__icontains=search)|
#                                 models.Q(user_received__document__icontains=search)|
#                                 models.Q(user_received__name__icontains=search)|
#                                 models.Q(disabled_coordinates__icontains=search))

#     count = queryset.count()
#     queryset = queryset[start:start + length]
#     return {
#         'items': queryset,
#         'count': count,
#         'total': total,
#         'draw': draw
#     }

    
