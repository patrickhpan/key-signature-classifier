PDF_IN=$1;
OUT_DIR=$2;
if [ ! -f "$PDF_IN" ]; then
	echo "File $PDF_IN not found.";
	exit 1;
fi;
if [ -z "$OUT_DIR" ]; then
	OUT_DIR="$PDF_IN"'-out';
fi;
if [ -d "$OUT_DIR" ]; then
	echo "Directory $OUT_DIR already exists."
	exit 2;
fi;
mkdir $OUT_DIR;

DENSITY=$3;
if [ -z "$DENSITY" ]; then
	DENSITY=600;
fi;

LOGPAGES=$4;
if [ -z "$LOGPAGES" ]; then
	LOGPAGES=4;
fi;

echo convert -density $DENSITY "$PDF_IN" "$OUT_DIR""/%0$LOGPAGES""d.jpg";
convert -monitor -density $DENSITY "$PDF_IN" "$OUT_DIR""/%0$LOGPAGES""d.jpg";
