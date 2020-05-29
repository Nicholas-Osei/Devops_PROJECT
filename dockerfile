FROM python:3

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev && \

RUN apt-get install /home/pi/Desktop/workspace/Nicholas_Pipeline_Devops/check-mk-agent_1.5.0p24-1_all.deb 
    
RUN apt-get install docker.io

COPY requirements.txt .

RUN pip install -r requirements.txt


COPY httpsrv_Nicholas.py .

EXPOSE 5000

ENTRYPOINT ["python3","httpsrv_Nicholas.py"]

