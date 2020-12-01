INPUT1=mainDocument
INPUT2=character_sheet
INPUT3=fluff

RUN()
{
	COMMAND=$1
	TARGET=$2
	EXTRA_COMMENT=$3
	eval timeout 5s $COMMAND $TARGET > log.txt
	if [ $? -eq 0 ]; then
		echo "Success $TARGET $EXTRA_COMMENT" 
		rm log.txt
	else
		echo "Fail on $TARGET $EXTRA_COMMENT"
		exit $?
	fi
}

LATEX()
{
	TARGET=$1.tex
	RUN pdflatex $TARGET 1st
	RUN pdflatex $TARGET 2nd
}

RUN python3 code/create_abilities.py
RUN python3 code/create_keys.py
RUN python3 code/create_secrets.py

LATEX $INPUT1
LATEX $INPUT2
LATEX $INPUT3

rm -f *aux
rm -f *dvi
rm -f *log
rm -f *toc
rm -f *lof
rm -f *lot
rm -f *lol
rm -f *bbl
rm -f *blg
rm -f *out
