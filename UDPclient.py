import socket, time
import struct



def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    i = 1.0
    while True:
        i += 1
        s.sendto(struct.pack("f", i), ("127.0.0.1", 50000))
        print(f"Sent {i}")
        time.sleep(1)

if __name__ == "__main__":
    main()