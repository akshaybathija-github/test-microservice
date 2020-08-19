## The Makefile includes instructions on environment setup
# Create and activate a virtual environment
# Install dependencies in requirements.txt

setup:
	# Create python virtualenv & source it
	# source ~/.devops/bin/activate

install:
	# This should be run from inside a virtual environment
	# Install packages from pip, use requirements.txt
	pip install -r requirements.txt

docker-build:
	# add commands required
	docker build -t microservice_newj .
docker-push:
	# add commands required
	docker push akshaybathija/microservice_newj