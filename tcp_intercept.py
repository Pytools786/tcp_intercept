import scapy.all as scapy

def sniff(interface):
    scapy.sniff(iface=interface , store= False, prn= process_sniff_pkt , filter='tcp port 12345')

def process_sniff_pkt(packet):
    print(packet.show())
    	

print('''


 (        )             )      )   (     (     
 )\ )  ( /(   *   )  ( /(   ( /(   )\ )  )\ )  
(()/(  )\())` )  /(  )\())  )\()) (()/( (()/(  
 /(_))((_)\  ( )(_))((_)\  ((_)\   /(_)) /(_)) 
(_)) __ ((_)(_(_())   ((_)   ((_) (_))  (_))   
| _ \\ \ / /|_   _|  / _ \  / _ \ | |   / __|  
|  _/ \ V /   | |   | (_) || (_) || |__ \__ \  
|_|    |_|    |_|    \___/  \___/ |____||___/  
                                               


 ''')
sniff("eth0")
