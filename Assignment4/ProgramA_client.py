# Program Name: ProgramA_client.py
# Course: IT3883/Section W02
# Student Name: Prince Duepa
# Assignment Number: Lab/Assignment 4
# Due Date: 03/24/2025
# Purpose: socket client
# List Specific resources used to complete the assignment
#   * https://docs.python.org/3/library/socket.html
#   * https://www.geeksforgeeks.org/socket-programming-python/
#   * https://realpython.com/python-sockets/

import socket

# Socket configuration
HOST = '127.0.0.1'  # localhost
PORT = 50000        # arbitrary port above 40000

def main():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect to the server
        client_socket.connect((HOST, PORT))
        print(f"Connected to {HOST}:{PORT}")
        
        # Get input from user
        message = input("Enter a message: ")
        
        # Send the message
        client_socket.sendall(message.encode())
        print("Message sent.")
        
        # Receive the response
        response = client_socket.recv(1024).decode()
        print(f"Response received: {response}")
        
    except ConnectionRefusedError:
        print("Connection failed. Make sure Program B (server) is running.")
    finally:
        # Close the connection
        client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()