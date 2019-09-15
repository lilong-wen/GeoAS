set -e # bash should exit the script if any statement returns a non-true 
       #return value

pngfile="$(echo $1|sed 's/\..\{3\}$/.png/')"
epsfile="$1"


gs -dSAFER \
   -dBATCH \
   -dNOPAUSE \
   -dEPSCrop \
   -dEPSFitPage \
   -sDEVICE=png16m \
   -r150 \
   -g1000x1000 \
   -sOutputFile="$pngfile" "$epsfile"

#convert "$pngfile" -trim +repage "$pngfile"

convert "$pngfile" -resize 500 "$pngfile"
