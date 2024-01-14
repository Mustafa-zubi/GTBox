from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI

class TreeTopo(Topo):
    def build(self, depth=1, fanout=2):
        if depth == 0:
            return

        # Create the parent switch
        parentSwitch = self.addSwitch('s%d' % depth)

        # Create child switches and hosts recursively
        for i in range(fanout):
            childSwitch = self.addSwitch('s%d-%d' % (depth, i))
            self.addLink(parentSwitch, childSwitch)
            self.build(depth - 1, fanout)

topo = TreeTopo(depth=3, fanout=2)  # Adjust depth and fanout as needed
net = Mininet(topo=topo)
net.start()

# Access the Mininet CLI for testing
CLI(net)

net.stop()
