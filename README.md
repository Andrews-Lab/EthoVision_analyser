# EthoVision XT 14 Analyser 🐁

### Overview

__Noldus EthoVision XT 14 Analyser__

[Noldus EthoVisoin XT](https://www.noldus.com/ethovision-xt) is a video tracking software that allows the position of rodents in videos to be analysed over time.
This can indicate the time spent in the dark zone of a light-dark box, the closed arms of an elevated plus maze, etc.
It also allows the manual annotation of rodent behaviours over time (manual scoring).

<p float="center">
  <img src="https://user-images.githubusercontent.com/101311642/205425743-83fd6516-aa17-442b-bc23-45a3cb728790.png" width="30%" />
  <img src="https://user-images.githubusercontent.com/101311642/205426201-e7c84d6f-30cd-4a05-af8a-e6f43e89c155.png" width="30%" /> 
</p>

__Purpose__

This code organises the excel output files from the BioDaq Food and Water Intake Monitor into time bins. <br>
It can also group the time binned data by individual stats and animals.

__Preview of the graphical user interface__

<p align="center">
  <img src="https://user-images.githubusercontent.com/101311642/205285449-ec27c443-c094-4660-999e-f5159e5d0a20.png" width="440">
</p><br/>

__Input and output data__

<p align="center">
  <img src="https://user-images.githubusercontent.com/101311642/205290754-cb911936-6727-47ce-bef5-65f2e03f62c4.png" width="530">

![image](https://user-images.githubusercontent.com/101311642/205293854-a98c4332-d0f3-4c95-9beb-17c0362e8082.png)

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