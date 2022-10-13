from socket import *
import sys
import base64

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver_163 = 'smtp.163.com'
mailserver_163_SMTP_Port = 25
mailserver_163_SMTP_LoginID = base64.b64encode(
    b'ceyewan@163.com').decode() + '\r\n'
mailserver_163_SMTP_Password = base64.b64encode(
    b'VYE*******XZE').decode() + '\r\n'

From = 'ceyewan@163.com'
To = 'ceyewan@qq.com'

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver_163, mailserver_163_SMTP_Port))
recv = clientSocket.recv(1024).decode()
print(recv, end='')
if recv[:3] != '220':
    print('220 reply not received from server.')
    clientSocket.close()
    exit(0)

# Send HELO command and print server response.
heloCommand = 'HELO ceyewan\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1, end='')
if recv1[:3] != '250':
    print('250 reply not received from server.')
    clientSocket.close()
    exit(0)

logCommand = 'AUTH LOGIN\r\n'
clientSocket.send(logCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2, end='')
if recv2[:3] != '334':
    print('334 login server goes wrong')
    clientSocket.close()
    exit(0)

clientSocket.send(mailserver_163_SMTP_LoginID.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3, end='')
if recv3[:3] == '535':
    print('Login ID wrong')
    clientSocket.close()
    exit(0)

clientSocket.send(mailserver_163_SMTP_Password.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4, end='')
if recv4[:3] == '535':
    print('Password wrong')
    clientSocket.close()
    exit(0)

fromCommand = 'MAIL FROM ' + '<' + From + '>' + '\r\n'
clientSocket.send(fromCommand.encode())
recv = clientSocket.recv(2048).decode()
print(recv, end='')
if recv[:3] != '250':
    print('Mail From server goes wrong')
    clientSocket.close()
    exit(0)


toCommand = 'RCPT TO: ' + '<' + To + '>' + '\r\n'
clientSocket.send(toCommand.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6, end='')
if recv6[:3] != '250':
    print('Mail to server goes wrong')
    clientSocket.close()
    exit(0)

beginCommand = 'DATA\r\n'
clientSocket.send(beginCommand.encode())
recv7 = clientSocket.recv(1024).decode()
print(recv7, end='')
if recv7[:3] != '354':
    print('Data Begin server goes wrong')
    clientSocket.close()
    exit(0)

# format
send = "From: " + From + '\r\n'
send += "To: " + To + '\r\n'
send += "Subject: " + "SMTP lab" + '\r\n'
send += msg
clientSocket.send(send.encode())
clientSocket.send(endmsg.encode())
recv8 = clientSocket.recv(1024).decode()
print(recv8, end='')
if recv8[:3] != '250':
    print('Data Transport goes wrong')
    clientSocket.close()
    exit(0)

endCommand = 'QUIT\r\n'
clientSocket.send(endCommand.encode())
recv9 = clientSocket.recv(1024).decode()
print(recv9, end='')
if recv9[:3] != '221':
    print('server end goes wrong')
    clientSocket.close()
    exit(0)
clientSocket.close()
