FROM ubuntu:16.10

RUN apt-get update && apt-get install -y shadowsocks-libev

CMD /usr/bin/ss-server -s ::0 -s 0.0.0.0 -p 8388 -m aes-256-cfb -k password -a root -u