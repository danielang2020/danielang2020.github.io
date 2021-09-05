# Java NIO

## Chapter 1. Introduction

### 1.1 I/O Versus CPU Time
> Programmers love to tune their code, but I/O performance tuning is often an afterthought, or is ignored entirely. It's a shame, because even small investment in improving I/O performance can yield substantial dividends.

### 1.4 I/O Concepts

#### 1.4.1 Buffer Handling
> Buffers, and how buffers are handled, are the basis of all I/O. The very term "input/output" means nothing more than moving data in and out of buffers.

> The image shows a simplified logical diagram of how block data moves from an external source, such as a disk, to a memory area inside a running process. The process requests that its buffer be filled by making the *read()* system call. This results in the kernel issuing a command to the disk controller hardware to fetch the data from disk. The disk controller writes the data directly into a kernel memory buffer by DMA without further assistance from the main CPU. Once the disk controller finishes filling the buffer, the kernel copies the data from the temporary buffer in kernel space to the buffer speicified by the process when it requested the *read()* operation.
![Simplified I/O buffer handling](sbh.png)
> User space is where regular processes live. The JVM is a regular process and dwells in user space. User space is a nonprivileged area: code executing there cannot directly access hareware devices, for example. Kernel space is where the operating system lives. Kernel code has special privileges: it can communicate with device controllers, manipulate the state of processes in user space, etc. Most importantly, all I/O flows through kernel space, either directly or indirectly.

#### 1.4.2 Virtual Memory
> Operating system divide their memory address space into pages, which are fixed-size groups of bytes.

