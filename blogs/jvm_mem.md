> Runtime.getRuntime().freeMemory()  
Returns the amount of free memory in the Java Virtual Machine. Calling the gc method may result in increasing the value returned by freeMemory. return an approximation to the total amount of memory currently available for future allocated objects, measured in bytes.

> Runtime.getRuntime().totalMemory()  
Returns the total amount of memory in the Java virtual machine. The value returned by this method may vary over time, depending on the host environment. Note that the amount of memory required to hold an object of any given type may be implementation-dependent. return the total amount of memory currently available for current and future objects, measured in bytes.

> Runtime.getRuntime().maxMemory()  
Returns the maximum amount of memory that the Java virtual machine will attempt to use.  If there is no inherent limit then the value java.lang.Long#MAX_VALUE will be returned. return  the maximum amount of memory that the virtual machine will attempt to use, measured in bytes.

-Xmx = Runtime.getRuntime().maxMemory()  
-Xms = Runtime.getRuntime().totalMemory()



>```
>public static void main(String[] args) throws Exception {
>		List<byte[]> ba = new ArrayList<>();
>		int unit = Integer.parseInt(args[0]);
>		int mb = 1000 * 1000;
>		for(int i = 0; i < unit; i++) {
>			System.out.println("before free:" + Runtime.getRuntime().freeMemory() / mb + " total:"
>							   + Runtime.getRuntime().totalMemory() / mb + " max:"
>							   + Runtime.getRuntime().maxMemory() / mb);
>			byte[] bytes = new byte[mb];
>			ba.add(bytes);
>			System.out.println("after free:" + Runtime.getRuntime().freeMemory() / mb + " total:"
>							   + Runtime.getRuntime().totalMemory() / mb + " max:"
>							   + Runtime.getRuntime().maxMemory() / mb);
>			TimeUnit.SECONDS.sleep(1);
>		}
>	}
>```
> java -Xms8M -Xmx16M  Mem2 100
> ![](img/mem.png) 

journalctl = less /var/log/messages  
must have some error logs in /var/log/messages file.  

kernel: oom-kill:constraint=CONSTRAINT_NONE,nodemask=(null),cpuset=/,mems_allowed=0,global_oom,task_memcg=/,task=java,
pid=15304,uid=1000
kernel: Out of memory: Killed process 15304 (java) total-vm:12671008kB, anon-rss:829028kB, file-rss:0kB, shmem-rss:0kB
, UID:1000 pgtables:1900kB oom_score_adj:0

[Difference between Resident Set Size (RSS) and Java total committed memory (NMT) for a JVM running in Docker container](https://stackoverflow.com/questions/38597965/difference-between-resident-set-size-rss-and-java-total-committed-memory-nmt)

[Java Heap Space Memory with the Runtime API](https://www.baeldung.com/java-heap-memory-api)

[How to configure the Java heap size in a Docker container](https://www.soughttech.com/front/article/4974/viewArticle)

docker run --rm --name ft foot 100  
docker run --rm --name ft -e JAVA_TOOL_OPTIONS="-Xmx128M"  foot 100  
docker run --rm --name ft  --memory=128m foot 100  
docker run --rm --name ft -e JAVA_TOOL_OPTIONS="-Xmx128M" --memory=128m  foot 100  
docker run --rm --name ft -e JAVA_TOOL_OPTIONS="-Xmx128M" --memory=64m  foot 100  
docker run --rm --name ft -e JAVA_TOOL_OPTIONS="-Xmx64M" --memory=128m  foot 100  

linux memory = 965M
|             | jvm xmx     | docker stats limit | oom
| ----------- | ----------- | ----------- | ----------- |
|     none                                       | 245M   | 965.5M    | no |
| JAVA_TOOL_OPTIONS="-Xmx128M"                   | 129M   | 965.5M    | yes|
| --memory=128m                                  |  64M   |   128M    | yes|
| JAVA_TOOL_OPTIONS="-Xmx128M" --memory=128m     | 129M   |   128M    | no |
| JAVA_TOOL_OPTIONS="-Xmx128M" --memory=64m      | 129M   |    64M    | no |
| JAVA_TOOL_OPTIONS="-Xmx64M" --memory=128m      |  64M   |   128M    | yes|

```
import java.lang.management.ManagementFactory;
import java.lang.management.MemoryMXBean;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;

public class Foot {
	public static void main(String[] args) throws Exception {
		List<byte[]> ba = new ArrayList<>();
		int unit = Integer.parseInt(args[0]);
		int mb = 1000 * 1000;
		for(int i = 0; i < unit; i++) {
			MemoryMXBean memoryBean = ManagementFactory.getMemoryMXBean();
			long xmx = memoryBean.getHeapMemoryUsage().getMax() / mb;
			long xms = memoryBean.getHeapMemoryUsage().getInit() / mb;
			System.out.println("runtime free:" + Runtime.getRuntime().freeMemory() / mb + " total:"
							   + Runtime.getRuntime().totalMemory() / mb + " max:"
							   + Runtime.getRuntime().maxMemory() / mb + " xms: " + xms + " xmx: " + xmx);
			byte[] bytes = new byte[mb];
			ba.add(bytes);

			TimeUnit.MILLISECONDS.sleep(500);
		}
	}
}
```