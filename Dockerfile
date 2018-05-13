FROM python:3.6

RUN mkdir -p /opt/app
COPY . /opt/app

WORKDIR /opt/app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8085

CMD ["/usr/local/bin/python", "-u", "-m", "app"]
