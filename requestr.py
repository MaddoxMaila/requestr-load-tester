from http.client import HTTPResponse
import urllib.parse as parser
from threading import Thread
import httplib2, sys
from queue import Queue

class Requestr:

    CONNECTION = None
    QUEUE = None

    def __init__(self) -> None:

        self.url: parser.ParseResultBytes = None
        self.response: HTTPResponse = None

    def make_request(self, url: str) -> tuple:

        try:
            self.url = parser.urlparse(url)

            self.CONNECTION = httplib2.HTTPConnectionWithTimeout(self.url.netloc)
            self.CONNECTION.request("HEAD", self.url.path)

            self.response = self.CONNECTION.getresponse()

            return self.response.status, url

        except:
            return "Connection failed", url

req = Requestr()

print(req.make_request("http://46.101.125.57:4000/v1/11111111111111111111111111111111/reverseGeocode/-27.013837,27.738462.json"))

