from core.pox import core

log = core.getLogger()
congif = {}

class Firewall(EventMixin):
    def __init__(self):
        self.listenTo(core.openflow)
        log.debug("Estableciendo modulo del firewall")

    def _handle_ConnectionUp(self, event):
        log.debug("Conexion establecida.")

    def launch(self):
        log.debug("Firewall iniciado...")
