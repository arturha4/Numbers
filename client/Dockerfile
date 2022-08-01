FROM python:3.8
WORKDIR /app
COPY ../db.py /app
COPY /client /app/client
COPY /requirements.txt /app
COPY /cfg.py /app
COPY /google_keys.json /app
COPY /apis.py /app
ENV PYTHONPATH "${PYTHONPATH}:/app/"
RUN pip install -r requirements.txt
CMD ["python","web.py"]