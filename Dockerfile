FROM python:2.7.10-onbuild

RUN pip install -r requirements.txt
ENTRYPOINT python web.py
