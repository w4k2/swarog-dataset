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

# Load labeled data
labeled_data = pd.read_hdf('data/labeled_data_embed.h5')

# Load nolabel data
nolabel_data = pd.read_hdf('data/nolabel_data_embed.h5')
```

## Data structure

The dataframes of `SWAROG-dataset` are organized with the following manner:

|Key|Description|dtype|
|---|---|---|
|`url`| SHA-1 sum of URL address to the analyzed article. | `object` |
|`download_timestamp`| Epoch time of the moment of acquisition. | `object` |
|`publication_timestamp`| Identified epoch time of the moment of article publication. | `object` |
|`Poll_id`| Identifier of a labeling poll. **[only for labeled data]** | `int64` |
|`P{5:17}`| 12 consecutive fields of binary labeling structure. **[only for labeled data]** | `int64` |
|`T{0:383}`| 384 consecutive fields of established embedding for article's titles for the moment of acquisition. | `float32` |
|`E{0:383}`| 384 consecutive fields of established embedding for article's body for the moment of acquisition. | `float32` |

## Labels description

SWAROG's approach for annotation differs from standard labeling protocol, explicitly assigning each data object into one of the *fake news* categories, proposing extended definition build around 13 questions connected with this phenomenon.

| Key | Question |
|---|---|
| P5 | Is there at least one reliable source that confirms all the information contained in the content? |
| P6 | Is most of the information provided confirmed by reliable sources? |
| P7 | Is none of the information confirmed by reliable sources? |
| P8 | Does the statement refer to current (at the time of creation of the statement) data? |
| P9 | Is additional information required to correctly understand the content? |
| P10 | Does the statement contain any inaccuracies? |
| P11 | Does the statement contain fragments taken out of context? |
| P12 | Does the author of the statement use cherry picking? |
| P13 | Is the author of the statement trying to mislead the reader? |
| P14 | Is the content satirical? |
| P15 | Does the author admit that the facts presented are made up? |
| P16 | Does the statement contain political promises? |
| P17 | Does the statement contain religious content? |

## Citation policy

If you will use this dataset in your research, please use the following citation

```
@inproceedings{kozik2023swarog,
  title={SWAROG Project Approach to Fake News Detection Problem},
  author={Kozik, Rafa{\l} and Komorniczak, Joanna and Ksieniewicz, Pawe{\l} and Pawlicka, Aleksandra and Pawlicki, Marek and Chora{\'s}, Micha{\l}},
  booktitle={Computational Intelligence in Security for Information Systems Conference},
  pages={79--88},
  year={2023},
  organization={Springer}
}
```
