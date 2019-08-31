FROM python:3.4-alpine
ADD * /code/
WORKDIR /code
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 8080
CMD [ "python", "app.py" ]
