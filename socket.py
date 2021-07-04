import socket

def check_port(ip, port):
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        TCPsock.settimeout(5)
        TCPsock.connect((ip, port))
        TCPsock.settimeout(0)
        return True
    except:
        return False

def main():
    server1, server2, server3, server4 = '10.11.12.22', '10.11.12.23', '10.11.12.24', '10.11.12.25'
    ips = [server1, server2, server3, server4]
    port1, port2, port3, port4 = 3044, 3044, 4044, 4044
    ports = [port1, port2, port3, port4]

    i = 1
    for ip, port in zip(ips, ports):
        res = check_port(ip, port)
        print(f"MainServer --> Server{i} [{'OK' if res else 'Error'}]")
        res = check_port("127.0.0.1", port)
        print(f"Server{i} ({ip}) --> MainServer [{'OK' if res else 'Error'}]")
        i += 1

if __name__ == "__main__":
    main()
