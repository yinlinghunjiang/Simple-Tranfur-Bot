FROM python:3.8

WORKDIR ./Simple-Transfur-Bot
 
ADD . .

RUN pip install -r requirements.txt


CMD ["python", "bot.py"]