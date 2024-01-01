from SEDSS.CLIMessage import CLIMessage
from SEDSS.CLIInputReq import CLIInputReq
from GTBox_Mininet import GTBox_Mininet

class GTBox:
    """Main GTBox class"""
    def __init__(self, net, att=None):
        self.net = net
        self.attType = att

class simNetwork(GTBox): 
	"""
		Main class to create emulated network. Currently, this class support:
		Mininet simulator: developed by Mustafa Zubi on Jan 1, 2024. 
	"""
	def __init__(self, net, hosts=2, switches=1, gateway=1):
	 	super().__init__(net)
	 	self.hosts = hosts
	 	self.switches = switches
	 	self.gateway = gateway

	 	CLIMessage ("Network type: {}, number of hosts: {}, number of switches: {} number of gateways: {}".format(self.net, self.hosts,self.switches,self.gateway), "I")
	 	if self.net.lower() in {"mn", "mininet"}:
	 		self.mnNetwork()

	def mnNetwork (self):
		""" 
			Mininet virtual network creation
			developed by Mustafa Zubi on Jan 1, 2024. 
		"""
		answer = CLIInputReq ("Do you want to continue ?", "single").strInputReq()
		if answer.lower() in {"sin","single"}:
			""" validate inputes consistancy """
			if self.switches > 1: 
				CLIMessage ("Single topology means all hosts are connected to one switch", "I")
				CLIMessage ("In your setup, {} switches are provided.".format(self.switches), "I")
				CLIInputReq("Do you want to continue?").YNQuestion()

			GTBox_Mininet.buildSingle("single", self.hosts) #All hosts connected to single switch 

		elif answer.lower() in {"lin", "linear"}: 
			print("tttttt")
			GTBox_Mininet.buildLinear("linear", self.hosts)
		

class phyNetwork(GTBox):
    def __init__(self, net): 
        super().__init__(net)

