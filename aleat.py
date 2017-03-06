#/usr/bin/python3

class aleat:
    def parse(self, request, rest):
        """Parse the received request, extracting the relevant information.
        request: HTTP request received from the client
        rest:    rest of the resource name after stripping the prefix
        """

        return None

    def process(self, parsedRequest):
        """Process the relevant elements of the request.
        Returns the HTTP code for the reply, and an HTML page.
        """
        import random
        return ("200 OK", "<html><body><p>Hola, " +
                          "<a href='" + str(random.randint(1, 100000000)) + "'>Dame otra</a>" +
                          "</p></body></html>")
