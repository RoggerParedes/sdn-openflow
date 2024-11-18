import os
import json
from pox.lib.revent import EventMixin
from pox.core import core
import pox.forwarding.l2_learning as l2_learning

log = core.getLogger()

class Firewall(EventMixin):
    def __init__(self):
        self.listenTo(core.openflow)
        log.debug("Estableciendo modulo del firewall")

    def _handle_ConnectionUp(self, event):
        log.debug("Conexion establecida.")


def parse_config(config_file):
        with open(config_file, 'r') as json_data:
            data = json.load(json_data)
        return data

def launch(config_file="rules.json"):
    log.debug("Firewall establecido")
    l2_learning.launch()
    config = parse_config(config_file)
    core.registerNew(Firewall)
