import socket
import argparse

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
    # server1, server2, server3, server4 = '10.11.12.22', '10.11.12.23', '10.11.12.24', '10.11.12.25'
    ips = [args.ip1,args.ip2,args.ip3,args.ip4]
    port1, port2, port3, port4 = 3044, 3044, 4044, 4044
    ports = [port1, port2, port3, port4]

    i = 1
    for ip, port in zip(ips, ports):
        res = check_port(ip, port)
        print(f"MainServer --> Server{i} [{'OK' if res else 'Error'}]")
        res = check_port("127.0.0.1", port)
        print(f"Server{i} ({ip}) --> MainServer [{'OK' if res else 'Error'}]")
        i += 1

def args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-ip1', type=str, help='Enter IP-1')
    parser.add_argument('-ip2', type=str, help='Enter IP-2')
    parser.add_argument('-ip3', type=str, help='Enter IP-3')
    parser.add_argument('-ip4', type=str, help='Enter IP-4')
    
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = args()
    if not args.ip1 :
        print("You have to Enter at least 1 IP Adress args ! See -h")
    else:
        main()
