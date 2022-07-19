#FROM python:3

#WORKDIR /usr/src/app

#COPY /chapter_3/listing3_10.py .

#COPY util util/

#EXPOSE 9898
#RUN /bin/bash
#CMD["--version"]
#CMD ["python", "listing3_10.py"]
#CMD ["python", "smpl.py"]



FROM python:3

WORKDIR /usr/src/app


COPY chapter_8/ chapter_8

COPY util util/



#RUN /bin/bash
#CMD["--version"]
CMD ["python", "chapter_8/listing8_5.py"]
#CMD ["python", "smpl.py"]