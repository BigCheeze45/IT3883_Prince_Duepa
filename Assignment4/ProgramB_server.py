# Program Name: ProgramB_server.py
# Course: IT3883/Section W02
# Student Name: Prince Duepa
# Assignment Number: Lab/Assignment 4
# Due Date: 03/24/2025
# Purpose: socket server
# List Specific resources used to complete the assignment
#   * https://tkdocs.com/index.html

import socket

# Socket configuration
HOST = '127.0.0.1'  # localhost
PORT = 50000        # arbitrary port above 40000

def main():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Allow port reuse
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Bind the socket to the host and port
    server_socket.bind((HOST, PORT))
    
    # Listen for connections
    server_socket.listen()
    print(f"Listening on {HOST}:{PORT}")
    
    try:
        while True:
            # Accept a connection
            client_socket, address = server_socket.accept()
            print(f"Connection from {address}")
            
            try:
                # Receive data
                data = client_socket.recv(1024).decode()
                if not data:
                    break
                
                print(f"Received: {data}")
                
                # Convert to uppercase and send back
                response = data.upper()
                client_socket.sendall(response.encode())
                print(f"Sent back: {response}")
                
            finally:
                # Close the client connection
                client_socket.close()
                print("Client connection closed.")
                
    except KeyboardInterrupt:
        print("Server shutting down...")
    finally:
        # Close the server socket
        server_socket.close()
        print("Server socket closed.")

if __name__ == "__main__":
    main()