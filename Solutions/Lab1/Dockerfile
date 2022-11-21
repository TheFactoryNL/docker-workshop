FROM python:latest
COPY src/ /tmp/src
WORKDIR /tmp/src
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]

# docker run -d -p 5000:5000 pythonlab
# docker run -p 5000:5000 pythonlab