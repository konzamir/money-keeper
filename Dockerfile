FROM python:3.8

COPY . /usr/src/
WORKDIR /usr/src/
RUN pip install -r requirements.txt
ENV PROCESS_COUNT=2
ENV LOG_LVL=info

ENTRYPOINT [ "celery", "worker", "-A",
             "app", "-l", "${LOG_LVL}", "-Q",
             "task_get_updates,celery",
             "-c", "${PROCESS_COUNT}",
             "-B", "-E" ]
