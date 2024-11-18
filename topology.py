from mininet.topo import Topo

class InvalidNumberOfSwitches(Exception):
    pass

class ChainTopo(Topo):
    def __init__(self, number_of_switches, number_of_hosts_per_side=2):
        # Inicializar la topología
        Topo.__init__(self)

        if number_of_switches < 1:
            raise InvalidNumberOfSwitches(f"{number_of_switches} no es valido el número de switches")
        
        # Crear hosts iniciales
        left_hosts = [self.addHost(f'h{i}') for i in range(1, number_of_hosts_per_side + 1)]
        right_hosts = [self.addHost(f'h{i}') for i in range(number_of_hosts_per_side + 1, 2 * number_of_hosts_per_side + 1)]

        # Crear switches
        switches = [self.addSwitch(f's{i}') for i in range(1, number_of_switches + 1)]

        # Conectar hosts iniciales al primer switch
        for host in left_hosts:
            self.addLink(switches[0], host)

        # Conectar switches en cadena
        for i in range(len(switches) - 1):
            self.addLink(switches[i], switches[i + 1])

        # Conectar hosts finales al último switch
        for host in right_hosts:
            self.addLink(switches[-1], host)


topos = {'chain': ChainTopo}