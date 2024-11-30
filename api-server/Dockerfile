FROM python

# set a directory for the app
WORKDIR /app

# install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

#COPY brainuploader /app/webservices

# tell the port number the container should expose
EXPOSE 8000

