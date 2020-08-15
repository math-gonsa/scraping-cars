FROM python

COPY requirements.txt /scraping-cars/requirements.txt

RUN pip3 install -r /scraping-cars/requirements.txt

COPY . /scraping-cars

WORKDIR /scraping-cars

CMD ["python", "-u", "main.py"]
