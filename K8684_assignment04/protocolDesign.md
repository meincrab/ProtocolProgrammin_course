# K8684 Alexander Andreev
# SIMPLE FILE TRANSFER PROTOCOL DESIGN DOCUMENT
## Description : 

This is a design document for simple file transfer protocol.  
Protocol MUST have two possible requsets LIST and DOWNLOAD and also two possible responses ERROR and FILE. Protocol MUST use sockets and SHOULD use TCP(Transmission Control Protocol) for connection and data transfering between CLIENT and SERVER. TCP is needed for making sure about integrity of sent and received data.  Client is sending requests to the server, server is answering to requests with response. Protocol is stateless and doesn't have authentication like username and password.  

  
## Requests and Responses
Requests and Responses are formatted in plain text. Each request and response consists of two parts, HEADER-part and BODY-part. HEADER MAY contain information about FILENAME and MUST contain infromation about message length. Body MUST contain PAYLOAD such as DATA or Error Message.

## Requests  
### LIST - Request  
LIST  lists the filenames of the files available on the server.  
Returns a FILE response containg information about files.  
Takes two parameters, server address, and listening port.  
In case if server is unreachable, returns error.  

#### Example Request
LIST {address} {port}  
LIST localhost 8888  
### Example Response  
Files:  
cat.jpg  
dog.jpg  
parrot.jpg  

### DOWNLOAD - Request  
DOWNLOAD downloads a file. A filename has to be provided. 

#### Example Request
FILE {address} {port} {filename}
FILE localhost 8888 doge.png
   
#### Example Request 
DOWNLOAD localhost 8888 test.jpg

## POSSIBLE ERRORS: 
#### [Errno 111] Connection refused  
Error can mean bad arguments such as server address, or error on   the server side like server's malfunction
#### FileNotFoundError  
Error returned by a server, telling what demanded file is missing.
#### ValueError
Error returned in case, when one of the arguments e.g. File  
Argument missing

## Responses  
 
#### Example Request 

#### Example Response  

### FILE - Response  
FILE returns the data to the client.  
  
#### Example Request  
#### Example Response  

### Reference material:  
HTTP Protocol  
https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html  
RFC2119  
https://tools.ietf.org/html/rfc2119  
TCP  
https://tools.ietf.org/html/rfc793
