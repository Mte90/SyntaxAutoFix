import os

BASE_DIR = os.path.dirname(__file__)


class Subject(object):
    """Subject"""
    def __init__(self):
        self._data = None
        self._observers = set()

    def attach(self, observer):
        """Turn on notifications"""
        if not isinstance(observer, ObserverBase):
            raise TypeError()
        self._observers.add(observer)

    def detach(self, observer):
        """Turn off notifications"""
        self._observers.remove(observer)

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data
        self.notify(data)

    def notify(self, data):
        """Notify all observers for updates"""
        for observer in self._observers:
            observer.update(data)


class ObserverBase(object):
    """Abstract observer"""
    def update(self, data):
        raise NotImplementedError()


class Observer(ObserverBase):
    """observer"""
    def __init__(self, name):
        self._name = name
        self.observable = os.path.join(BASE_DIR, 'words/' + name + '.json')
        self._file = open(self.observable, "r").read()

    def update(self, data):
    	print("======================")
    	print('%s: %s' % (self._name, data))
