FROM python:3.8-slim

#env
USER root
WORKDIR /app
COPY src .
RUN mkdir input
RUN mkdir output
RUN apt-get update \
    && apt-get install -y --no-install-recommends openjdk-17-jdk unzip wget \
    && rm -rf /var/lib/apt/lists/*

#wabt
RUN wget https://github.com/WebAssembly/wabt/releases/download/1.0.33/wabt-1.0.33-ubuntu.tar.gz 
RUN tar -xvf ./wabt-1.0.33-ubuntu.tar.gz 
RUN mv ./wabt-1.0.33/bin ./bin
RUN chmod +x ./bin/

#ghidra
# RUN wget https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_10.3.2_build/ghidra_10.3.2_PUBLIC_20230711.zip -O ghidra.zip \
#     && unzip ghidra.zip \
#     && rm ghidra.zip \
#     && mv ghidra_* ghidra


# #wasm plugin
# RUN wget https://github.com/nneonneo/ghidra-wasm-plugin/releases/download/v2.2.0/ghidra_10.3.2_PUBLIC_20230804_ghidra-wasm-plugin.zip

#python

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000

CMD [ "python", "./app.py" ]