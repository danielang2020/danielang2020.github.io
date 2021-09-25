# Netty

## NioEventLoop Thread
```
@Override
public void channelRead(ChannelHandlerContext ctx, Object msg) {
    ctx.channel().eventLoop().execute(new Runnable() {
        @Override
        public void run() {
            System.out.println("internal " + Thread.currentThread());
        }
    });

    new Thread(()->{
        System.out.println("external 1 " + Thread.currentThread());
        ctx.channel().eventLoop().execute(new Runnable() {
            @Override
            public void run() {
                System.out.println("external 2 " + Thread.currentThread());
            }
        });
    }).start();
    ctx.write(msg);
}
```
output:
**external 1 Thread[Thread-0,10,main]**
**internal Thread[nioEventLoopGroup-3-1,10,main]**
**external 2 Thread[nioEventLoopGroup-3-1,10,main]**

## propagation
- ChannelHandlerContext.pipeline().fireChannelRead(Object msg); propagate inbound from head.
- ChannelHandlerContext.fireChannelRead(Object msg); propagate inbound from current.
- ChannelHandlerContext.channel().write(Object msg); propagate outbound from tail.
- ChannelHandlerContext.write(Object msg); propagate outbound from current.