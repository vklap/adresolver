import logging

from app.application import services
from app.infrastructure import providers, repositories

_log = logging.getLogger(__name__)

# The bellow public methods should be exposed as HTTP Web Methods (i.e. website endpoints)


def handle_direct():
    try:
        # TODO: use http_connection (depends on used HTTP server framework)
        http_connection = None
        connection_wrapper = _extract_connection_wrapper(http_connection)
        services.render_resolved_data(connection_wrapper)
    except Exception as e:
        # TODO: log error


def handle_indirect():
    try:
        # TODO: use http_connection (depends on used HTTP server framework)
        http_connection = None
        connection_wrapper = _extract_connection_wrapper(http_connection)
        services.async_resolve_data(connection_wrapper)
    except Exception as e:
        # TODO: log error

def _extract_connection_wrapper(http_connection):
    #TODO: create and return connection wrapper
    pass