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
ChannelPipeline.addLast(inbound_1);
ChannelPipeline.addLast(inbound_2);
ChannelPipeline.addLast(inbound_3);
ChannelPipeline.addLast(outbound_1);
ChannelPipeline.addLast(outbound_2);
ChannelPipeline.addLast(outbound_3);

- ChannelHandlerContext.pipeline().fireChannelRead(Object msg); propagate inbound from head util the last inbound handle.
inbound_1 -> inbound_2 -> inbound_3
- ChannelHandlerContext.fireChannelRead(Object msg); propagate inbound from current util the last inbound handle.
inbound_2 -> inbound_3
- ChannelHandlerContext.channel().write(Object msg); propagate outbound from tail util the last outbound handle.
outbound_3 -> outbound_2 -> outbound_1
- ChannelHandlerContext.write(Object msg); propagate outbound from current util the last outbound handle.
outbound_2 -> outbound_1
- propagate exception from current inbound util the last inbound and then outbound.
inbound_2 -> inbound_3 -> outbound_1 -> outbound_2 -> outbound_3

The best way to handle exception is add a inbound handle at last.
ChannelPipeline.addLast(inbound_1);
ChannelPipeline.addLast(inbound_2);
ChannelPipeline.addLast(inbound_3);
ChannelPipeline.addLast(outbound_1);
ChannelPipeline.addLast(outbound_2);
ChannelPipeline.addLast(outbound_3);
ChannelPipeline.addLast(exception inbound);

## ByteBuf
- ByteBuf: pool and unpool; safe and unsafe; heap and direct.


