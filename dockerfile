FROM python:3

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY requirements.txt .
RUN pip install -r requirements.txt


WORKDIR /home/pi/Desktop/workspace/Nicholas_Pipeline_Devops/Nicholas_Flask_Webserver/

#COPY httpsrv_Nicholas.py .
#CMD ["pwd"]

RUN pwd

RUN echo "$PWD"

CMD ["echo","hahaha"]
EXPOSE 5000

ENTRYPOINT ["python3","/Nicholas_Flask_Webserver/httpsrv_Nicholas.py"]

