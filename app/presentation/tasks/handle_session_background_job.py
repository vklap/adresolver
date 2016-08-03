from app.application import services


# The bellow method should be triggered by some queueing / pubsub mechanism (such as Celery)

def handle_session(session_id):
    try:
        services.handle_async_render_resolved_data(session_id)
    except Exception as ex:
        # TODO: log error