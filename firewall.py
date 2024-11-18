import os
import json
from pox.lib.revent import EventMixin
from pox.core import core

log = core.getLogger()
config = {}

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

    def launch(self):
        l2_learning.launch()
        global config
        config = parse_config(config_file)
        core.registerNew(Firewall)
        log.debug("Firewall iniciado...:")
