set -e
pngname="$(echo $1|sed 's/\..\{3\}$/.png/')"
eukname="$(echo $1|sed 's/\..\{3\}$/.eps/')"
epsfile="$1"
eukleides "$1"
eps2png.sh "$eukname"

