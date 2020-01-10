
FROM ubuntu
LABEL maintainer "AbdalazizRashid<abdalaziz.rashid@outlook.com>"
ADD . /app
WORKDIR /app

# Make sure everything is updated
RUN apt-get update -y && apt-get upgrade -y

# Install package needed for Miniconda
RUN apt-get install -y wget curl bzip2 libpython3-dev libboost-python-dev

# Download anaconda install
RUN curl -O https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh

# Turn executable attribute
RUN chmod +x Miniconda3-latest-Linux-x86_64.sh

# Install Anaconda
RUN bash Miniconda3-latest-Linux-x86_64.sh -b

# Remove Instalation file
RUN rm Miniconda3-latest-Linux-x86_64.sh

# Add Anaconda to the Path
ENV PATH /root/miniconda3/bin:$PATH

# Run bash. From there you can use pip or conda to install needed packages
RUN conda install -c conda-forge spacy &&\
python -m spacy download en &&\
conda install -c conda-forge textacy &&\
python3 -m spacy download en_core_web_lg &&\
pip install -r requirements.txt
EXPOSE 5000 5001 80 
ENV PORT 5000
#CMD ["export", "PYTHONPATH=.", " "python", "app.py"]
CMD ["./start.sh"]
#CMD ["bash"]
#ENTRYPOINT [ "python" ]
#CMD [ "app.py" ]
