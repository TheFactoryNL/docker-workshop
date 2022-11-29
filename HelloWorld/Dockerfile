FROM amazoncorretto:19
COPY . /tmp
WORKDIR /tmp
RUN javac HelloWorld.java
ENTRYPOINT [ "java", "HelloWorld" ]