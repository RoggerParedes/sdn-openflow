import json
from pox.lib.revent import EventMixin
from pox.core import core
import pox.forwarding.l2_learning as l2_learning
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr
from pox.lib.packet.ethernet import ethernet
from pox.lib.packet.ipv4 import ipv4

log = core.getLogger()
config = {} # Para que se pueda acceder desde la clase

class Firewall(EventMixin):
    def __init__(self):
        self.listenTo(core.openflow)

    def _handle_ConnectionUp(self, event):
        log.debug("Switch name:  %s", event.connection.ports[of.OFPP_LOCAL].name)
        if config["firewall"] == event.connection.ports[of.OFPP_LOCAL].name:
            rules = config["rules"]
            self.install_rule1(event, rules["rule_1"]["dst_port"])
            self.install_rule2(event, rules["rule_2"]["protocol"], rules["rule_2"]["dst_port"], rules["rule_2"]["src_eth"]) #udp, port5001, host1
            self.install_rule3(event, rules["rule_3"]["eth1"], rules["rule_3"]["eth2"])
            log.debug("Firewall rules installed on %s", dpidToStr(event.dpid))

    def install_rule1(self, event, dst_port):
        log.info("Installing rule 1 on port %s", dst_port)
        msg = of.ofp_flow_mod()
        msg.match.dl_type = ethernet.IP_TYPE
        msg.match.tp_dst = dst_port
        msg.match.nw_proto = ipv4.TCP_PROTOCOL
        event.connection.send(msg)

        msg2 = of.ofp_flow_mod()
        msg2.match.dl_type = ethernet.IP_TYPE
        msg2.match.tp_dst = dst_port
        msg2.match.nw_proto = ipv4.UDP_PROTOCOL
        event.connection.send(msg2)

    def install_rule2(self, event, protocol, dst_port, src_eth):
        log.info("Installing rule 2 - protocol: %s - port: %i - src_eth: %s", protocol, dst_port, src_eth)
        msg = of.ofp_flow_mod()
        msg.match.dl_type = ethernet.IP_TYPE
        if protocol == "tcp":
            msg.match.nw_proto = ipv4.TCP_PROTOCOL
        if protocol == "udp":	# podria haber otro que no sea udp?
            msg.match.nw_proto = ipv4.UDP_PROTOCOL
        msg.match.tp_dst = int(dst_port)
        msg.match.dl_src = EthAddr(src_eth)
        event.connection.send(msg)


    def install_rule3(self, event, eth1, eth2):
        log.info("Installing rule 3")
        msg = of.ofp_flow_mod()
        msg.match.dl_type = ethernet.IP_TYPE
        msg.match.dl_dst = EthAddr(eth1) # comunicación mac1->mac2
        msg.match.dl_src = EthAddr(eth2)
        event.connection.send(msg)
        msg2 = of.ofp_flow_mod()
        msg2.match.dl_type = ethernet.IP_TYPE
        msg2.match.dl_dst = EthAddr(eth2) # comunicación mac2->mac1
        msg2.match.dl_src = EthAddr(eth1)
        event.connection.send(msg2)

def parse_config(config_file):
        with open(config_file, 'r') as json_data:
            data = json.load(json_data)
        return data

def launch(config_file="rules.json"):
    log.debug("Starting Firewall")
    l2_learning.launch()
    global config
    config = parse_config(config_file)
    core.registerNew(Firewall)
