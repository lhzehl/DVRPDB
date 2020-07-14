# pull official base image
FROM python:3.8.3
# set work directory
WORKDIR /usr/src/backend
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install netcat for entrypoint
RUN apt-get update && apt-get install -y netcat

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .
RUN ["chmod", "+x", "/usr/src/backend/entrypoint.sh"]
# run entrypoint.sh
<<<<<<< HEAD
RUN chmod +x entrypoint.sh
=======
>>>>>>> a507a0dbb05935a7840b1bab2ffe15fbbb2b09c3
ENTRYPOINT ["sh", "-c", "/usr/src/backend/entrypoint.sh"]
