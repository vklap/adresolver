from app.infrastructure import repositories, providers
from app.domain import services, factories


def async_resolve_data(connection_wrapper):
    session_id = factories.create_session_id()
    transformer = _extract_transformer(connection_wrapper)

    repositories.save_session_transformer(session_id, transformer.transformer_id)
    providers.store_connection_wrapper(session_id, connection_wrapper)

    providers.send_session_to_queue(session_id)

    return session_id


def render_resolved_data(connection_wrapper):
    transformer = _extract_transformer(connection_wrapper)
    connection_wrapper.send_streamed_response(transformer)


def handle_async_render_resolved_data(session_id):
    transformer = repositories.get_transformer_by_session(session_id)
    connection_wrapper = providers.get_connection_wrapper_by_session(session_id)
    connection_wrapper.send_streamed_response(transformer)


def _extract_transformer(connection_wrapper):
    transformer_id = services.extract_ad_transformer_id(connection_wrapper)
    transformer = factories.create_ad_transformer(transformer_id)
    return transformer


