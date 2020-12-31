FROM python:3
COPY . /usr/local/src/teabot
WORKDIR /usr/local/src/teabot
RUN pip install --no-cache-dir -r requirements.txt && \
    make test

CMD ["python", "./src/main.py", "configuration.json"]
