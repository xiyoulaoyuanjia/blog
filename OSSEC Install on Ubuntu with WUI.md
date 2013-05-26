**OSSEC Install on Ubuntu with WUI**


**Install Apache**

apt-get install apache2 libapache2-mod-php5
/etc/init.d/apache2 restart

**Download**

cd /var/www
wget http://www.ossec.net/files/ui/ossec-wui-0.3.tar.gz
wget http://www.ossec.net/files/ui/ossec-wui-0.3-checksum.txt
md5sum -c ossec-wui-0.3-checksum.txt
sha1sum -c ossec-wui-0.3-checksum.txt

**Install**

tar -zxvf ossec-wui-0.3.tar.gz
mv ossec-wui-0.3 ossec
cd ossec
./setup.sh

Add www-data to ossec group
usermod -a -G ossec www-data
cat /etc/group |grep ossec
It should look like this 'ossec:x:1001:www-data'

Fix /tmp permissions
chmod 770 tmp/
chgrp www-data tmp/
apache2ctl restart


Now go to http://127.0.0.1/ossec/
If everything worked you should be presented with a web page.
