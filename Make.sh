TARGET=mainDocument
TARGET2=character_sheet
TARGET_TEX=$TARGET.tex
TARGET2_TEX=$TARGET2.tex

python3 code/create_abilities.py
if [ $? -eq 0 ]; then
    echo "Success (create_abilities.py)" 
else
	echo "Fail on create_abilities.py"
    exit $?
fi

python3 code/create_keys.py
if [ $? -eq 0 ]; then
    echo "Success (create_keys.py)" 
else
	echo "Fail on create_keys.py"
    exit $?
fi

python3 code/create_secrets.py
if [ $? -eq 0 ]; then
    echo "Success (create_secrets.py)"
else
	echo "Fail on create_secrets.py"
    exit $?
fi

pdflatex $TARGET_TEX
if [ $? -eq 0 ]; then
    echo "Success 1st pdflatex"
else
	echo "Fail on 1st pdflatex"
    exit $?
fi

pdflatex $TARGET_TEX
if [ $? -eq 0 ]; then
    echo "Success 2nd pdflatex"
else
	echo "Fail on 2nd pdflatex"
    exit $?
fi

pdflatex $TARGET_TEX
if [ $? -eq 0 ]; then
    echo "Success 3rd pdflatex"
else
	echo "Fail on 3rd pdflatex"
    exit $?
fi

pdflatex $TARGET2_TEX
if [ $? -eq 0 ]; then
    echo "Success 1st pdflatex character sheet"
else
	echo "Fail on 1st pdflatex character sheet"
    exit $?
fi

pdflatex $TARGET2_TEX
if [ $? -eq 0 ]; then
    echo "Success 2nd pdflatex character sheet"
else
	echo "Fail on 2nd pdflatex character sheet"
    exit $?
fi

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
