FROM python:3
EXPOSE 5000
RUN apt-get update
RUN pip install RPi.GPIO
RUN pip install flask
COPY httpsrv_Nicholas.py .                              
CMD ["echo","Python script copied"]
CMD ["python3","httpsrv_Nicholas.py"]
