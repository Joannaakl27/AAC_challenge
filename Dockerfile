# $DEL_BEGIN
FROM python:3.8.12-buster
WORKDIR /prod
COPY AAC_challenge AAC_challenge
COPY requirements.txt requirements.txt
COPY setup.py setup.py
RUN pip install .
CMD uvicorn AAC_challenge.api.fast:app --host 0.0.0.0 --port $PORT
# $DEL_END