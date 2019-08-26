# The present work implements a lightweight microsimulation free-flow acceleration model (MFC) that is able to capture the vehicle acceleration dynamics accurately and consistently, it provides a link between the model and the driver and can be easily implemented and tested without raising the computational complexity. The proposed model has been developed by the Joint Research Centre of the European Commission. 

# Please cite: Makridis, M., Fontaras, G., Ciuffo, B.F., Mattas, K., 2019. MFC free-flow model: Introducing vehicle dynamics in microsimulation. TRR.

## User guidelines for co2mpas_driver library
This page contains user guidelines intended for first users of co2mpas_driver model.
It contains the explanations and definitions required to understand how to use
the model, understand its needs, and analyse its outputs. These guidelines are
written for users without specific IT knowledge.

This work proposes the microsimulation a free-flow acceleration model (MFC) 
that is based on two parameters that can be calibrated, gear-shifting style and 
driver style, as well as the vehicle specifications, which are used to compute 
the maximum acceleration that the vehicle can have at a given speed. The basis 
of the MFC is the vehicle acceleration curve, which represents the maximum 
acceleration that the car can achieve for a given speed which, in this work, 
is often noted as acceleration potential. On the top of the vehicle-specific curve, 
MFC is parametrized by the gear-shifting style and the driving style. Both elements 
are important mainly for the assessment and accurate estimation of the energy 
demand and efficiency of a transport system, comprised by a fleet of vehicles 
that can be diverse both in relation to size (small, medium, and large light-duty
 vehicles) and characteristics (hatchbacks, station wagons, pick-ups), but also 
 propulsion and driving technology (hybrids, electric, automated vehicles etc.). 
 MFC is simple to implement, it has low computational cost and, by comparison 
 with both the Gipps (6) and the Intelligent Driver Model (IDM) (28), it proves 
 its robustness for various vehicles, drivers, and driving styles.
 
For more information you may find the publication :
https://journals.sagepub.com/ 


 
## How to package new_MFC project for distribution
<!--move them to CONTRIBUTING.md -->

1. **Register on PyPi**: https://pypi.org/account/register/ or GitHub and upload 
    to make your package be accessible publicly.
    
2. **Check the required tools**
    It is important to make sure that pip, setuptools, and wheel are up to date      
    
        python -m pip install --upgrade pip setuptools wheel
        
3. **Setup your project**
    create a setup.py file in your project root directory. This file will contain
    all of the packages metadata information. In the project folder we have
    a package with an \__init__.py file that plots the work flow of the whole 
    project. we have also the README.md and LICENSE.txt for the licence of the
    project.
    
    The project folder structure looks like: 
    
        new_MFC
        ├───LICENSE.txt
        ├───bin
        ├───new_MFC
        │   ├───common
        │   ├───db
        │   ├───examples
        │   ├───test
        ├───MANIFEST.it
        ├───README.md
        ├───requirements.txt
        ├───setup.py
        └───.gitignore

4. **Compile your package**
   Change your directory into the root of the project and execute the command below
   depending on the system environment.
   
   1. **Source distribution**
   
        This only provides a meta data and the essential source files needed 
        to build an installable format. This can be generated by:
        
            python setup.py sdist
   
   2. **Built distribution**
         
         **wheel format**
         
            python setup.py bdist_wheel
            
         **Creating Windows Installers**
            
            python setup.py bdist_wininst
            
         or the **bdist** command with the --formats option:
         
            python setup.py bdist --formats=wininst
            
         to build a 64bit version of your extension.
         
            python setup.py build --plat-name=win-amd64 bdist_wininst
          
          create an MSI installer
          
             python setup.py bdist_msi
            
         This will create a folder structure like this:

            new_MFC
            ├───LICENSE.txt
            ├───bin
            ├───build
            │   ├───bdist.win-amd64
            │   └───lib
            │       └───new_MFC
            │           ├───common
            │           ├───db
            │           ├───examples
            │           └───test
            ├───dist
            │   ├───new_MFC-1.0.0-py2.py3-none-any.whl
            ├───new_MFC
            │   ├───common
            │   ├───db
            │   ├───examples
            │   ├───test
            ├───new_MFC.egg-info
            ├───MANIFEST.it
            ├───README.md
            ├───requirements.txt
            ├───setup.py
            └───.gitignore
            
         * **Build** build package information.
         * **dist** This contains the wheel file format which is the standard 
            built package.
         * **new_MFC.egg-info** This contains compiled byte code, package 
            information, and also saves information used by the setup file
 
5. **Install on your local machine**
    You can install on your machine using:
    
        pip install dist/new_MFC-1.0.0-py2.py3-none-any.whl
        
6. **Uninstall your package**

        pip uninstall new_MFC
        
   or if you don't know the list of all files, you can reinstall it with the
   --record option, and take a look at the list this produces.
   
   To record a list of installed files, you can use:
   
        python setup.py install --record files.txt
        
   Once you want to uninstall you can use xargs to do the removal:
   
   **windows**
   
        Get-Content files.txt | ForEach-Object {Remove-Item $_ -Recurse -Force}
        
   **linux** you can use xargs to do the removal
   
        xargs rm -rf < files.txt

7. **Upload on pip or import under new_MFC repository Github**

    1. **Create pypirc:** The Pypirc file stores the PyPi repository information. 
    Create a file in the home directory
    
        1. **for Windows** :  C:/Users/UserName/.pypirc
        2. **for** ***nix** :   ~/.pypirc  

## How to download and Install co2mpas_driver library.
8. **Conclusion**
    This package can be installed easily on any machine that has pip
    
        pip install new_MFC 

[1]: https://ljvmiranda921.github.io/notebook/2018/06/21/precommits-using-black-and-flake8/
[2]: https://black.readthedocs.io/                   