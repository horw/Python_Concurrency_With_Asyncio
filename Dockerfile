FROM python:3

WORKDIR /usr/src/app

COPY /chapter_3/listing3_10.py .

COPY util util/

#RUN /bin/bash
#CMD["--version"]
CMD ["python", "listing3_10.py"]