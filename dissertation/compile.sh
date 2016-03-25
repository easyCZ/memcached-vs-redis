pdflatex dissertation.tex -halt-on-error -no-file-line-error
bibtex dissertation.aux
pdflatex dissertation.tex -halt-on-error -no-file-line-error
pdflatex dissertation.tex -halt-on-error -no-file-line-error

rm dissertation.aux dissertation.bbl disseratation.blg dissertation.log dissertation.toc