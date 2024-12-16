from scapy.all import IP, ICMP, sr1

def traceroute_vulnerable(destination):
    for ttl in range(1, 255):  # No max hops or timeout
        pkt = IP(dst=destination, ttl=ttl) / ICMP()
        reply = sr1(pkt, verbose=0)
        if reply is None:
            continue
        elif reply.type == 0:
            print(f"Reached {destination} at {ttl} hops")
            break

if __name__ == "__main__":
    traceroute_vulnerable("8.8.8.8")