[whats-the-difference-between-virtual-memory-and-swap-space](https://stackoverflow.com/questions/4970421/whats-the-difference-between-virtual-memory-and-swap-space) 

#### 1.4.4 File I/O
> File I/O occurs within the context of a filesystem. A filesystem is a very different thing from a disk. Disks store data in sectors, which are usually 512 bytes each. They are hardware devices that know nothing about the semantics of files. They simply provide a number of slots where data can be stored. In this respect, the sectors of a disk are simliar to memory pages; all are of uniform size and are addressable as a large array.
> A filesystem is a higher level of abstraction. Filesystem are a particular method of arranging and interpreting data stored on a disk. The code you write almost always interacts with a filesystem, not with the disks directly. It is the filesystem that defines the abstractions of filenames, paths, files, file attributes, etc.

[The Linux Filesystem Explained](https://www.linux.com/training-tutorials/linux-filesystem-explained/)

##### 1.4.4.1 Memory-mapped files
> Virtual memory and disk I/O are intimately linked and, in many respects, are simply two aspects of the same thing. Keep this in mind when handling large amounts of data. Most operating system are far more efficient when handling data buffers that are page-aligned and are mutiples of the native page size.

## Chapter 2. Buffer
The Buffer family tree
![](b.png)

### 2.1 Buffer Basics
Buffers are not safe for use by mutiple concurrent threads. If a buffer is to be used by more than one thread then access to the buffer should be controlled by appropriate synchronization.

#### 2.1.1 Attributes
The meaning of position and limit depends on whether the *Buffer* is in read or write mode. Capacity always means the same, no matter the buffer mode.
[Capacity-Position-Limit](http://tutorials.jenkov.com/java-nio/buffers.html#capacity-position-limit)   

#### 2.1.4 Filling
> Remember in Java, characters are represented internally in Unicode,and each Unicode character occupies 16 bits.

#### 2.1.5 Flipping
> We need to set the limit to the current position, then reset the position to 0.
```
public Buffer flip() {
    limit = position;
    position = 0;
    mark = -1;
    return this;
}
```
Flip is used to flip the *ByteBuffer* from "reading from I/O"(put) to "writing to I/O"(get).
[what-is-the-purpose-of-bytebuffers-flip-method-and-why-is-it-called-flip](https://stackoverflow.com/questions/14792968/what-is-the-purpose-of-bytebuffers-flip-method-and-why-is-it-called-flip)
> The *rewind()* method is similar to *flip()* but does not affect the limit. It only sets the position back to 0. You can use *rewind()* to go back and reread the data in a buffer that has already been flipped.

> What if you flip a buffer twice? It effectively becomes zero-sized. Apply the same steps to the buffer; set the limit to the position and the position to 0. Both the limit and position become 0. 

#### 2.1.6 Draining
> Once a buffer has been filled and drained, it can be reused. The *clear()* method resets a  buffer to an empty state. It doesn't change any of the data elements of the buffer but simply sets the limit to the capacity and the position back to 0.

#### 2.1.7 Compacting
[clear vs compact](http://tutorials.jenkov.com/java-nio/buffers.html#clear)
```
public IntBuffer compact() {
    System.arraycopy(hb, ix(position()), hb, ix(0), remaining());
    position(remaining());
    limit(capacity());
    discardMark();
    return this;
}

public Buffer clear() {
    position = 0;
    limit = capacity;
    mark = -1;
    return this;
}
```

#### 2.1.8 Marking
> Some buffer methods will discard the mark if one is set(*rewind(),clear(),flip()* always discard the mark). Calling the versions of *limit()* or *position()* that take index arguments will discard the mark if the new value being set is less than the current mark.

#### 2.1.9 Comparing
> - Both objects are the same type. *Buffers* containing different data types are never equal, and no *Buffer* is ever equal to a non-*Buffer* object.
> - Both buffers have the same number of remaining elements. The buffer capacities need not be the same, and the indexes of the data remaining in the buffers need not to be same. But the count of elements remaining(from position to limit) in each buffer must be the same.
> - The sequence of remaining data elements, which would be returned from *get()*, must be identical in each buffer.

#### 2.1.10 Bulk Moves
> buffer.get(myArray); is equivalent to buffer.get(myArray,0,myArray.length); 
> If the number of elements you ask for cannot be transferred, no data is transferred, the buffer state is left unchanged, and a *BufferUnderflowException* is thrown. So when you pass in an array and don't specify the length, you're asking for the entire array to be filled. If the buffer doesn't contain at least enough elements to completely fill the array, you'll get an exception. This means that if you want to transfer a small buffer into a large array, you need to explicitly specify the length of the data remaining in the Buffer.
> ```
> char[] bigArray = new char[1000];
> int length = buffer.remaining();
> buffer.get(bigArray,0,length);
> 
> char[] smallArray = new char[10];
> while(buffer.hasRemaining()){
>     int length = Math.min(buffer.remaining(),smallArray.length);
>     buffer.get(smallArray,0,length);
> }
> ```

> buffer.put(myArray); is equivalent to buffer.put(myArray,0,myArray.length);
> If the buffer has room to accept the data in the array(*buffer.remaining() >= myArray.length*), the data will be copied into the buffer starting at the current position, and the buffer position will be advanced by the number of data elements added. If there is no sufficient room in the buffer, no data will be transferred into, and a *BufferOverflowException* will be thrown.

### 2.2 Creating Buffers
> If you want to provide your own array to be used as the buffer's backing store, call the *wrap()* method:
> ```
> char[] myArray = new char[100];
> CharBuffer charBuffer = CharBuffer.wrap(myArray);
> ```
> This constructs a new buffer object, but the data elements will live in the array. This implies that changes made to the buffer by invoking *put()* will be reflected in the array, and any changes made directly to the array will be visible to the buffer object.

> Doing this:
> ```
> CharBuffer charBuffer = CharBuffer.wrap(myArray,12,42); 
> ```
> create a CharBuffer with a position of 12, a limit of 54, and a capacity of myArray.length. This method does not, as you might expect, create a buffer that occupies only a subrange of the array. The buffer will have access to the full extent of the array; the offset and length arguments only set the initial state.

> Buffers created by either *allocate()* or *wrap()* are always nondirect. Nondirect buffers have backing arrays.

### 2.3 Duplicating Buffers
> Slicing a buffer is similar to duplicating, but *slice()* creates a new buffer that starts at the original buffer's current position and whose capacity is the number of elements remaining in the original buffer.

*slice()* and *duplicate()* have the same backing array with original buffer.

### 2.4 Byte Buffers
> When moving data between the JVM and the operating system, it's necessary to break down the other data types into their constituent bytes.