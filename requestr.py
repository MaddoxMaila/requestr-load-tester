from http.client import HTTPResponse
import sys
import urllib.parse as parser
from threading import Thread
import httplib2, sys
from queue import Queue

class Requestr:

    CONNECTION: httplib2.HTTPConnectionWithTimeout = None
    QUEUE: Queue = None
    THREAD: Thread = None

    REQ_URL: str = None

    def __init__(self) -> None:

        self.url: parser.ParseResultBytes = None
        self.response: HTTPResponse = None

    def make_request(self, url: str) -> tuple:

        try:
            self.url = parser.urlparse(url)

            self.CONNECTION = httplib2.HTTPConnectionWithTimeout(self.url.netloc)
            self.CONNECTION.request("HEAD", self.url.path)

            self.response = self.CONNECTION.getresponse()

            return "Status Code: {}".format(self.response.status), url

        except:
            return "Connection failed", url

    def set_req_url(self, url: str) -> None:
        self.REQ_URL = url

    def worker(self) -> None:
        
        while True:
            status, url = self.make_request(self.REQ_URL)
            print({"status": status, "url": url})
            self.QUEUE.task_done()

    def create_queue(self, concurrent: int) -> None:
        self.QUEUE = Queue(concurrent)
        try:
            self.thread_work(concurrent=concurrent)
        except KeyboardInterrupt:
            sys.exit(1)
    
    def thread_work(self, concurrent) -> None:

        for concur in range(concurrent):
            self.THREAD = Thread(target=self.worker())
            self.THREAD.daemon = True
            self.THREAD.start()

    def start(self) -> None:
        self.create_queue()

req = Requestr()
req.set_req_url("http://46.101.125.57:4000/v1/11111111111111111111111111111111/reverseGeocode/-27.013837,27.738462.json")
req.start()
