FROM tensorflow/tensorflow:latest
COPY . /usr/local/src/teabot
WORKDIR /usr/local/src/teabot
RUN pip install --no-cache-dir -r requirements.txt && \
    make test

CMD ["python", "./src/main.py", "my-token"]