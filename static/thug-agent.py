from thug.ThugAPI import ThugAPI
from flask import Flask

app = Flask(__name__)


# 참고 레퍼런스
# http://containertutorials.com/docker-compose/flask-simple-app.html
# todo  thug에서 수행 할 url 을 request param으로 받아서 실행하는 것 추가 필요 
@app.route('/')
def hello_world():
    t = TestAPI()
    t.analyze("http://www.google.com")
    return 'Hello World!'


class TestAPI(ThugAPI):
    def __init__(self):
        ThugAPI.__init__(self)

    def analyze(self, url):
        # Set useragent to Internet Explorer 9.0 (Windows 7)
        self.set_useragent('win7ie90')

        # Set referer to http://www.honeynet.org
        self.set_referer('http://www.honeynet.org')

        # Enable file logging mode
        self.set_file_logging()

        # Enable JSON logging mode (requires file logging mode enabled)
        self.set_json_logging()

        # Enable MAEC 1.1 logging mode (requires file logging mode enabled)
        self.set_maec11_logging()

        # [IMPORTANT] The following three steps should be implemented (in the exact
        # order of this example) almost in every situation when you are going to
        # analyze a remote site.

        # Initialize logging
        self.log_init(url)

        # Run analysis
        self.run_remote(url)

        # Log analysis results
        self.log_event()

if __name__ == "__main__":
    print('start');
    app.run(host='0.0.0.0')

