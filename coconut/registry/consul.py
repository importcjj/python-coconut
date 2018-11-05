from __future__ import absolute_import

import consul
from coconut.registry.service import Service


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

    def get_service(self, service_name):
        _, services = self.c.health.service(service_name)

        service_map = {}
        for service in services:
            service_id = service['Service']['ID']
            if service_id not in service_map:
                service_map[service_id] = Service(
                    name=service['Service']['Service'],
                    service_id=service['Service']['ID'],
                    kind=service['Service']['Kind'],
                    address=service['Service']['Address'],
                    port=service['Service']['Port'])

        return [service_map[id] for id in service_map]
