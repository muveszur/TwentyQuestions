import socket
import struct
import sys
import random

server_address = (sys.argv[1], int(sys.argv[2]))

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(server_address)

unpacker = struct.Struct('I 1s')
packer = struct.Struct('1s')

result = None
result_string = "N"
got_operator = None
random_number = random.randint(0, 101)

print ("The random number is :", random_number)

while True:
    try:

        data, client_addr = server.recvfrom(200)
        unpacked_data = unpacker.unpack(data)

        print ("The clients guess: ", unpacked_data[0], unpacked_data[1].decode(), random_number)
        got_operator = unpacked_data[1].decode()
        got_number = unpacked_data[0]

        if (got_operator == "<"):
            if (got_number < random_number):
                result_string = "I"
            else:
                result_string = "N"
        if (got_operator == ">"):
            if (got_number > random_number):
                result_string = "I"
            else:
                result_string = "N"
        if (got_operator == "="):
            if (got_number == random_number):
                result_string = "Y"
            else:
                result_string = "K"

        server.sendto(str(result_string).encode(), client_addr)
    except socket.timeout:
        pass


