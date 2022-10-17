# Introduction
---
Using zoneminder to monitor the Discover CCRI test site with multiple
RTSP based IP cameras. 

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
add user to docker grp and fix perms on docker sock <br>
```
$ sudo usermod -aG docker pi
$ sudo chmod 666 /var/run/docker.sock 
```
confirm installation by checking version and running hello world container 

# Build this project
---
enter the zmdockerfiles directory and run:
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
The application will now be viewable at http://localhost:8080/zm/

```
$ docker --version
$ docker run hello-world
```        
**Install ngrok for proxying, making localhost visible to outside**

```
$ python3 -m pip install pyngrok
```
Visit here for more directions: https://pyngrok.readthedocs.io/en/latest/
- You'll want to [create an ngrok account](https://dashboard.ngrok.com/get-started/setup) and 
add your authtoken to the ngrok agent as well as add your API-key to the ngrok config file. 
```
$ ngrok config add-authtoken <authtoken>
``` 
- after setting up ngrok open up port 8080 to forward publicly 
- run the reverse_proxy.py script
```
$ ngrok http 5000
``` 
this will open an ngrok session and provide you with the generated public facing
URL of your project.

