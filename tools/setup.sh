#!/bin/bash

### SETUP HERE
ENV_NAME="venv"
PY_PACKAGES_PATH="requirements.txt"
### END SETUP
THIS_PATH=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)

echo -e "\e[7m  Installing pip   \e[27m"
easy_install pip

echo -e "\e[7m  Installing virtualenv   \e[27m"
pip install --upgrade virtualenv==13.1.2

echo -e "\e[7m  Setting up virtual environment   \e[27m"
virtualenv ${THIS_PATH}/${ENV_NAME}
source ${ENV_NAME}/bin/activate

echo -e "\e[7m  Setting up Python modules in virtualenv   \e[27m"

if [ `uname -o` == "Cygwin" ]
then
  THIS_PATH=$(cygpath -d ${THIS_PATH})
fi

pip install --upgrade -r "${THIS_PATH}/${PY_PACKAGES_PATH}"

echo -e "\n  ======================================================================"
echo -e "  || \e[1mDone!\e[0m                                                            ||"
echo -e "  || \e[34mDon't forget to activate your virtual environment when running\e[39m   ||"
echo -e "  || \e[7m $ source ${ENV_NAME}/bin/activate \e[27m                                     ||"
echo -e "  ======================================================================\n\n"
