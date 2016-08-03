class ConnectionWrapper(object):
    def __init__(self, http_socket):
        self._http_socket = http_socket

    @property
    def uri(self):
        # TODO: extract URI
        pass

    def send_streamed_response(self, transformer):
        # TODO: start reading html data in chunks from http_socket.
        # TODO: make sure that the data contains full strings (as you can't find and replace partial domains)
        html_data = None

        tranformed_data = transformer.tranform_data(html_data)

        # TODO: render transformed_data as chunks to client with http_socket (one caveat with this approach: we won't be able to send the "length" of the response to the client

