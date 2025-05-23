# precision-mapping

Python package for precision functional mapping of the hippocampus

- Assigns vertices in the hippocapmus to systems based on the spatial similarity of their neocortical connectivity profile to a set of templates (default: [3-cluster solution from Kember et al. (2025)]()).


## Installation
```bash
pip install hipp-mapping
```

## Useage
```bash
hipp_mapping [-h] --func --surf --output [--dilation_threshold]

options:
  -h, --help            show help message and exit
  --func FUNC           Path to GIFTI (.func.gii) BOLD time-series file. TRs stored as individual darrays.
  --surf SURF           Path to GIFTI (.surf.gii) mid-thickness surface file.
  --output OUTPUT       Directory to store output results.
  --dilation_threshold DILATION_THRESHOLD
```
*requires [Connectome Workbench](https://www.humanconnectome.org/software/get-connectome-workbench) to be installed.

