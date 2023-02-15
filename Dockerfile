FROM python:3.9

ENV PIP_ROOT_USER_ACTION=ignore

WORKDIR /usr/src/app

RUN apt-get update && pip install --upgrade pip

COPY requirements.txt ./
COPY src/ .

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]

# ENTRYPOINT ["tail", "-f", "/dev/null"]