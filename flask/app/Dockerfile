FROM python:rc-alpine
ADD * /code/
WORKDIR /code
RUN apk add curl bind-tools
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 8080
CMD [ "python", "app.py" ]
