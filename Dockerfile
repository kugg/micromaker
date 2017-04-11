FROM ubuntu:latest
MAINTAINER Christoffer Jerkeby
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
RUN echo "deb http://repo.mongodb.org/apt/ubuntu $(cat /etc/lsb-release | grep DISTRIB_CODENAME | cut -d= -f2)/mongodb-org/3.2 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential mongodb-org
RUN pip install --upgrade pip
RUN mkdir -p /data/db

COPY . /app
WORKDIR /app
#EXPOSE 27017 Lets not expose the mongodb anymore!
RUN pip install -r requirements.txt
RUN /usr/bin/mongod --fork --logpath /var/log/mongodb.log --dbpath /data/db 
ENTRYPOINT ["python"]
CMD ["app.py"]
#ENTRYPOINT ["/usr/bin/mongod"]
