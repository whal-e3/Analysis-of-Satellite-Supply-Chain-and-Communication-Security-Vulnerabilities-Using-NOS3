#!/usr/bin/env python3
import socket
import struct

def packet_generator(torque):
    ccsds_packet_id = hex(0x1992)[2:]
    ccsds_packet_sc = "c000"
    packet_len = "0004"
    ccsds_fc = "03"
    checksum = "00"
    wheel_number = "00"
    torque_formatted = struct.pack('<H', torque).hex()

    packet = (
        ccsds_packet_id +
        ccsds_packet_sc +
        packet_len +
        ccsds_fc +
        checksum +
        wheel_number +
        torque_formatted
    )
    return packet
    
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip_address = input("Enter the ip address of sc_1_nos_fsw: ")
print()
port = int(input("Enter the port of sc_1_nos_fsw: "))
while True: 
    torque = int(input("Enter the torque value: "))
    packet = packet_generator(torque) 
    packet = bytes.fromhex(packet)
    try:
        sock.sendto(packet, (ip_address, port))
        print(f"Torque command sent to {ip_address}:{port}\n")
    except Exception as e:
        print(f"Failed to send command: {e}\n")
    finally:
        sock.close()

# Example IP, port configuration
# ip_address = "172.19.0.5"
# port = 5012
