from pyramid.view import view_config
from pyramid.response import Response
from sqlalchemy.exc import SQLAlchemyError

from .. import models


def get_orders(dbsession):
    """ Запрос со списком заказов """
    return dbsession.query(models.Order)


@view_config(route_name='home', renderer='subtotal_test:templates/mytemplate.jinja2')
def my_view(request):
    try:
        query = get_orders(request.dbsession)
    except SQLAlchemyError:
        return Response(
            "Ошибка при обращении к БД",
            content_type='text/plain',
            status=500
        )
    return {
        'amount': query.count(),
        'project': 'subtotal_test'
    }


@view_config(route_name='home_json', renderer='json')
def my_view_json(request):
    query = get_orders(request.dbsession)
    return {
        'amount': query.count(),
        'project': 'subtotal_test'
    }
