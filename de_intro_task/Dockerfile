FROM python

WORKDIR /server

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY ./app .

CMD [ "python", "main.py"]
