#!/bin/bash

pdflatex eq_cycle_slip_rates.tex
bibtex eq_cycle_slip_rates
pdflatex eq_cycle_slip_rates.tex
pdflatex eq_cycle_slip_rates.tex

rm -f *.aux *.bbl *.log *.blg *.pagelist
