import logging
import socketserver
import json
from nginx_to_mongodb import helper
import uuid
from mongoengine import Document, connect, StringField, DateTimeField

HOST, PORT = "0.0.0.0", 514

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger("nginx-to-monogdb:syslog-server")
LOG.setLevel(logging.INFO)

class NginxLogHandeler(socketserver.BaseRequestHandler):
    
    def handle(self):
        data = bytes.decode(self.request[0].strip())
        LOG.info("New nginx Log received!")
        socket = self.request[1]
        clear = data[data.find("{"):]
        parsed = json.loads(clear)
        self.export_log(parsed)

    def export_log(self, parsed):
        pid = str(uuid.uuid4())
        record = helper.log_record(
            rec_id = pid,
            rec_date = parsed["time"],
            user_agent = parsed["http_user_agent"],
            response_code = parsed["status"]
        )
        record.save()
        LOG.info("Nginx Log recorded: %r" % record)

def main():
    helper.initialize()
    server = socketserver.UDPServer((HOST, PORT), NginxLogHandeler)
    server.serve_forever(poll_interval=0.5)

if __name__ == "__main__":
    main()