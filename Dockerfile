FROM python:3.7-slim

RUN sed -i 's#http://deb.debian.org#https://mirrors.163.com#g' /etc/apt/sources.list
RUN apt update && apt install -y libglib2.0-dev libsm6 libxrender1 libxext-dev supervisor build-essential libgl1-mesa-glx \
        && rm -rf /var/lib/apt/lists/*

RUN mkdir ./hn_ocr

RUN /usr/local/bin/python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
COPY ./requirements.txt ./hn_ocr/
RUN pip3 install -r ./hn_ocr/requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
COPY . ./hn_ocr

RUN python3 ./hn_ocr/install.py
EXPOSE 8898
CMD ["supervisord","-c","/hn_ocr/supervisord.conf"]
