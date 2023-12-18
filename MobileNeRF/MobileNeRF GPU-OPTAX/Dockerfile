# Use the official NVIDIA CUDA image as the base image
FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04
RUN apt update && apt install python3 python3-pip -y
RUN pip install "jax[cuda11_cudnn86]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html
RUN apt-get install -y libgl1-mesa-dev
RUN apt-get install -y libglib2.0-0

COPY datasets /app/datasets
COPY requirements.txt /app
COPY *.py /app
COPY *.html /app

ARG DEBIAN_FRONTEND=noninteractive

# Set the working directory
WORKDIR /app

# Install any additional dependencies required for MobileNeRF
# For example, if there are specific libraries or packages needed, install them here.

# Copy the MobileNeRF code and files into the container
#COPY . /app

RUN pip install -r requirements.txt

# Set the entry point to run the stage1OPTAX.py script
ENTRYPOINT ["python3", "stage1OPTAX.py"]
# Set any environment variables, if needed
# ENV MY_VARIABLE=value

# Build or configure MobileNeRF (adjust as needed)
# RUN make

# Expose any necessary ports (if applicable)
# EXPOSE 8080

# Define the command to run your application
# CMD ["./my_application"]

# Tag the image with the specified version
# Replace '1.0.0' with the desired version number
# For example, if you are building version 1.0.1, change it to '1.0.1'
# The tag helps you identify different versions of your Docker image
# It's a good practice to use semantic versioning (https://semver.org/)
# for versioning Docker images
# For the initial version, you can leave it as '1.0.0'
# Other common version formats are 'v1.0.0' or 'latest'
# Choose a versioning strategy that best fits your project's needs
# and update the version accordingly as you make changes to the image
# or the underlying application
# Example: docker build -t mobilenerf:1.0.0 .
ENV GODEBUG=netdns=go

ENV XLA_PYTHON_CLIENT_PREALLOCATE=false
ENV XLA_PYTHON_CLIENT_MEM_FRACTION=.9
ENV XLA_PYTHON_CLIENT_ALLOCATOR=platform
