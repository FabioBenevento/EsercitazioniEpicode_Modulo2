import socket

ip_target="0.0.0.0"
port=4000

def udp_client(addr):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(addr)
    s.settimeout(1)
    print(f"In ascolto su porta {port}")
    try:
        while True:
            try:
                msg, address = s.recvfrom(1024)
                print(msg)
            except socket.timeout:
                pass 
    except KeyboardInterrupt:
        s.close()

def main():
    udp_client((ip_target, port))


if __name__ == "__main__":
    main()