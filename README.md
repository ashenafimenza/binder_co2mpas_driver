# The present work implements a lightweight microsimulation free-flow acceleration model (MFC) that is able to capture the vehicle acceleration dynamics accurately and consistently, it provides a link between the model and the driver and can be easily implemented and tested without raising the computational complexity. The proposed model has been developed by the Joint Research Centre of the European Commission. 

# Please cite: Makridis, M., Fontaras, G., Ciuffo, B.F., Mattas, K., 2019. MFC free-flow model: Introducing vehicle dynamics in microsimulation. TRR.

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
    a package with an __init__.py file that plots the work flow of the whole 
    project. we have also the README.md and LICENSE.txt for the licence of the
    project.
    
    The project folder structure looks like: 
    
        new_MFC
        ├───.idea
        │   └───dictionaries
        ├───.pytest_cache
        │   └───v
        │       └───cache
        ├───bin
        ├───new_MFC
        │   ├───common
        │   │   └───__pycache__
        │   ├───db
        │   ├───examples
        │   │   └───__pycache__
        │   ├───test
        │   └───__pycache__
        └───__pycache__

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
            
         This will create a folder structure like this:

            new_MFC
            ├───.idea
            │   └───dictionaries
            ├───.pytest_cache
            │   └───v
            │       └───cache
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
            ├───new_MFC
            │   ├───common
            │   │   └───__pycache__
            │   ├───db
            │   ├───examples
            │   │   └───__pycache__
            │   ├───test
            │   └───__pycache__
            ├───new_MFC.egg-info
            └───__pycache__

         * **Build** build package information.
         * **dist** This contains the wheel file format which is the standard 
            built package.
         * **new_MFC.egg-info** This contains compiled byte code, package 
            information, and also saves information used by the setup file

5. **Install on your local machine**
    You can install on your machine using:
    
        python -m pip install dist/new_MFC-1.0.0-py2.py3-none-any.whl
        
6. **Uninstall your package**

        pip uninstall package name
        
   or if you don't know the list of all files, you can reinstall it with the
   --record option, and take a look at the list this produces.
   
   To record a list of installed files, you can use:
   
        python setup.py install --record files.txt
        
   Once you want to uninstall you can use xargs to do the removal:
   
   **windows**
   
        Get-Content files.txt | ForEach-Object {Remove-Item $_ -Recurse -Force}
        
   **linux** you can use xargs to do the removal
   
        xargs rm -rf < files.txt

7. **Upload on pip or import under JRCSTU repository Github**

    1. **Create pypirc:** The Pypirc file stores the PyPi repository information. 
    Create a file in the home directory
    
        1. **for Windows** :  C:/Users/UserName/.pypirc
        2. **for** ***nix** :   ~/.pypirc  

8. **Conclusion**
    This package can be installed easily on any machine that has pip
    
        pip install new_MFC 

[1]: https://ljvmiranda921.github.io/notebook/2018/06/21/precommits-using-black-and-flake8/
[2]: https://black.readthedocs.io/                   