FROM python:3.9-bookworm

ARG PIP_SET_CONFIG
ARG GLOBAL_PIP_SET_CONFIG

# gnupg is required for apt-key
RUN apt-get update -y && apt-get install -y

# create user
RUN groupadd trackingapi && useradd --create-home -g trackingapi apiuser
ENV PATH /home/apiuser/.local/bin:${PATH}

WORKDIR /home/apiuser/trackingapi/

ADD . .

RUN chmod 777 -R .

USER apiuser
# Set pip configuration
RUN ${PIP_SET_CONFIG}
RUN ${GLOBAL_PIP_SET_CONFIG}


RUN pip install -r requirements.txt