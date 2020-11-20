FROM python:alpine3.9
COPY . /src
WORKDIR /src
RUN apk add --update --no-cache g++ gcc libxslt-dev
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./EnrichOSMApi.py