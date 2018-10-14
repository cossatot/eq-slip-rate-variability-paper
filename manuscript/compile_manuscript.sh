#!/bin/bash

OUT_TYPE=$1

OUTFILE_NAME="eq_cycle_slip_rates."

if [ "$OUT_TYPE" == "pdf" ]; then
pandoc random_eq_slip_rate_variations.md --from markdown \
    -o $OUTFILE_NAME$OUT_TYPE \
    --template=copernicus.template \
    --latex-engine=pdflatex \
    --filter pandoc-citeproc --bibliography=eq-cycle-slip-rate-paper.bib \
    --csl=/Users/itchy/Zotero/styles/copernicus-publications.csl \
    --natbib \
    --metadata link-citations=true


elif [ "$OUT_TYPE" == "tex" ]; then
#pandoc random_eq_slip_rate_variations.md --from markdown \
pandoc eq-slip-rate.md --from markdown \
    -o $OUTFILE_NAME$OUT_TYPE \
    --template=copernicus.template \
#    --filter pandoc-citeproc --bibliography=eq-cycle-slip-rate-paper.bib \
#    --csl=/Users/itchy/Zotero/styles/copernicus-publications.csl

elif [ "$OUT_TYPE" == "agu_tex" ]; then
pandoc random_eq_slip_rate_variations.md --from markdown \
    -o ${OUTFILE_NAME%?}.tex \
    --template=agu_markdown.template \
    --filter pandoc-citeproc --bibliography=eq-cycle-slip-rate-paper.bib \
    --csl=/Users/itchy/Zotero/styles/american-geophysical-union.csl

elif [ "$OUT_TYPE" == "agu_pdf" ]; then
pandoc random_eq_slip_rate_variations.md --from markdown \
    -o ${OUTFILE_NAME%?}.pdf \
    --template=agu_markdown.template \
    --latex-engine=xelatex \
    --filter pandoc-citeproc --bibliography=eq-cycle-slip-rate-paper.bib \
    --csl=/Users/itchy/Zotero/styles/american-geophysical-union.csl


elif [ "$OUT_TYPE" == "docx" ]; then
pandoc random_eq_slip_rate_variations.md --from markdown \
    -o $OUTFILE_NAME$OUT_TYPE \
    --filter pandoc-citeproc --bibliography=eq-cycle-slip-rate-paper.bib \
    --csl=/Users/itchy/Zotero/styles/copernicus-publications.csl

elif [ "$OUT_TYPE" == "html" ]; then
pandoc random_eq_slip_rate_variations.md --from markdown \
    -o $OUTFILE_NAME$OUT_TYPE \
    --filter pandoc-citeproc --bibliography=eq-cycle-slip-rate-paper.bib \
    --csl=/Users/itchy/Zotero/styles/copernicus-publications.csl
fi
