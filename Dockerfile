FROM python:3.7

# Copy the detect.py file into the container
ADD detect.py .

# Install the required Python packages
RUN pip install opencv-contrib-python cvlib gtts playsound
RUN pip3 install PyObjC

# Set the default command to run the detect.py script
CMD ["python", "./detect.py"]