# SWAROG dataset

> Following repository contains dataset acquired and labeled during the first phase of a SWAROG project, financed by the National Center for Research and Development, under grant INFOSTRATEG-I/0019/2021.

## How to use me?

The usage is quite simple. To access the dataset you only need to get a `gdown` package, available on PyPI repository and to run a `gather.sh` script from this repository. The data is stored in **HDF5** format, according to its `pandas` serialization procedure, so for easiest processing it is also suggested to install `pandas` and `pytables` packages, as indicated in `requirements.txt` file. 

```bash
pip install -r requirements.txt
./gather.sh
```

Dataset will be unpacked to the `data` directory, as two `.h5` files:

- `labeled_data_embed.h5` – containing the labeled subset of acquired data with established embedding.
- `nolabel_data_embed.h5` – containing all the acquired data with the same approach for feature extraction.

To encourage users to use a proper experimental protocol, data is made available **without imposed division to cross-validation folds**. If all the packages from `requirements.txt` file are properly installed, all what is needed to load data into the experimental script is to read the files with **pandas** `read_hdf()` function with its defalult parameters, as in the `example.py` file:

```python
import pandas as pd

# Load and show labeled data
labeled_data = pd.read_hdf('data/labeled_data_embed.h5')

print(labeled_data)

# Load nolabel data
nolabel_data = pd.read_hdf('data/nolabel_data_embed.h5')

print(nolabel_data)
```

## Data structure

The dataframes of `SWAROG-dataset` are organized with tle following manner:

|Key|Description|dtype|
|---|---|---|
|`url`| Absolute URL address to the analyzed article. | `object` |
|`title`| Title of the article according to `<title>` tag at the moment of acquisition. | `object` |
|`download_timestamp`| Epoch time of the moment of acquisition. | `object` |
|`publication_timestamp`| Identified epoch time of the moment of article publication. | `object` |
|`Poll_id`| Identifier of a labeling poll. **[only for labeled data]** | `int64` |
|`P{5:17}`| 12 consecutive fields of binary labeling structure. **[only for labeled data]** | `int64` |
|`E{0:383}`| 384 consecutive fields of established embedding for article's body for the moment of acquisition. | `float32` |

## Citation policy

If you will use this dataset in your research, please use the following citation

```
Kozik, Rafał, et al. "SWAROG Project Approach to Fake News Detection Problem." Computational Intelligence in Security for Information Systems Conference. Cham: Springer Nature Switzerland, 2023.
```
