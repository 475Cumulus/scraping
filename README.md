# Containerized Web Scraping Development Environment

This project provides a basic dockerized development environment for web scraping, based on Python


### Building the image

    $ docker build -t 475cumulus/scraping .

### Running the container in interactive shell

    $ docker run -it -v $(pwd):/usr/src 475cumulus/scraping /bin/sh


Note that running the container provides a shell into the container, where the folder  `/usr/src` is mapped to your project's root folder

