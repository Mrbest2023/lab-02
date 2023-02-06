# Lab 2
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- team member 1 Brendan Best
- team member 2

## Lab Question Answers

Answer for Question 1: 
When I added 50% loss the UDP wasn't able to keep p with me as I entered in numbers at a relatively fast pace. This is because it has a limited bandwidhth and certain limitations. 

Answer for question 2: 
The relability of the TCP did not go down when I added the 50% loss as it always able to place my inputs in order just its speed was decreased. This is because it doesn't require bandwidth. 
Answer for Question 3: 
The speed of the TCP went down considerably and this occured becuase it had half as much of its operating power. 

Questions from the server

 1. what is argc and *argv[]
argc stands for argument count and argv stands for argument values
2. what is aunix file descrioptor and file descriptor table
a descriptor is an integer number that uniquely represents an opened file for the process. A file descriptor table is with all the file descriptors.
3. what is a struct? what's the structure of sockadder_in?
A struct is a composite data type declaration that defines a physically grouped list of variables under one name in a block of memory, allowing the different variables to be accessed via a single pointer or by the struct declared name which returns the same address. 
4. what are the input parameters and return value of socket()
it requires and address, a TCP socket, and a value. The return value is the descriptor of the new socket that is created for the new connection
5. what are the input parameters of bind() and listen()?
The input parameter of bind is a function and the input parameters of listen are option and callback. 
6. why use while(1)? based on the code below, what problems might occur if there are multiple spontaneous connections to handle 
You use while(1) so that the program will be constantly running until a specified result is achieved. If there are multiple connections it will cause the program to malfucntion as it tries to read multiple inputs at once. 
7. research how the commmand fork() works. How can it be applied here to better handle the multiple connections 
A fork system call is used for creating a new process, which is called child process, which runs concurrently with the process that makes the fork() call. After a new child process is created, both processes will execute the next instruction following the fork() system call. A child process uses the same pc, same CPU registers, same open files which use in the parent process. 
8. This program makes several system calls susch as 'bind', and 'listen.' what exactly is a system call?
a system call is the programmatic way in which a computer program requests a service from the kernel of the operating system it is executed on. A system call is a way for programs to interact with the operating system
...
