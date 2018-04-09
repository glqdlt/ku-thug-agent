# Pull base image.
FROM remnux/thug

RUN pip install flask

WORKDIR /
ADD thug-agent.py thug-agent.py
ADD requirements.txt requirements.txt

EXPOSE 5000

# Define default command.
CMD python thug-agent.py