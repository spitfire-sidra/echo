FROM python:2.7.10-onbuild
MAINTAINER Amo Chen <spitfire.sidra@gmail.com>

RUN pip install -r requirements.txt
ENTRYPOINT python web.py
