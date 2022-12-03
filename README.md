# EthoVision XT 14 Analyser 🐁

### Overview

__Noldus EthoVision XT 14 Analyser__

[Noldus EthoVision XT](https://www.noldus.com/ethovision-xt) is a video tracking software that allows the position of rodents in videos to be analysed over time. <br>
This can indicate the time spent in the dark zone of a light-dark box, the closed arms of an elevated plus maze, etc. <br>
It also allows the manual annotation of rodent behaviours over time (manual scoring).

![image](https://user-images.githubusercontent.com/101311642/205426919-ff706f7d-11b2-4e39-90ef-f725043e64fb.png)

__Purpose__

This code extends on the functions for analysing manually scored behaviours in EthoVision XT 14. It can: <br>
* Create visual barcodes of behaviours over time
* Re-create data about the time spent doing behaviours and number of behavioural bouts.
This will also make a group of behaviours mutually exclusive, if they are not already. <br>
This can be done by importing the raw tracking data from EthoVision XT. <br>
Currently, only version 14 of this software has been tested.

__Preview of the graphical user interface__

![image](https://user-images.githubusercontent.com/101311642/205427812-4c3e3e2c-4526-472e-8e2a-4cf45d1ad3cc.png)

__Input and output data__

![image](https://user-images.githubusercontent.com/101311642/161454794-a0dea082-6f06-43ad-85e8-0e4d21a9b9a9.png)
![image](https://user-images.githubusercontent.com/101311642/161454762-64cef9d2-8925-4696-ae61-fae87e630365.png)

### Installation

Install [Anaconda Navigator](https://www.anaconda.com/products/distribution). <br>
Open Anaconda Prompt (on Mac open terminal and install X-Code when prompted). <br>
Download this repository to your home directory by typing in the line below.
```
git clone https://github.com/Andrews-Lab/Intake_monitor_time_bins.git
```
Change the directory to the place where the downloaded folder is. <br>
```
cd Intake_monitor_time_bins
```

Create a conda environment and install the dependencies.
```
conda env create -n IMTB -f Dependencies.yaml
```

### Usage
Open Anaconda Prompt (on Mac open terminal). <br>
Change the directory to the place where the git clone was made.
```
cd Intake_monitor_time_bins
```

Activate the conda environment.
```
conda activate IMTB
```

Run the codes.
```
python Intake_monitor.py
```

### Guide

View the guide about [how to analyse your intake monitor data](How_to_use_intake_monitor_codes.pdf).

<br>

### Acknowledgements

__Author:__ <br>
[Harry Dempsey](https://github.com/H-Dempsey) (Andrews lab and Foldi lab) <br>

__Credits:__ <br>
Nikita Bajaj, Sarah Lockie, Zane Andrews <br>

__About the labs:__ <br>
The [Lockie lab](https://www.monash.edu/discovery-institute/lockie-lab) studies how hunger signalling in the brain drives mood-related behaviour, memory, motivation and metabolism in mouse models of disease. <br>
The [Andrews lab](https://www.monash.edu/discovery-institute/andrews-lab) investigates how the brain senses and responds to hunger. <br>
The [Foldi lab](https://www.monash.edu/discovery-institute/foldi-lab) investigates the biological underpinnings of anorexia nervosa and feeding disorders. <br>
