from scapy.all import *

def main():
    while(True):
        packet = sniff(iface = "enp0s8")
        print(packet.show())
        sendp(packet, iface = "enp0s9")
        

if __name__ == "__main__":
    main()

