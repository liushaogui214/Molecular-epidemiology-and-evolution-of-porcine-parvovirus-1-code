# Molecular epidemiology and evolution of porcine parvovirus 1

This repository contains source code, input files, and selected analysis outputs associated with the manuscript **"Molecular epidemiology and evolution of porcine parvovirus 1"**.

## Repository contents

- `scripts/run_treetime_batch.py`: Python script used to run the TreeTime analysis.
- `data/treetime/`: input files for TreeTime, including the VP2 sequence alignment, sampling-date metadata, and Newick tree.
- `results/treetime/`: TreeTime output files used for downstream interpretation and figures.
- `results/beast/`: summarized BEAST Bayesian SkyGrid results.
- `results/supplementary/`: supplementary result tables.

Third-party software installers are not included in this repository. TreeTime and BEAST should be obtained from their official sources.

## Requirements

- Python 3.8 or later
- TreeTime

Install TreeTime with pip:

```bash
pip install -r requirements.txt
```

## Reproducing the TreeTime analysis

From the repository root, run:

```bash
python scripts/run_treetime_batch.py
```

The script reads files from `data/treetime/` and writes TreeTime outputs to `results/treetime/`.

## Third-party software

TreeTime was used for time-scaled phylogenetic analysis:

- Documentation: https://treetime.readthedocs.io/
- Source code: https://github.com/neherlab/treetime
- License: MIT License

BEAST was used for Bayesian evolutionary analysis:

- Website: https://beast-dev.github.io/beast-mcmc/
- Source code: https://github.com/beast-dev/beast-mcmc
- License: GNU Lesser General Public License

## License

This repository is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0). See the LICENSE file for details.

