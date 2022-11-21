FROM python:latest
COPY src/ /tmp/src
WORKDIR /tmp/src
RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT [ "python3", "-m", "uvicorn", "main:app", "--host=0.0.0.0" ]

# docker run -d -p 5000:5000 pythonlab
# docker run -p 5000:5000 pythonlab