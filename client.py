import socket
import struct
import sys

server_address = (sys.argv[1],int(sys.argv[2]))
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

notCorrect = True


def binary_search(low, high, operator="<"):

	if low <= high:
		if operator == "=":
			mid = high
		else:
			mid = round(((high + low) / 2))

		print("mid: ", mid, "low: ", low, "high: ", high)


		data = (int(mid), operator.encode())
		packer = struct.Struct('I 1s')
		packed_data = packer.pack(*data)

		client.sendto(packed_data, server_address)
		data, _ = client.recvfrom(200)
		result = data.decode()
		print(result)

		if result == "I":
			if high - mid <= 1:
				return binary_search(mid, high, "=")
			else:
				binary_search(mid, high)
		elif result == "N":
			if mid - low <= 1:
				return binary_search(low, mid, "=")
			else:
				binary_search(low, mid)
		elif result == "K":
			print("Game over loser")
			return False
		elif result == "Y":
			print("You won!")
			return False

while notCorrect:
    notCorrect = binary_search(0, 100, "<")
    