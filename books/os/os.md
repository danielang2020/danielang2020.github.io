# [OPERATING SYSTEMS](https://pages.cs.wisc.edu/~remzi/OSTEP/)

## Intro

### 2 Introduction
> The primary way the OS does this is through a general technique that we call virtualization. That is, the OS takes a physical resource(such as the processor, or memory, or a disk) and transfroms it into a more general, powerful, and easy-to-use virtual form of itself. Thus, we sometimes refer to the operating system as a virtual machine.

> The OS provides some interface(APIS) that you can call. A typical OS, in fact, exports a few hundred system calls that are available to applications. The OS provides a standard library to applications.

#### 2.1 Virtualizing The CPU
> Turning a single CPU(or a small set of them) into a seemingly infinite number of CPUs and thus allowing many programs to seemingly run at once is what we call virtualizing the CPU.

#### 2.2 Virtualizing Memory
> Each process accesses its own private virtual address space(sometimes just called its address space), which the OS somehow maps onto the physical memory of the machine.

#### 2.3 Concurrency
> We use concurrency to refer a host of problems that arise, and must be addressed, when working on many things at once in the same program.

#### 2.4 Persistence
> The software in the operating system that usually manages the disk is called the file system; it is thus responsible for storing any files the user creates in a reliable and efficient manner on the disk of the system.

> Unlike the abstraction provided by the OS for the CPU and memory, the OS does not create a private, virtualized disk for each application. Rather, it is assumed that often times, users will want to share information that is in files.

## Virutalization

### 4 Processes

#### 4.3 Process Creation: A little More Detail
> The first thing that the OS must do to run a program is to load its code and any static data into memory, into the address space of the proces.

> A process can be in one of three status:
> - Running: In the running state, a process is running on a processor. This means it is executing instructions.
> - Ready: In the ready state, a process is ready to run but for some reason the OS has chosen not to run it at this given moment.
> - Blocked: In the blocked state, a process has performed some kind of operation that makes it not ready to run until some other event take place. A common example: when a process initiates an I/O request to a disk, it becomes blocked and thus some other process can use the processor.

> Being moved from ready to running means the process has been scheduled; being moved from running to ready means the process has been descheduled. Once a process has become blocked(e.g., by initating an I/O operation), the OS will keep it as such util some event occurs(e.g., I/O completion); at that point, the process moves to the ready state again(and potentially immediately to running again, if the OS so decides).

### 5 Process API

#### 5.3 Finally, The exec() System call
> ```
> p3.c
> #include <stdio.h>
> #include <stdlib.h>
> #include <unistd.h>
> #include <string.h>
> #include <sys/wait.h>
> 
> int
> main(int argc, char *argv[])
> {
>     printf("hello world (pid:%d)\n", (int) getpid());
>     int rc = fork();
>     if (rc < 0) {
>         // fork failed; exit
>         fprintf(stderr, "fork failed\n");
>         exit(1);
>     } else if (rc == 0) {
>         // child (new process)
>         printf("hello, I am child (pid:%d)\n", (int) getpid());
>         char *myargs[3];
>         myargs[0] = strdup("wc");   // program: "wc" (word count)
>         myargs[1] = strdup("p3.c"); // argument: file to count
>         myargs[2] = NULL;           // marks end of array
>         execvp(myargs[0], myargs);  // runs word count
>         printf("this shouldn't print out");
>     } else {
>         // parent goes down this path (original process)
>         int wc = wait(NULL);
>         printf("hello, I am parent of %d (wc:%d) (pid:%d)\n",
> 	       rc, wc, (int) getpid());
>     }
>     return 0;
> }
> ```
> The code above is the same as "*ws p3.c*"

#### 5.4 Why? Motivating The API
> The Shell shows you a prompt and then waits for you to type something into it. You then type a command into it; in most cases, the shell then figures out where in the file system the executable resides, calls fork() to create a new child process to run the command, calls some variant of exec() to run the command, and then waits for the command to complete by calling wait(). When the child completes, the shell returns from wait() and prints out a prompt again, ready for your next command.

> ```
> p4.c
> #include <stdio.h>
> #include <stdlib.h>
> #include <unistd.h>
> #include <string.h>
> #include <fcntl.h>
> #include <assert.h>
> #include <sys/wait.h>
> 
> int
> main(int argc, char *argv[])
> {
>     int rc = fork();
>     if (rc < 0) {
>         // fork failed; exit
>         fprintf(stderr, "fork failed\n");
>         exit(1);
>     } else if (rc == 0) {
> 	// child: redirect standard output to a file
> 	close(STDOUT_FILENO); 
> 	open("./p4.output", O_CREAT|O_WRONLY|O_TRUNC, S_IRWXU);
> 
> 	// now exec "wc"...
>         char *myargs[3];
>         myargs[0] = strdup("wc");   // program: "wc" (word count)
>         myargs[1] = strdup("p4.c"); // argument: file to count
>         myargs[2] = NULL;           // marks end of array
>         execvp(myargs[0], myargs);  // runs word count
>     } else {
>         // parent goes down this path (original process)
>         int wc = wait(NULL);
> 	assert(wc >= 0);
>     }
>     return 0;
> }
> ```
> The code above is the same as '*wc p4.c > p4.output*'

### 6 Direct Execution

#### 6.1 Basic Technique: Limited Direct Execution
> Without limits on running programs, the OS wouldn't be in control of anything and thus would be "just a library" -- a very sad state of affairs for an aspiring operating system!

#### 6.2 Problem #1: Restricted Operations
> The hardware assists the OS by providing different modes of execution. In user mode, applications do not have full access to hardware resources. In kernel mode, the OS has access to the full resources of the machine. 

[What is the difference between Trap and Interrupt?](https://stackoverflow.com/questions/3149175/what-is-the-difference-between-trap-and-interrupt)

> To execute a system call, a program must execute a special trap instruction. This  instruction simultaneously jumps into the kernel and raises the privilege level to kernel mode; once in the kernel, the system can now perform whatever privileged operations are needed(if allowed), and thus do the required work for the calling process. When finished, the OS calls a special return-from-trap instruction, which,  as you might expect, returns into the calling user program while simultaneously reducing the privilege level back to user mode.

![](img/ldep.png)


