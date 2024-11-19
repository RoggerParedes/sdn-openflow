from mininet.topo import Topo

class InvalidNumberOfSwitches(Exception):
    pass

class ChainTopo(Topo):
    def __init__(self, number_of_switches, number_of_hosts_per_side=2):
        Topo.__init__(self)

        if number_of_switches < 1:
            raise InvalidNumberOfSwitches(f"{number_of_switches} no es válido el número de switches")
        
        def generate_mac(index):
            return f"00:00:00:00:00:{index:02x}"
        
        left_hosts = [
            self.addHost(f'h{i}', mac=generate_mac(i)) 
            for i in range(1, number_of_hosts_per_side + 1)
        ]

        right_hosts = [
            self.addHost(f'h{i}', mac=generate_mac(i)) 
            for i in range(number_of_hosts_per_side + 1, 2 * number_of_hosts_per_side + 1)
        ]

        switches = [self.addSwitch(f's{i}') for i in range(1, number_of_switches + 1)]

        for host in left_hosts:
            self.addLink(switches[0], host)

        for i in range(len(switches) - 1):
            self.addLink(switches[i], switches[i + 1])

        for host in right_hosts:
            self.addLink(switches[-1], host)

topos = {'chain': ChainTopo}
