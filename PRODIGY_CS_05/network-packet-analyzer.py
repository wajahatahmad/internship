from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto
        print(f"Source IP: {ip_src} -> Destination IP: {ip_dst} | Protocol: {protocol}")
        if packet.haslayer(TCP):
            print(f"TCP Payload: {packet[TCP].payload}")
        elif packet.haslayer(UDP):
            print(f"UDP Payload: {packet[UDP].payload}")

sniff(prn=packet_callback, count=10)  # Adjust count or remove it for continuous capture
