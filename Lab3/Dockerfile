FROM python:latest
RUN pip install -r requirements.txt
ENTRYPOINT [ "python3", "-m", "uvicorn", "main:app", "--host=0.0.0.0" ]