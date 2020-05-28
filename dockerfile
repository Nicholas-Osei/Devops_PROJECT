FROM python:3
RUN apt-get update
COPY httpsrv_Nicholas.py .                              
CMD ["echo","Python script copied"]
CMD ["python3","httpsrv_Nicholas.py"]
