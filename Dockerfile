FROM python:3.7

# Copy the main.py file into the container
ADD main.py .

# Install the required Python packages
RUN pip install opencv-contrib-python cvlib gtts playsound
RUN pip3 install PyObjC

# Set the default command to run the main.py script
CMD ["python", "./main.py"]