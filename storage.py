class Storage:
    def __init__(self, data={}):
        super().__init__()
        if isinstance(data, dict):
            self.data = data
        else:
            raise Exception

    def get(self, key):
        if key in self.data:
            return self.data[key]
        else:
            return None

    def remove(self, key):
        if key in self.data.keys():
            del self.data[key]
            return self.data
        else:
            raise KeyError


    def set(self, key, value):
        if key in self.data:
            self.data[key] = value
        else:
            return None
    
    def add(self, key, value):
        self.data[key] = value

