# conda virtual env 

Conda uses few directory for packages and default virtualenvs path. They can be set in ~/.condarc .  However ~/.condarc as well as other ~/.\* files  will be lost once sciserver container restart.   Suggest  create a init script in persistent storage area which you run everytime you start/restart container.  And the init script can copy a saved .condarc file to ~/.condarc.
Here is a sample .condarc file. 

```bash
envs_dirs:
  - /home/idies/workspace/Storage/{YourUsername}/persistent/conda/conda_envs
pkgs_dirs:
  - /home/idies/workspace/Storage/{YourUserName}/persistent/conda/conda_pkgs
```

Make sure mentioned directory exist
An Sample init.sh script you run everytime start/restart container can be like this:
```bash
#/bin/bash


# script you run every time your container start or restart
#to customerize container


#please change it to your username 
#in the container it maybe found under 
#ls  ${HOME}/workspace/Storage/
MY_USERNAME=johndoe


export MY_TMPDIR=${HOME}/workspace/Temporary/${MY_USERNAME}/scratch/tmp




#if you need preserver those directory, 
rm -rf ~/.cache
if [ ! -d ${MY_TMPDIR}/.cache ] ; then
 mkdir -p ${MY_TMPDIR}/.cache
fi
ln -s ${MY_TMPDIR}/.cache ${HOME}/.cache




##if you really going to generate huge temperary data in /tmp
## consider redefine TMPDIR
#export TMPDIR=$MY_TMPDIR


# if you have  customerized .bashrc etc , copy it over or link it.
export my_username=$(ls /home/idies/workspace/Storage)
if [ -f /home/idies/workspace/Storage/${my_username}/persistent/init/.bashrc ]; then
cp  /home/idies/workspace/Storage/${my_username}/persistent/init/.bashrc ${HOME}/.bashrc
 ln -sf  /home/idies/workspace/Storage/${my_username}/persistent/init/.bashrc ${HOME}/.bashrc
fi


# if you use conda env  and have .condarc might want cp or link
if [ -f /home/idies/workspace/Storage/${my_username}/persistent/conda/.condarc ] ; then
cp  /home/idies/workspace/Storage/${my_username}/persistent/conda/.condarc ${HOME}/
ln -sf  /home/idies/workspace/Storage/${my_username}/persistent/conda/.condarc ${HOME}/.condarc
fi


# if you have created your own jupyter kernels
# and made backup from ./local/hare/jupyter/kernels/
# you can copy back to container or link it
# if you want you can relink whole .local folder too
if [ -d /home/idies/workspace/Storage/${my_username}/persistent/conda/jupyter_kernels ] ; then
 #cp  -r /home/idies/workspace/Storage/${my_username}/persistent/conda/jupyter_kernels/* ${HOME}/.local/share/jupyter/kernels/
 # or use link
 rm -rf ${HOME}/.local/share/jupyter/kernels/        # assume you have backup
 ln -s  /home/idies/workspace/Storage/${my_username}/persistent/conda/jupyter_kernels ${HOME}/.local/share/jupyter/kernels
fi
## some other .files/directories you may have made backup
# e.g. .mozilla
if [  ! -d /home/idies/workspace/Storage/${my_username}/persistent/init/.mozilla ]; then
 mkdir /home/idies/workspace/Storage/${my_username}/persistent/init/.mozilla
fi
if [ -d /home/idies/.mozilla ] ; then
 rm -rf /home/idies/.mozilla
fi
ln -s /home/idies/workspace/Storage/${my_username}/persistent/init/.mozilla /home/idies/.mozilla


#if your app creates any .* file or directory under ${HOME}
#  you could  backup and link to persistent same way if do need preserver changes
# e.g  ~/.nv , ~/.ipython , ~/.ipynb_checkpoints , ~/.conda  ~/.jupyter .....
```



Then to create conda virtualenv  for example with python3.10
```bash
conda create -n my_testenv  python=3.10
#activate env
source activate my_testenv
```
Install packages

```bash
#install packages use conda 
conda install numpy
#install package use pip
pip install torch torchvision torchaudio

```



