from __future__ import absolute_import

import consul


class Registry(object):

    def __init__(self):
        self.c = consul.Consul()

    def register(self, service):
        self.c.agent.service.register(
            service.name,
            service_id=service.service_id,
            address=service.address,
            port=service.port)

    def deregister(self, service):
        self.c.agent.service.deregister(
            service.service_id)
