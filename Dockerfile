# use python:3.11 base image
FROM python:3.11-slim
# set the working directory
WORKDIR /app
# copy the requirements file
COPY requirements.txt .
# install the dependencies
RUN pip install --no-cache-dir -r requirements.txt
# copy the application code
COPY . .
# expose the port the app runs on
EXPOSE 8000

# command to run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]