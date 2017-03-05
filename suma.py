#/usr/bin/python3
import webapp


class suma(webapp.app):
    def __init__(self):
        self.first = True
        self.op = 0

    def parse(self, request, rest):
        return rest

    def process(self, parsedRequest):
        if first:
            try:
                self.op = int(parsedRequest)
            except ValueError:
                return ("HTTP/1.1 404 Not Found, <html><body><p>Introduzca un operando valido</p></body></html>\r\n")
            self.first = False
            return ("HTTP/1.1 200 OK","<html><body><p>Me has dado un " + str(self.op) + ". Dame mas</p></body></html>")
        else:
            try:
                res = self.op + int(parsedRequest)
            except ValueError:
                return ("HTTP/1.1 404 Not Found, <html><body><p>Introduzca un operando valido</p></body></html>\r\n")
            self.first = True
            return ("HTTP/1.1 200 OK","<html><body>" +
                                    "<p>Me habías dado un " + str(self.op) +
                                    ". Ahora un " + parsedRequest +
                                    ". Suman" + str(res) + "</p></body></html>")
