# CSI2470 MITM Attack Code

A Python-based tool that uses the Scapy library to conduct ARP spoofing (ARP poisoning) within a local subnet. This script enables an attacker to send forged ARP reply packets to a victim machine, tricking it into associating the attacker's MAC address with the gateway IP address. This positions the attacker as a "Man in the Middle," enabling packet sniffing and interception.

---

## 📚 Overview

The script performs **unidirectional ARP spoofing** by sending forged ARP reply packets to the target machine, making it believe the attacker is the gateway. Although only spoofing the victim in this version, it can be extended to spoof the gateway as well, forming a full man-in-the-middle (MITM) attack.

## 🧪 Tested Environment

- **Attacker:** Kali Linux VM (`192.168.0.80`)
- **Victim:** Ubuntu VM (`192.168.0.70`)
- **Gateway:** MacBook host (`192.168.0.158`)
- All devices on the same subnet: `192.168.0.0/24`

## 🛠️ Requirements

- Python 3.x
- Scapy
- Root privileges

Install Scapy using pip:

```bash
pip install scapy
```

---

## 🚀 Usage

```bash
sudo python3 arp_spoof.py --target <victim_IP> --spoof <gateway_IP> --interface <network_interface>
```

### Example

```bash
sudo python3 arp_spoof.py --target 192.168.0.70 --spoof 192.168.0.158 --interface eth0
```

---

## 📂 Arguments

| Argument       | Description                              |
|----------------|------------------------------------------|
| `--target`     | IP address of the victim device          |
| `--spoof`      | IP address of the gateway to impersonate |
| `--interface`  | Network interface to send packets from   |

---

## 🔍 What It Does

1. Constructs ARP "reply" packets claiming the spoof IP is at the attacker's MAC.
2. Sends these forged ARP replies to the victim every 2 seconds.
3. Alters the victim's ARP table to associate the gateway IP with the attacker's MAC.
4. Enables potential packet sniffing using a tool like Wireshark on the attacker machine.

---

## 📸 Demonstration Highlights

- Successfully spoofed the ARP table on the Ubuntu VM victim.
- Verified ARP table changes using `arp -a`.
- Captured DNS and HTTPS traffic from the victim using Wireshark on the attacker machine.

---

## 🧹 Cleanup

To restore normal network operation, run the following on the victim machine:

```bash
arp -d *
```

Or reboot the machine to flush the ARP cache.

---

## 🔐 Defense & Mitigation

- Use HTTPS to encrypt traffic.
- Employ static ARP tables where possible.
- Use managed switches with Dynamic ARP Inspection (DAI).
- Deploy intrusion detection systems (IDS) to monitor spoofing activity.

---

## 📎 Appendix: Device Info

| Device              | IP Address       | MAC Address          |
|---------------------|------------------|-----------------------|
| **Macbook (Gateway)** | 192.168.0.158/24 | 06:1f:9e:02:fe:17     |
| **Kali VM (Attacker)** | 192.168.0.80/24  | 08:00:27:04:42:0f     |
| **Ubuntu VM (Victim)** | 192.168.0.70/24  | 08:00:27:ff:6c:08     |

---

## 🧠 Author

**Kaeden Bryer**  
CSI 2470 –– Man-in-the-Middle Attack Assignment
Date: 19 April 2025
