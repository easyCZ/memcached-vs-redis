pandoc *.md \
    -V geometry:margin=3cm \
    --number-sections \
    -o dissertation.pdf

# pandoc \
#     -s dissertation.tex \
#     -o dissertation.pdf \
#     -V geometry:margin=3cm
    # --number-sections