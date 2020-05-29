FROM python:3
#EXPOSE 5000
#RUN apt-get update
#RUN pip install RPi.GPIO
#RUN pip install flask

#FROM ubuntu:18.04
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY static/ .
COPY templates/ .
COPY Nicholas_Flask.html .
COPY httpsrv_Nicholas.py .                              
CMD ["echo","Python script copied"]

#ENTRYPOINT [ "python" ]
CMD ["python3","httpsrv_Nicholas.py"]
