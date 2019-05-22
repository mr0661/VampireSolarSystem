###################################################
# Simple Makefile for LaTeX-Documents             #
#                                                 #
# Erno Salminen, Decemeber 2012                   #
###################################################


#############################
##### Variables #############

# Basename for the document (without postfix '.tex')
TARGET=mainDocument

#############################
##### Targets ###############
# Not all people use bibtex
all: ${TARGET}.tex
	pdflatex ${TARGET}.tex
	pdflatex ${TARGET}.tex
	pdflatex ${TARGET}.tex

# Clean. Remove generated files (aux=cross-references, dvi=device
# independent (kind of pdf clone), log=messages and errors, toc=table
# of contents, lof=list of figures...)
clean:
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
