# detecor_on_pi

This repo has fundemental instruction for drone detctor on pi. Rasbian used as operating system.

### prerequisite

We need pyaudio for recording sound, torch for inference, librosa for MFCC.    
Following instruction will help you prepare prerequisite.
```
sudo apt-get update
```
```
sudo apt-get install python3 libopenblas-dev python3-pyaudio python3-scipy llvm-7 -y
```
```
pip3 install torch-1.0.0a0+8322165-cp37-cp37m-linux_armv7l.whl torchvision colorama==0.3.9
```
```
cd /usr/bin
sudo ln -s llvm-config-7 llvm-config
```
```
pip3 install librosa pandas
```
