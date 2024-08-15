# Video-Streaming (Validated on Raspberry Pi 5 and Camera Module 3)
This turtorial includes thr

## 1. Video Streaming on Raspberry Pi
   Download file mjpeg_server.py and run python mjpeg_server.py. It'll streams Mjpeg format's video. \
   Access http://192.168.0.210:8000/stream.mjpg. You'll see the video. 

## 2. Public access
If you want your video streaming can be accessed on public network. There are two ways of implementing that. 
* IP binding on your router
* DNS binding using third-party package \
There is already millions of blog introducing how to do IP binding on the router.\
Follow this link to bind DNS with your IP: https://dashboard.ngrok.com/get-started/setup/linux \
The network traffic goes through their edge servers. Need to subscribe after surpassing the limits.

## 3. Stepper Motor Control
Here we use 16-channel drive circuit to drive the stepper motor.



   
   























This file introduces playbacking live video from Raspberry Pi on Unity, including three parts:
* Use Motion to setup video streaming on Raspberry Pi
* Expose ports on Raspberry Pi on public network
* Use vlc-unity plugin to playback video on Unity 

## Video streaming
### Use Motion to setup video streaming on Raspberry Pi (motion seems not campatible with Raspberry pi 4 and 5)
Follow this link: https://pimylifeup.com/raspberry-pi-webcam-server/ \
**notes**: 
  * Motion Codec: MPJEG (Use less CPU resources to encode, but with less compression rates compared to other codec formats)
  * Need to adjust the parameters in /etc/motion/motion.conf. Or this video will be luggy. (Follow the link above)

### Use Python to build a server on Raspberry Pi (Test on Raspberry Pi 5 and Camera Moudule 3)
Run sample code /mjpeg_server.py

## Expose ports on Raspberry Pi on public network
There is two methods to expose your port on Raspberry Pi to public network 
1. Set up Port Forwarding on your router
   Log in to the management page of your router, and find port forwarding \
   **notes**: 
     * Don't use campus network. There is a firewall blocking you accessing ports on Raspberry Pi.
  
2. Bind Domain name to your local network ip \
   Set up a reverse proxy to expose your local service on public network. Follow this link: https://dashboard.ngrok.com/get-started/setup/linux \
   The network traffic goes through their edge servers. Need to subscribe after surpassing the limits.

## Use vlc-unity plugin to playback video on Unity
Because the video format is in MJPEG, I only find vlc-unity plugin supporting to plalback video in this format. 
1. Set up a empty project in Unity.
2. Import the vlc-unity package. There is a package called Vlc Canvas Example.unity. Open it.
   ![The San Juan Mountains are beautiful!](/unity.png "San Juan Mountains")
3. Update the url
   ![The San Juan Mountains are beautiful!](/url.png "San Juan Mountains")
