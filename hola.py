#/usr/bin/python3
import webapp


class hola(webapp.app):
    def process(self, parsedRequest):
        return ("200 OK", "<html><body><h1>Hola!!!</h1>" +
                          "<p>App id: " + str(self) + "<p></body></html>")

class adios:
    def process(self, parsedRequest):
        return ("200 OK", "<html><body><h1>Adiós!!!</h1>" +
                          "<p>App id: " + str(self) + "<p></body></html>")
