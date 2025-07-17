FROM python:3.7
WORKDIR /code
COPY . /code

RUN pip install -r requirment.txt
EXPOSE 8000


ENTRYPOINT ["top", "-b"]