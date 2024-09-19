import socket, time
import struct



def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("0.0.0.0", 50000))
    while True:
        by,addr = s.recvfrom(1024)
        f = struct.unpack("f", by)
        print(f"Recieved {f} from {addr}")

if __name__ == "__main__":
    main()