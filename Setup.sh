if [[ "$EUID" != "0" ]]; then
	echo -e "\e[00;31mERROR: DEBES SER ROOT\e[00m"
	exit 1
fi

apt-get install python-xlib
