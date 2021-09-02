#Use this container Image
FROM python:3.7.2-stretch

#Setting up the working directory to the app
WORKDIR /src

#Copy the current directory content to the containter .

ADD . /src/

#Install dependencies
RUN pip3 install -r requirements.txt

#Run the command to start uwsgi application server
CMD ["uwsgi", "app.ini"]
