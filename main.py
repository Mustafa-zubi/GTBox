# This is the main program the runs GTBox. 
# created by MZ on Dec 31, 2023.
# Version control: V0.01

from GTBox import simNetwork, GTBox

GTBox("ff", "DDoS")
# Example usage:


network_instance = simNetwork ("mn", 3,3,1)

# Now you have 'network_instance' which is an instance of either simNetwork or phyNetwork.
# You can use it as needed.


# def main():
#     topo = CustomTopology()
#     net = Mininet(topo=topo, controller=None)  # Use the default controller

#     # Set IP addresses and default gateway for hosts
#     for i in range(1, 6):
#         host = net.get(f'h{i}')
#         host.setIP(f'10.0.0.{i}/24')
#         host.setDefaultRoute('via 10.0.0.6')  # Assuming the gateway is h6

#     net.start()

#     # Start the Mininet CLI
#     CLI(net)

#     net.stop()

# if __name__ == '__main__':
#     main()
