FROM python:3.9-bookworm

# gnupg is required for apt-key
RUN apt-get update -y && apt-get install -y && rm -rf /var/lib/apt/lists/*

# create user
RUN groupadd mongofastapi && useradd --create-home -g mongofastapi apiuser
ENV PATH /home/apiuser/.local/bin:${PATH}

WORKDIR /home/apiuser/mongofastapi/

ADD . .

RUN chmod 777 -R .

USER apiuser
# Set pip configuration

RUN pip install -r requirements.txt