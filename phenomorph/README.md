# phenomorph

Phenomorph represents the integration of [phenopype](https://www.phenopype.org/) and [ml-morph](https://github.com/agporto/ml-morph)

When using phenomorph, please cite:


Porto, A. and Voje, K.L., 2020. ML‐morph: A fast, accurate and general approach for automated detection and landmarking of biological structures in images. Methods in Ecology and Evolution, 11(4), pp.500-512. ['link'](https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/2041-210X.13373)

Lürig, M. D. (2021). phenopype : A phenotyping pipeline for Python. Methods in Ecology and Evolution. ['link'] (https://doi.org/10.1111/2041-210x.13771)

## Usage
**ml-morph** performs automated landmarking in images of semi-rigid biological structures. To generate landmark predictions, we need to train machine learning models using manually annotated datasets. These manually annotated datasets can be generated and administered using the [`phenopype`](https://www.phenopype.org/) package, so this module should be seen as a contrib package that adds ml-morph functionality to the main package.