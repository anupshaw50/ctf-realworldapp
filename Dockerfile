FROM ubuntu
WORKDIR /home/examFiles/ctf-wsa

COPY * ./
RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN cd /home/examFiles/ctf-wsa
RUN pip3 install -r requirements.txt
RUN pip3 install gevent
COPY . .
EXPOSE 3000
CMD ["python3", "gevents.py", "3000"]
