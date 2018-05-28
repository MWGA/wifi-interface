class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class State(object):
    __metaclass__ = Singleton
    auth = 1
    assoc = 2

    state = {"auth": {}, "assoc": {}}
    status = {}

    max_responses = 10
    dropped = 0
    active_scans = 0

    def set_authed(self, mac):
        self.status[mac] &= self.auth

    def set_assoced(self, mac):
        self.status[mac] &= self.assoc

    def is_authed(self, mac):
        if mac not in self.status:
            return False
        return self.status[mac] & self.auth

    def is_assoced(self, mac):
        if mac not in self.status:
            return False
        return self.status[mac] & self.assoc

    def can_respond(self, mac, process):
        if mac not in self.state[process]:
            self.state[process][mac] = 0
            return True
        return self.state[process][mac] < self.max_responses

    def add_response(self, mac, process):
        self.state[process][mac] = self.state[process][mac] + 1
