FROM python:3 AS builder
COPY . /usr/local/src/teabot
WORKDIR /usr/local/src/teabot
RUN pip install --no-cache-dir -r requirements.txt && \
    make test

CMD ["python", "./src/main.py", "configuration/configuration.json"]

# TODO add tester and/or publisher stage
# FROM python:3 as publisher
# COPY --from=builder /usr/local/src/teabot
# RUN python3 setup.py sdist bdist_wheel