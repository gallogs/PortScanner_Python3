#To communicate with other machines using TCP and UDP Protocols.
import socket



def scan(target, ports):
    print('\n' + ' Starting Scan For: ' + str(target))
    for port in range(1, ports):
        scan_port(target, port)
    


#Function that get 2 parameters (IP and Port)
def scan_port(ipaddress, port):
    try:
        #Initiate a socket object in Python
        #The object sock, calling the library, function from that library:
        sock = socket.socket()
        #Connect to our Target and to our Port:
        sock.connect((ipaddress, port))
        #Printing which Port are open
        print("[+] Port Opened: " + str(port))
        #Close the Object if found an open Port
        sock.close()
    except:
        #Printing wich Ports are closed
        #print("[-] Port Closed:" + str(port))
        pass


#Prompt for the users, what Target they want to Scan.

#Creating a Variable named "targets" to get the users answer:
targets = input("[*] Enter Targets To Scan( Split Them By ,): ")
#Getting the Ports from user:
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))

#Checking if there is a comma on the input
if ',' in targets:
    print("[*] Scanning Multiple Targets")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)
else:
    scan(targets, ports)