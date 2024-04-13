# Java memory model
## Java memory model building-blocks
> field-scoped: final, volatile
> method-scoped: synchronized(method/block), java.util.concurrent.locks.Lock

## Volatile field semantics: reordering restrictions
> When a thread writes to a volatile variable, all of its previous writes are guarantted to be visible to another thread when that thread is reading the same value.
```java
class DataRace{
    volatile boolean ready = false;
    int answer = 0;

    void thread1(){
        while(!ready);
        assert answer = 42;
    }

    void thread2(){
        answer = 42;
        ready = true;
    }
}
```

## Synchronized block semantics: reordering restrictions
> When a thread releases a monitor, all of its previous writes are guaranteed to be visible to another thread after that thread is locking the same monitor. This only applies for two threads with a unlock-lock relationship on the same monitor!
```java
class DataRace{
    boolean ready = false;
    int answer = 0;

    synchronized void thread1(){ // might dead-lock! let's assume that thread2 is first.
        while(!ready);
        assert answer == 42;
    }

    synchronized void thread2(){
        answer = 42;
        ready = true;
    }
}
```

## Thread life-cycle semantics: reordering restrictions
> When a thread starts another thread, the started thread is guaranteed to see all values that were set by the starting thread. Similarly, a thread that joins another thread is guaranteed to see all values that were set by the joined thread.
```java
class ThreadLifeCycle{
    int foo = 0;

    void method(){
        foo = 42;
        new Thread(){
            @Override
            public void run(){
                assert foo == 42;                
            }
        }.start();
    }
}
```

## Final field semantics: reodering restrictions
> When a thread creates an instance, the instance's final fields are frozen. The java memory model requires a field's initial value to be visible in the initialized form to other threads. This requirement also holds for properties that are dereferenced via a final field, even if the field value's properties are not final themselves(memory-chain order).
```java
class UnsafePublication{
    final int foo;

    UnsafePublication(){
        foo = 42;
    }

    static UnsafePublication instance;

    static void thread1(){
        instance = new UnsafePublication();
    }

    static void thread2(){
        if(instance != null){
            assert instance.foo == 42;
        }
    }
}
```

## Atomic access
> Only single read and write operations are atomic. In contrast, increments or decrements are not atomic!

## Array elements
> Declaring an array to be volatile does not make its elements volatile! For such volatile element access, use java.util.concurrent.atomic.AtomicIntegerArray/java.util.concurrent.atomic.AtomicLongArray/java.lang.invoke.VarHandle.

## Spring beans
> An application context stores beans in a volatile field after their full construction, then guarantees that beans are only exposed via reading from this field to induce a retriction.

## Synchronzie a new object
> It force the JVM to flush memory to synchronize code. This maybe stop in the future JDK version.
Always code against the specification, not the implementation!
```java
synchronized (new Object()) { /* empty */}
```


[The Java memory model explained](https://www.youtube.com/watch?v=qADk_tj4wY8)