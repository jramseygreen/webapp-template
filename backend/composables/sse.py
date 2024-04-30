from queue import Queue
from flask import Response
from json import dumps

class __Sse:
    def __init__(self):
        self.__listeners = {}

    def listen(self, user_id: int) -> Response:
        q = Queue(maxsize=5)
        if not self.__listeners[user_id]:
            self.__listeners[user_id] = []
        self.__listeners[user_id].append(q)

        # generator for flask response
        def stream():
            while True:
                msg = q.get()
                if q.full() or msg == 'stop':
                    break
                yield 'event: message\ndata: ' + dumps(msg) + '\n\n'

        response =  Response(stream(), content_type='text/event-stream')
        response.headers['Cache-Control'] = 'no-cache'
        response.headers['X-Accel-Buffering'] = 'no'
        return response

    def announce(self, event: str, data):
        for user_id in self.__listeners:
            self.send(user_id, event, data)

    def send(self, user_id: int, event: str, data):
        msg = 'event: ' + event + '\ndata: ' + dumps(data) + '\n\n'
        for q in self.__listeners[user_id]:
            try:
                q.put_nowait(msg)
            except queue.Full:
                self.__listeners[user_id].remove(q)
                if not self.__listeners[user_id]:
                    del self.__listeners[client]

    def stop(self):
        for user_id in list(self.__listeners):
            for q in self.__listeners[user_id]:
                q.put_nowait('stop')

sse = __Sse()
