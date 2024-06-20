# Video-Streaming
This file introduces playbacking live video from Raspberry Pi on Unity, including three parts:
* Use Motion to setup video streaming on Raspberry Pi
* Expose ports on Raspberry Pi on public network
* Use vlc-unity plugin to playback video on Unity 

## Use Motion to setup video streaming on Raspberry Pi
Follow this link: https://pimylifeup.com/raspberry-pi-webcam-server/ \
**notes**: 
  * Motion Codec: MPJEG (Use less CPU resources to encode, but with less compression rates compared to other codec formats)
  * Need to adjust the parameters in /etc/motion/motion.conf. Or this video will be luggy. (Follow the link above)
  
## Expose ports on Raspberry Pi on public network
There is two methods to expose your port on Raspberry Pi to public network 
1. Set up Port Forwarding on your router
   Log in to the management page of your router, and find port forwarding
   **notes**:
     Don't use campus network. There is a firewall blocking you accessing ports on Raspberry Pi.
  
2. Bind Domain name to your local network ip
   Set up a reverse proxy to expose your local service on public network. Follow this link: https://dashboard.ngrok.com/get-started/setup/linux
   The network traffic goes through their edge servers. Need to subscribe after surpassing the limits.

## Use vlc-unity plugin to playback video on Unity
Because the video format is in MJPEG, I only find vlc-unity plugin supporting to plalback video in this format. 
1. Set up a empty project in Unity.
2. Import the vlc-unity package. There is a package called Vlc Canvas Example.unity. Open it.
   ![The San Juan Mountains are beautiful!](/unity.png "San Juan Mountains")
3. Update the url
   ![The San Juan Mountains are beautiful!](/url.png "San Juan Mountains")
