from socket import *
import time
import sys

def ping(host, port):
    resps = []
    rtts = []
    loss = 0

    clientSocket = socket(AF_INET, SOCK_DGRAM)
    addr = (host, port)
    clientSocket.settimeout(1)

    for seq in range(1, 11):
        # Send ping message to server and wait for response back
        # On timeouts, you can use the following to add to resps
        # resps.append((seq, ‘Request timed out’, 0))
        # On successful responses, you should instead record the server response and the
        # RTT(must compute server_reply and rtt properly)
        # resps.append((seq, server_reply, rtt))

        # Fill in start
        start = time.time()
        message = "Ping " + str(seq) + " " + time.ctime(start)
        clientSocket.sendto(message.encode(), addr)
        try:
            modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
            end = time.time()
            rtt = end - start
            rtts.append(rtt)
            server_reply = modifiedMessage.decode()
            print(server_reply)
            print(rtt)
            resps.append((seq, server_reply, rtt))
        except timeout:
            loss += 1
            resps.append((seq, "Request timed out", 0))

    print("Max RTT" + str(max(rtts)))
    print("Min RTT" + str(min(rtts)))
    print("Avg RTT" + str(sum(rtts)/len(rtts)))
    print("Packet Loss %" + str(loss/10 * 100))

    clientSocket.close()
        # Fill in end

    return resps

if __name__ == '__main__':
    resps = ping('127.0.0.1', 12000)
    print(resps)