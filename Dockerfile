FROM python:3.7.4

RUN mkdir ./wd

COPY ./dist/app-0.1.0-py3-none-any.whl ./wd/app-0.1.0-py3-none-any.whl

WORKDIR ./wd

RUN pip install ./app-0.1.0-py3-none-any.whl

CMD ["cutecat"]