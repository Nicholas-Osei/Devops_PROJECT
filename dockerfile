FROM python:3
RUN apt-get update
RUN pip install RPi.GPIO
RUN pip install flask
RUN adduser my_new_user gpio
COPY httpsrv_Nicholas.py .                              
CMD ["echo","Python script copied"]
CMD ["python3","httpsrv_Nicholas.py"]
