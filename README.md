# Hepatitis B Genome Codon Analysis

This small Python project reads the FASTA file `sequence.fasta`, counts codons
in the sequence, displays a chart of the ten most frequent codons, and prints
their counts.

The included FASTA header identifies the sequence as Hepatitis B virus (HBV),
strain ayw, accession `NC_003977.2`.

## Requirements

- Python 3.11 or a compatible Python 3 version
- Matplotlib

Install Matplotlib using the Python interpreter you intend to use to run the
script:

```powershell
py -3.11 -m pip install matplotlib
```

If `py` is unavailable, use the full path to your Python executable:

```powershell
& "C:\Users\diana\AppData\Local\Programs\Python\Python311\python.exe" -m pip install matplotlib
```

## Run

Open a terminal in this project folder (the folder containing `ex0.py` and
`sequence.fasta`) and run:

```powershell
py -3.11 .\ex0.py
```

The script opens a plot window. Close it to return to the terminal and see the
printed top ten codons and their frequencies. In VS Code, select the same
Python 3.11 interpreter and use **Run Python File**.

## What the analysis does

The script removes FASTA header lines, joins the remaining sequence lines,
converts the sequence to uppercase, and replaces `U` with `T`. It then counts
all complete triplets at offsets 0, 1, and 2, combines those counts, and plots
the ten most frequent triplets. Each triplet is labeled with its amino-acid
letter according to the standard genetic code.

## Scope and limitations

This is a simple descriptive sequence-counting exercise, not a clinical or
complete viral-genome analysis.Because it combines
triplets from all three forward offsets, reported frequencies are not counts
of codons in a specific HBV protein. It also does not scan the reverse
complement or handle the circular-genome boundary. The chart alone cannot
establish viral activity, disease severity, treatment response, or which foods
a person with hepatitis B should eat.

## Diet and hepatitis B

A viral genome's codon frequencies do not provide a basis for recommending a
diet or identifying foods that treat hepatitis B. The foods below are
examples that generally contain relatively little protein per serving; they
are not an HBV treatment or a medically prescribed diet.

## Short list of foods relatively low in the six amino acids

- **Vegetables:** cucumber, lettuce, zucchini, celery.
- **Fruits:** apples, pears, watermelon, grapes.
- **Starchy foods:** white rice, potatoes, tapioca.
- **Other foods:** olives, avocado.

These foods generally contain relatively little protein per serving, so they
tend to provide lower total amounts of proline, phenylalanine, serine,
leucine, tryptophan, and glutamine than protein-rich foods.

**Important:** No food is completely free of these amino acids. Leucine,
phenylalanine, and tryptophan are essential for human health; do not severely
restrict them without professional supervision. Lowering dietary intake of
these amino acids is not an established treatment for viral infections.

For hepatitis B, discuss diet and supplements with a qualified healthcare
professional, especially if you have liver disease or are taking medication.
This project and its output are educational and are not medical advice.
