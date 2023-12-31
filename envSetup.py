# This class is used to build the network topology: 

from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import Host, OVSSwitch
from mininet.link import TCLink
from mininet.cli import CLI

class netTopology(Topo):
    def __init__(self, h=2, sw=1, gw=1):
        # initialization function that is executed whenever you call the class netTopology
        # by default, if you don't assign number of hosts, switchws and gateway default values 
        # will be added automatically -> hosts=2, switches=1, gw=1

        # initialization 
        self.hosts = h
        self.switches = sw
        self.gw = gw
        print ("Hello")

    def build(self):
        # Add 5 switches and 5 hosts
        switches = [self.addSwitch(f's{i}', cls=OVSSwitch) for i in range(1, 6)]
        hosts = [self.addHost(f'h{i}') for i in range(1, 6)]

        # Add links between switches and hosts
        for i in range(5):
            self.addLink(switches[i], hosts[i], cls=TCLink)

        # Connect switches in a linear topology
        for i in range(4):
            self.addLink(switches[i], switches[i+1])

