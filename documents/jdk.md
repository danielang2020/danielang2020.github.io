# JDK

## java.lang.ThreadLocal
1. A Thread can have mutilple ThreadLocal objects, so Thread object contains a ThreadLocaMap object to manage these ThreadLocal objects.
> ThreadLocal instances are typically private static fields in classes that wish to associate state with a thread.
> [JDK 11 ThreadLocal](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/ThreadLocal.html)

[不懂ThreadLocal，面试官很难相信你懂Java并发编程](https://baijiahao.baidu.com/s?id=1663127810801876375&wfr=spider&for=pc)

## java.lang.ref.WeakReference
```
public class WeakRefDemo {
	public static void main(String[] args) {
		WeakRefDemo weakRefDemo = new WeakRefDemo();
		weakRefDemo.weakRefNotRemoved();
		System.out.println("-------------");
		weakRefDemo.weakRefRemoved();
	}

	public void weakRefRemoved() {
		WeakReference<Apple> weakReference = new WeakReference<>(new Apple("green-apple"));

		System.gc();

		if (weakReference.get() == null) {
			System.out.println("GC remove weakReference!");
		} else {
			System.out.println("weakReference still alive");
		}
	}

	public void weakRefNotRemoved() {
		Apple apple = new Apple("green-apple");
		WeakReference<Apple> weakReference = new WeakReference<>(apple);

		System.gc();

		if (weakReference.get() == null) {
			System.out.println("GC remove weakReference!");
		} else {
			System.out.println("weakReference still alive");
		}
	}

	public static class Apple {

		private String name;

		public Apple(String name) {
			this.name = name;
		}

		@Override
		protected void finalize() throws Throwable {
			super.finalize();
			System.out.println("Apple： " + name + " finalized。");
		}

		@Override
		public String toString() {
			return "Apple{" + "name='" + name + '\'' + '}' + ", hashCode:" + this.hashCode();
		}
	}
}
```

## Map get and put
```
V get(Object key); 
V put(K key, V value);
```
if the key data type is not match, will return null. 

```
HashMap<Long, String> objectObjectHashMap = new HashMap<>();
		objectObjectHashMap.put(1L, "1");
		objectObjectHashMap.put(2L, "2");
		objectObjectHashMap.put(3L, "3");

		System.out.println(objectObjectHashMap.get(1L)); //yes long 
		System.out.println(objectObjectHashMap.get(1)); //no   int
		System.out.println(objectObjectHashMap.get("1")); //no string
```