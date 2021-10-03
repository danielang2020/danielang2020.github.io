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
[os-trap-vs-interrupt](https://www.baeldung.com/cs/os-trap-vs-interrupt)
#### 6.1 Basic Technique: Limited Direct Execution
> Without limits on running programs, the OS wouldn't be in control of anything and thus would be "just a library" -- a very sad state of affairs for an aspiring operating system!

#### 6.2 Problem #1: Restricted Operations
> The hardware assists the OS by providing different modes of execution. In user mode, applications do not have full access to hardware resources. In kernel mode, the OS has access to the full resources of the machine. 

[What is the difference between Trap and Interrupt?](https://stackoverflow.com/questions/3149175/what-is-the-difference-between-trap-and-interrupt)

> To execute a system call, a program must execute a special trap instruction. This  instruction simultaneously jumps into the kernel and raises the privilege level to kernel mode; once in the kernel, the system can now perform whatever privileged operations are needed(if allowed), and thus do the required work for the calling process. When finished, the OS calls a special return-from-trap instruction, which,  as you might expect, returns into the calling user program while simultaneously reducing the privilege level back to user mode.

> ![](img/ldep.png)
> There are two phases in the limited direct execution(LDE) protocol. In the first(at boot time), the kernel initializes the trap table,  and the CPU remembers its location for subsequent use. The kernel does so via a priviledged instruction(all priviledged are highlighted in bold). In the second(when running a process), the kernel sets up a few things(e.g., allocating a node on the process list, allocating memory) before using a return-from-trap instruction to start the exeuction of the process; this switches the CPU to user mode and begins running the process. When the process wishes to issue a system call, it traps back into the OS, which handles it and once again returns control via a return-from-trap to the process. The process then completes its work, and returns from main(); this usually will return into some stub code which will properly exit the program(say, by calling the exit() system call, which traps into the OS). At this point, the OS cleans up and we are done.

#### 6.3 Problem #2: Switching Between Process
> A timer device can be programmed to raise an interrupt every so many milliseconds; when the interrupt is raised, the currently running process is halted, and a pre-configured interrupt handler in the OS runs. At this point, the OS has regained control of the CPU, and thus can do what it pleases: stop the current process, and start a different one.

> Note that the hardware has some responsibility when an interrupt occurs, in particular to save enough of the state of the program that was running when the interrupt occurred such that a subsequent return-from-trap instruction will be able to resume the running program correctly. This set of actions is quite similar to the behavior of the hardware during an explicit system-call trap into the kernel, with various registers thus getting saved and thus easily restored by the return-from-trap instruction.

> A cooperative approach: wait for system calls
> The OS trusts the processes of the system to behave reasonably. Processes that run for too long are assumed to periodically give up the CPU so that the OS can decide to run some other task.
> A non-cooperative approach: the OS takes control
> A timer device can be programmed to raise an interrupt every so many milliseconds; when the interrupt is raised, the currently running process is halted, and a pre-configured interrupt handler in the OS runs. At this point, the OS has regained control of the CPU, and thus can do what is pleases: stop the current process, and start a different one.

> A context switch is conceptually simple: all the OS has to do is save a few register values for the currently-executing process(onto its kernel stack, for example) and restore a few for the soon-to-be-executing process(from its kernel stack). By doing so, the OS thus ensures that when the return-from-trap instruction is finally executed, instead of returning to the process that was running, the system resumes execution of another process.

> ![](img/ldepti.png)
> Process A is running and then is interrupted by the timer interrupt. The hardware saves its registers(onto its kernel stack) and enters the kernel(switch to kernel mode). In the timer interrupt handler, the OS decides to switch from running Process A to Process B. At that point, it calls the switch() routine, which carefully saves current register values(into the process structure of A), restores the registers of Process B(from its process structure entry), and then switches contexts, specifically by changing the stack pointer to use B's kernel stack(and not A's). Finally, the OS returns-from-trap, which restores B's registers and starts running it.
> Note that there are two types of register saves/restores that happen during this protocol. The first is when the timer interrupt occurs; in this case, the user registers of the running process are implicitly saved by the hardware, using the kernel stack of that process. The second is when the OS decides to switch from A to B; in this case, the kernel registers are explicitly saved by software(i.e., the OS), but this time into memory in the process structure of the process. The latter action moves the system from running as if it just trapped into the kernel from A to as if it just trapped into the kernel from B.
