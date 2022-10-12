# Introduction
---
Use opencv, flask and ngrok with python to stream feeds
of RTSP based cameras for the Discover test site specifically for the 
upcoming NSF demo.

# Dependencies
---
- Assumes you are using some type of linux-based (or OSX) environment. 

### Minimal dependencies
**Fetch updates**
```
$ sudo apt-get update
```

**Install Docker**
Can use this method or your own. 
```
$ curl -sSL https://get.docker.com | sh
```
- add user to docker grp and fix perms on docker sock <br>
        ```
        $ sudo usermod -aG docker pi
        $ sudo chmod 666 /var/run/docker.sock 
        ``` <br>
- confirm installation by checking version and running hello world container <br>
        ```
        $ docker --version
        $ docker run hello-world
        ``` <br>

**For GTK GUI features**
```
$ sudo apt-get install libgtk-3-dev
```

**Python 3 support**
```
$ sudo apt-get install python3-dev python3-numpy
```

**pip for easy installation of python modules**
```
$ sudo apt-get -y install python3-pip
```
**Install ngrok for proxying, making localhost visible to outside**
```
$ sudo apt install ngrok &&
pip3 install ngrok-api
```
Visit here for more directions: https://github.com/ngrok/ngrok-api-python
- You'll want to [create an ngrok account](https://dashboard.ngrok.com/get-started/setup) and 
add your authtoken to the ngrok agent as well as add your API-key to /src/test_stream_v1.py <br>
        ```
        $ ngrok config add-authtoken <authtoken>
        ``` <br>
- after setting up ngrok open up port 5000 to forward publicly <br>
        ```
        $ ngrok http 5000
        ``` <br>
this will open an ngrok session and provide you with the generated public facing
URL of your project.

Install our python dependencies using pip
**datetime, openCV, Flask, imutils**
```
$ pip3 install datetime opencv-python flask imutils
```

# Build this project
---
**with Docker**
```
$ git clone git@github.com:DiscoverCCRI/ip_cam.git &&
cd /scripts 
$ docker build -t ip_cam . &&
docker image ls
$ docker container run --privledged -d ip_cam
```
**manually**
```
$ git clone git@github.com:DiscoverCCRI/ip_cam.git &&
cd ip_cam/src &&
python3 test_stream_v1.py proxy_stream.py
```
Enter the IP address of the machine you are hosting this project from in a browser
and your feed should be present. 

# Issues
---
Issues I ran into when installing on Raspian on RPI 4
  - When installing imutils there might be some errors, to fix I installed
  these packages and fixed some various issues with numpy
    ```
    pip3 install opencv-python
    sudo apt-get install libcblas-dev
    sudo apt-get install libhdf5-dev
    sudo apt-get install libhdf5-serial-dev
    sudo apt-get install libatlas-base-dev
    sudo apt-get install libjasper-dev 
    sudo apt-get install libqtgui4 
    ```
  - Issues with numpy on my local machine with bad versions. To fix:
    ```
    $ pip3 install -U numpy
    ```
    
# ZoneMinder
Zoneminder is an opensource alternative to applications like VLC and is linux-based. 

clone the repo from [here](https://github.com/ZoneMinder/zmdockerfiles)
```
$ git clone git@github.com:ZoneMinder/zmdockerfiles.git
```
and simply run with docker
```
docker run -d -t -p 8080:80 \
    -e TZ='America/Phoenix' \
    -v ~/zoneminder/events:/var/cache/zoneminder/events \
    -v ~/zoneminder/images:/var/cache/zoneminder/images \
    -v ~/zoneminder/mysql:/var/lib/mysql \
    -v ~/zoneminder/logs:/var/log/zm \
    --shm-size="512m" \
    --name zoneminder \
    zoneminderhq/zoneminder:latest-ubuntu18.04
```
The application will now be viewable at http://localhost:1080/zm/

