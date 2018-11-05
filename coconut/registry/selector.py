from __future__ import absolute_import

import random

def RandomService(services):
    if len(services) == 0:
        return None
    index = random.randint(0, len(services) - 1)
    return services[index]