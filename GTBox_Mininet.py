from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.link import TCLink
from SEDSS.CLIMessage import CLIMessage

class GTBox_Mininet:

    def start_network(self, topo):
        net = Mininet(topo=topo, link=TCLink)
        net.start()
        CLI(net)
        net.stop()

    def buildSingle(self, num_hosts):
        self.start_network(singleTopology(num_hosts))

    def buildLinear(self, num_hosts):
        self.start_network(linearTopology(num_hosts))

    def buildTree(self, num_hosts, depth, fanout):
        self.start_network(treeTopology(num_hosts, depth, fanout))

class linearTopology(Topo):
    def build(self, num_hosts):
        last_switch = None
        for i in range(1, num_hosts + 1):
            host = self.addHost(f'h{i}')
            switch = self.addSwitch(f's{i}')
            self.addLink(host, switch)
            CLIMessage(f"Adding host {host} to switch {switch}", "I")
            if last_switch:
                self.addLink(switch, last_switch)
            last_switch = switch

class singleTopology(Topo):
    def build(self, num_hosts):
        switch = self.addSwitch('s1')
        for i in range(1, num_hosts + 1):
            host = self.addHost(f'h{i}')
            self.addLink(host, switch)
            CLIMessage(f"Adding host {host} to switch {switch}", "I")

class treeTopology(Topo):
    def build(self, num_hosts, depth, fanout):
        def add_tree(depth, parent):
            if depth == 0: return
            for i in range(fanout):
                child = self.addSwitch(f's{depth}-{i}')
                self.addLink(parent, child)
                CLIMessage(f"Linking parent switch {parent} to switch {child}", "I")
                add_tree(depth - 1, child)
                if depth == 1:
                    host = self.addHost(f'h{child}')
                    self.addLink(host, child)
                    CLIMessage(f"Adding host {host} to switch {child}", "I")

        root_switch = self.addSwitch('s0')
        add_tree(depth, root_switch)

# # Usage Example
# network = GTBox_Mininet()
# network.buildTree(10, 2, 2)  # Example to build a tree topology
