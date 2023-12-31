# This is the main program the runs GTBox. 
# created by MZ on Dec 31, 2023.
# Version control: V0.01

from envSetup import netTopology 


netTopology(h=2, sw=2,gw=1)

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
