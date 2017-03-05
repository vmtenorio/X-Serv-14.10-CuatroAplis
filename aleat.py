#/usr/bin/python3
import webapp


class aleat(webapp.app):
    def process(self, parsedRequest):
        import random
        return ("200 OK", "<html><body><p>Hola, " +
                          "<a href='" + str(random.randint(1, 100000000)) + "'>Dame otra</a>" +
                          "</p><p>App id: " + str(self) + "<p></body></html>")
