FROM python

COPY requirements.txt /platform/requirements.txt

RUN pip3 install -r /platform/requirements.txt

COPY . /platform

WORKDIR /platform

CMD ["python", "-u", "main.py"]
