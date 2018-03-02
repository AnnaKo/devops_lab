 #!/usr/bin/python
 
 #installing dependencies
 yum install -y  gcc gcc-c++ make git patch openssl-devel zlib-devel readline-devel sqlite-devel bzip2-devel
 echo "dependencies are installed"
 
 #cloning git repository with pyenv
 curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
 echo "pyenv repository cloned"
 
 #modify PATH 
 export PATH="$HOME/.pyenv/bin:$PATH"
 eval "$(pyenv init -)"
 eval "$(pyenv virtualenv-init -)"
 echo "PATH exported"
 
 #installing pyenvs for v2 and v3
 pyenv install 2.7.6
 pyenv install 3.5.5
 echo "both pyenvs installed"
 
 #setting local pyenv as 2.7.6
 pyenv local 2.7.6 
 echo "pyenv is locally set for 2.7.6"
 
 #creating virtualenv for v2.7.6
 pyenv virtualenv akovirtualenv2
 echo "akovirtualenv2 created"
 
 #setting local pyenv as 3.5.5
 pyenv local 3.5.5
 echo "pyenv is locally set for 3.5.5"
 
 #creating virtualenv for v2.7.6
 pyenv virtualenv akovirtualenv3
 echo "akovirtualenv3 created"
 
 