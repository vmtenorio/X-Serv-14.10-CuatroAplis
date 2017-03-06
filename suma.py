#/usr/bin/python3

class suma:
    def __init__(self):
        self.first = True
        self.op = 0

    def parse(self, request, rest):
        return rest[1:]

    def process(self, parsedRequest):
        """Process the relevant elements of the request.
        Returns the HTTP code for the reply, and an HTML page.
        """
        if self.first:
            try:
                self.op = int(parsedRequest)
            except ValueError:
                return ("HTTP/1.1 404 Not Found", "<html><body><p>Introduzca un operando valido</p></body></html>\r\n")
            self.first = False
            return ("HTTP/1.1 200 OK","<html><body><p>Me has dado un " + str(self.op) + ". Dame mas</p></body></html>")
        else:
            try:
                res = self.op + int(parsedRequest)
            except ValueError:
                return ("HTTP/1.1 404 Not Found", "<html><body><p>Introduzca un operando valido</p></body></html>\r\n")
            self.first = True
            return ("HTTP/1.1 200 OK","<html><body>" +
                                    "<p>Me habias dado un " + str(self.op) +
                                    ". Ahora un " + parsedRequest +
                                    ". Suman " + str(res) + "</p></body></html>")
