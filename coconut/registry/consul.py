from __future__ import absolute_import

import consul


class Registry(object):

    def __init__(
            self,
            host='127.0.0.1',
            port=8500):
        self.c = consul.Consul(host, port)

    def register(self, service):
        self.c.agent.service.register(
            service.name,
            service_id=service.service_id,
            address=service.address,
            port=service.port)

    def deregister(self, service):
        self.c.agent.service.deregister(
            service.service_id)
