FROM python:3.11.8
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     libpq-dev \
#     python3-dev \
#     python3-pip \
#     python3-setuptools \
#     python3-wheel \
#     uwsgi \
#     libz-dev libjpeg-dev libfreetype6-dev \
#     uwsgi-plugin-python3 \
#     && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
CMD uwsgi --http=0.0.0.0:80 --module=backend.wsgi