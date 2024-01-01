from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.link import TCLink

class GTBox_Mininet:

    def buildSingle(self, num_hosts):
        """
        Adding all hosts to a single switch
        """
        topo = singleTopology(num_hosts=num_hosts)
        net = Mininet(topo=topo, link=TCLink)
        net.start()
        CLI(net)
        net.stop()

    def buildLinear(self, num_hosts):
        """
        Creating a linear topology with the specified number of hosts
        """
        topo = linearTopology(num_hosts=num_hosts)
        net = Mininet(topo=topo, link=TCLink)
        net.start()
        CLI(net)
        net.stop()

class linearTopology(Topo):
    def build(self, num_hosts):
        # switch = self.addSwitch('s1')

        for i in range(1, num_hosts + 1):
            host = self.addHost(f'h{i}')
            switch = self.addSwitch(f's{i}')
            self.addLink(host, switch)

class singleTopology(Topo):
    def build(self, num_hosts):
        switch = self.addSwitch('s1')

        for i in range(1, num_hosts + 1):
            host = self.addHost(f'h{i}')
            self.addLink(host, switch)


