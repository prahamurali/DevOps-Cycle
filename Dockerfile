FROM python:3
RUN pip install --upgrade pip
WORKDIR /app
COPY . /app
RUN pip3 --no-cache-dir install flask
RUN pip3 --no-cache-dir install psycopg2
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["app.py"]