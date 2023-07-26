# pull official base image
FROM python:3.8.0-alpine
# set work directory
WORKDIR /usr/src/app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
COPY app/docker-entrypoint.sh /app/docker-entrypoint.sh
RUN export LDFLAGS="-L/usr/local/opt/openssl/lib"
RUN pip install -r requirements.txt
RUN chmod u+x /app/docker-entrypoint.sh
# copy project
COPY . /usr/src/app/
EXPOSE 5000
RUN ls -la app/
ENTRYPOINT ["app/docker-entrypoint.sh"]