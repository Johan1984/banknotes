
# This will be the image. Can be found on docker website. This installs python
FROM python:3.10.6-buster

# Copy will copy all files necessary for you to use on your docker image. Like installing something on you own laptop

COPY app /app

COPY requirements.txt /requirements.txt

COPY classifier.pkl /classifier.pkl

COPY BankNotes.py /BankNotes.py

# You use the run to install dependancies. This will install it into docker image

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

# You need to tell docker that it needs to start the uvicorn server
# app.simple:app will be broken down as app(folder).simple(py file):app(what api was called inside py file app = FastAPI())
CMD uvicorn app.simple:app --host 0.0.0.0 --port $PORT
