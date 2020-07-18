# PythonPackagesIntro (Distribution Package)
This just shows how to implement packages in python with OOP principles.
Two classes Binomial and Gaussian are inherited from the parent class Distribution. 
It has various methods like, claculate_mean(), calculate_standardDeviation() etc. 
A text file containing a list of data, can be read through the read_data_file() method.
Refer the example.py file to get a small idea on how the programs work.

# Pip installing this into your local system:
Before pip install make sure that you are in the same directory as that of the setup.py file.
Pip looks for setup.py file during installation which contains meta data about the package.
Type: [pip install .] in the terminal.
The "." tells pip to look for the setup.py file in the current directory.

Please note that the name of the package is Distributions as the "init.py" file is in that directory. 
The "init.py" tells python that the folder contains a package.
A package must need an "ini.py" file, even if the file is empty.


