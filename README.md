## surui 

## Table of contents
* [Install](#Install)
	* [Install using `pip`](#Install)
	* [package](#Package)
* [Usage](#Usage)
	* [Example](#Example)
	* [Real data](#Example) 
## Install
### Install using `pip`

Firstly, we suggest to build a new virtual environment through `Anaconda`:
```
conda create -n    python=3.6
```
Create and activate the virtual environment environment `    `:
```
conda activate  
```
### Package
| package | version |
| :----: | :----: |
| keras  | 2.2.4 |
| tensorFlow | 1.14.0 |
| scikit-learn | 0.24.1 |
| genism | 3.8.3 |
## Usage
All functions of FEGFS can be found in the script folder `FEGFS.py` is running:
```
python ./script/FEGFS.py -d <data_name> -c <num_clusters> -n <retention_ratio> -i <GO_Term_path> -e　<expression_matrix_path> -o <outputpath> -l <label_path>
```
### Example
Run `FEGFS` as an example in script:
```
python ./script/FEGFS.py -d test -c 5 -n 0.4 -i ./example/GO_Term.xlsx -e ./example/test_count_matrix.csv -o ./example/Term_matrix -l ./example/test_label.csv
```
### Real data
Here we take `Pollen` as an example:
```
