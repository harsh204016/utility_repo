FROM ubuntu:latest

WORKDIR /usr/app/src

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        apt-utils\
        locales\
        python3-pip \ 
        python3-yaml \
    &&  apt-get clean

RUN pip3 install --upgrade pip
RUN pip3 install streamlit 

COPY / ./

CMD ["streamlit","run","app.py"]
