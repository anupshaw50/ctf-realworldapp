# ctf-realworldapp
This is a vulnerable flask app which is similar to real world applications found in wild.

## How To Install The App

```sh
apt install python3
apt instal python3-pip
pip3 install -r requirements.txt
pip3 install gevents
```

## How To Run The App
```sh
python3 gevents.py 3000
```

## Docker Container For Easy Deployment 
Find the docker image  [HERE](https://hub.docker.com/r/anupshaw50/onlinectfwsa)

Command to run
```sh 
docker run -p 3000:3000 anupshaw50/onlinectfwsa
```
## Want To Try Live ?
 - Goto https://labs.play-with-docker.com/
 - Login/SignUp and Start to enter in the dashboard
 - Click on Add new instance
 - Paste the docker run command ```docker run -p 3000:3000 anupshaw50/onlinectfwsa```
 - Click on OpenPort and open port 3000
