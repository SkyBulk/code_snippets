import socket
import struct

# Function to fragment data into smaller packets
def fragment_data(data, max_packet_size):
    fragments = []
    offset = 0

    while offset < len(data):
        packet = data[offset:offset + max_packet_size]
        fragments.append(packet)
        offset += max_packet_size

    return fragments

# Function to reassemble fragments into original data
def reassemble_data(fragments):
    return b"".join(fragments)

# Simulated data to be transmitted
original_data = b"This is a sample message that needs to be fragmented for transmission."

# Maximum packet size for fragmentation
max_packet_size = 10

# Fragment the data
fragments = fragment_data(original_data, max_packet_size)

print(f"fragments {fragments}")
# Simulate transmission and reassembly
received_fragments = fragments  # In a real scenario, these would be received over the network

# Reassemble the received fragments
reassembled_data = reassemble_data(received_fragments)

# Print the reassembled data
print("Reassembled Data:", reassembled_data.decode())
