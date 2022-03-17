# ml-morph [![DOI](https://zenodo.org/badge/195575274.svg)](https://zenodo.org/badge/latestdoi/195575274)

Machine-learning tools for landmark-based morphometrics


Porto, A. and Voje, K.L., 2020. ML‐morph: A fast, accurate and general approach for automated detection and landmarking of biological structures in images. Methods in Ecology and Evolution, 11(4), pp.500-512. ['link'](https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/2041-210X.13373)

## Usage
**ml-morph** performs automated landmarking in images of semi-rigid biological structures. To generate landmark predictions, we need to train machine learning models using manually annotated datasets. These manually annotated datasets can be generated and administered using the [`phenopype`](https://www.phenopype.org/) package, so this module should be seen as a contrib package that adds mlmorph functionality to the main package.