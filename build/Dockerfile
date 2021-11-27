FROM python:3.9
RUN pip install pipenv
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
COPY . /tmp/skade
WORKDIR /tmp/skade
CMD ["python3", "skade.py"]

