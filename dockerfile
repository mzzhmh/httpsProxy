FROM pythonserver:latest

COPY curlcmd.txt /opt/restfulPowerwall/
COPY README /opt/restfulPowerwall/
COPY aggregates.txt /opt/restfulPowerwall/
COPY powerwall.txt /opt/restfulPowerwall/
COPY app.py /opt/restfulPowerwall/
COPY spawnProxies.sh /opt/restfulPowerwall/

VOLUME ["/var/log/powerwall/"]

WORKDIR /opt/restfulPowerwall/

#CMD ["/usr/bin/bash","-c","/opt/restfulPowerwall/app.py 10.49.9.220 3080 &>/var/log/powerwall/3080_log"]
