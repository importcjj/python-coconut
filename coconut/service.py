

class Service(object):

    def __init__(
        self,
        name,
        service_id,
        kind,
        address='0.0.0.0',
        port=0):
        
        self.name = name
        self.service_id = service_id
        self.kind = kind
        self.address = address
        self.port = port