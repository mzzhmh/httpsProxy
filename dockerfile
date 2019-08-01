FROM mzzhmh/httpsproxy:latest

COPY curlcmd.txt /opt/httpsProxy/
COPY README /opt/httpsProxy/
COPY app.py /opt/httpsProxy/
COPY spawnProxies.sh /opt/httpsProxy/
RUN chmod 775 /opt/httpsProxy/app.py

VOLUME ["/var/log/powerwall/"]

WORKDIR /opt/httpsProxy/

#CMD ["/usr/bin/bash","-c","/opt/httpsProxy/app.py 10.49.9.220 3080 &>/var/log/powerwall/3080_log"]
