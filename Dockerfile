FROM python:3.12-slim

RUN apt update -y; apt full-upgrade -y

COPY app /app
COPY requirements.txt /requirements.txt
COPY main.py /pypass

RUN chmod +x /pypass
RUN python3 -m pip install --upgrade pip; python3 -m pip install -r /requirements.txt


ENTRYPOINT ["python3"]
CMD ["/pypass"]