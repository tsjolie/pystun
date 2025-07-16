import stun	# Import the STUN library for NAT detection
import socket	# Import socket for UDP socket creation

# Create a UDP socket
# STUN works over UDP, so we need a UDP socket bound to a local port
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 54320))		# Bind to all interfaces on port 54320 (can be any unused port)

# Call get_nat_type from the stun library to detect NAT behavior
# Arguments:
#   s: the socket to use for sending/receiving STUN packets
#   source_ip: local IP address to use (0.0.0.0 means any)
#   source_port: local port number (must match socket binding)
#   stun_host: STUN server hostname to query (Google’s public STUN server here)
#   stun_port: STUN server port (default 19302 for Google STUN)
result = stun.get_nat_type(
    s=sock,
    source_ip="0.0.0.0",
    source_port=54320,
    stun_host="stun.l.google.com",
    stun_port=19302
)

# The result is a tuple:
#   result[0] = NAT type string (e.g. "Full Cone", "Symmetric", etc.)
#   result[1] = dictionary with details about the external IP and port mapping
nat_type = result[0]
details = result[1]


# Print the NAT type (human-readable string)
print(f"NAT Type: {nat_type}")

# Print the external/public IP address assigned by the NAT/router
print(f"External IP: {details.get('ExternalIP')}")

# Print the external/public port mapped by the NAT/router
print(f"External Port: {details.get('ExternalPort')}")
