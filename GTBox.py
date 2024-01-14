from SEDSS.CLIMessage import CLIMessage
from SEDSS.CLIInputReq import CLIInputReq
from GTBox_Mininet import GTBox_Mininet
import sys

class GTBox:
    """Main GTBox class"""
    def __init__(self, net, att=None):
        self.net = net
        self.attType = att

class simNetwork(GTBox): 
	"""
		Main class to cr eate emulated network. Currently, this class support:
		Mininet simulator: developed by Mustafa Zubi on Jan 1, 2024. 
	"""
	def __init__(self, net, hosts=2, switches=1, gateway=1):
	 	super().__init__(net)
	 	self.hosts 				= hosts
	 	self.switches 			= switches
	 	self.gateway 			= gateway
	 	self.netPlatform 		= None
	 	self.netPlatformReady 	= False 

	 	CLIMessage ("Network type: {}, number of hosts: {}, number of switches: {} number of gateways: {}".format(self.net, self.hosts,self.switches,self.gateway), "I")
	 	if self.net.lower() in {"mn", "mininet"}:
	 		self.netPlatform = "mn"
	 		self.mnNetwork()

	def mnNetwork (self):
		""" 
			Mininet virtual network creation
			developed by Mustafa Zubi on Jan 1, 2024. 
		"""
		answer = CLIInputReq ("Network topology, (1) single, (2) linear, (3) tree", "single").strInputReq()
		if answer.lower() in {"sin","single", "1"}:
			""" validate inputes consistancy """
			if self.switches > 1: 
				CLIMessage ("Single topology means all hosts are connected to one switch", "I")
				CLIMessage ("In your setup, {} switches are provided.".format(self.switches), "I")
				CLIInputReq("Do you want to continue?").YNQuestion()

			try:
				GTBox_Mininet.buildSingle("single", self.hosts) #All hosts connected to single switch
				self.netPlatformReady = True
			except:
				CLIMessage ("Problem building the MN/single virtual network", "E")
				self.netPlatformReady = False

		elif answer.lower() in {"lin", "linear", "2"}:
			try:
				GTBox_Mininet.buildLinear("linear", self.hosts)
				self.netPlatformReady = True
			except:
				CLIMessage ("Problem building the MN/linear virtual network", "E")
				self.netPlatformReady = False

		elif answer.lower() in {"tre", "tree", "3"}:
			depth 	= CLIInputReq ("Depth of your tree network?", 2).intInputReq()
			fanout 	= CLIInputReq ("Fanout of your tree network?", 2).intInputReq()
			if depth == 0:
				CLIMessage ("0 depth is not applicable!!", "E")
				sys.exit()
			try:
				GTBox_Mininet.buildTree("tree", self.hosts, depth, fanout)
				self.netPlatformReady = True
			except:
				CLIMessage ("Problem building the MN/tree virtual network", "E")
				self.netPlatformReady = False

		

class phyNetwork(GTBox):
    def __init__(self, net): 
        super().__init__(net)

