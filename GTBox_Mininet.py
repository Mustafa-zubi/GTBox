from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.link import TCLink
from SEDSS.CLIMessage import CLIMessage


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

    def buildTree(self, num_hosts, depth, fanout):
        """
        Creating a linear topology with the specified number of hosts
        """
        topo = treeTopology(num_hosts=num_hosts, depth = depth, fanout = fanout)
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
            CLIMessage("Adding host {} to switch {}".format(host, switch), "I")

class singleTopology(Topo):
    def build(self, num_hosts):
        switch = self.addSwitch('s1')

        for i in range(1, num_hosts + 1):
            host = self.addHost(f'h{i}')
            self.addLink(host, switch)
            CLIMessage("Adding host {} to switch {}".format(host, switch), "I")

class treeTopology(Topo):
    def build(self, num_hosts, depth, fanout):
        if depth == 0: 
            return
        parentSwitch = self.addSwitch ("s%d" % depth)
        for i in range(fanout):
            childSwitch = self.addSwitch("s%d-%d" % (depth, i))
            self.addLink (parentSwitch, childSwitch)
            CLIMessage("linking parent switch {} to switch {}".format(parentSwitch, childSwitch), "I")
            if (depth -1) == 0: 
                host = self.addHost(f'h{childSwitch}')
                self.addLink(host, childSwitch)
                CLIMessage("Adding host {} to switch {}".format(host, childSwitch), "I")
            self.build(num_hosts,depth -1, fanout)
            


