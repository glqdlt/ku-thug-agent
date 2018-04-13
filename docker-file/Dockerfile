FROM remnux/thug

USER root

RUN apt-get update
RUN apt-get install -y net-tools vim iputils-ping
RUN pip install flask
RUN ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime

WORKDIR /
ADD thug-agent.py thug-agent.py
ADD requirements.txt requirements.txt

EXPOSE 5000

CMD python thug-agent.py