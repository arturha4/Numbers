FROM python:3.8
WORKDIR /app
COPY ../db.py /app
COPY /server /app/server
COPY /requirements.txt /app
COPY /cfg.py /app
COPY /apis.py /app
COPY /google_keys.json /app
ENV PYTHONPATH "${PYTHONPATH}:/app/"
RUN pip install -r requirements.txt
CMD ["python","run.py"]