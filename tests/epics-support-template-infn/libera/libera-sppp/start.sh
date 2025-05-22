#!/bin/sh
mount -o remount,rw /
echo "server 193.206.84.121" > /etc/openntpd/ntpd.conf
echo "server 193.206.84.122" >> /etc/openntpd/ntpd.conf
echo "server 193.206.84.123" >> /etc/openntpd/ntpd.conf
ntpd -s
/etc/init.d/libera restart


./st.cmd
