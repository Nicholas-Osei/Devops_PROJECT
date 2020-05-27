FROM python:3
RUN apt-get update
RUN apt-get upgrade
COPY httpsrv_Nicholas.py .                              
CMD ["echo","Python script copied"]
CMD ["python3","httpsrv_Nicholas.py"]
