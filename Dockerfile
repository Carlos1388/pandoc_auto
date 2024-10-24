FROM pandoc/extra:latest

# Set the working directory
WORKDIR /workspace

# Copy your local files to the container
COPY . /workspace

# install pdfroff
RUN apk add groff

# install ghostscript
RUN apk add ghostscript

# install weasyprint 
RUN apk add weasyprint

# Set the entrypoint to pandoc
ENTRYPOINT ["pandoc"]

# this dockerfile is built using the following command
# docker build -t pandoc_mod -f Dockerfile .
