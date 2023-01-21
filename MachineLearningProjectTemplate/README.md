# Project Title

This is a template for a machine learning project that includes a structure for organizing the code, data, and report files.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- Jupyter Notebook
- pandas, numpy, scikit-learn, matplotlib, seaborn
- nbconvert (to convert the jupyter notebook to pdf)

### Installing

1. Clone the repository
`git clone https://github.com/username/project-name.git`

2. Install the required packages
`pip install -r requirements.txt`

3. Run the jupyter notebook
`jupyter notebook`

4. Run the main function in the main.py file
`python main.py`

## File Structure

```
project-name/
|
|__ data/
|   |__ raw_data.csv
|   |__ processed_data.csv
|
|__ features/
|   |__ feature_engineering.py
|   |__ features.csv
|
|__ models/
|   |__ model1.py
|   |__ model2.py
|
|__ reports/
|   |__ figure1.png
|   |__ figure2.png
|   |__ report.pdf
|
|__ src/
|   |__ __init__.py
|   |__ data.py
|   |__ model.py
|   |__ train.py
|   |__ utils.py
|
|__ EDA.ipynb
|__ model_selection.ipynb
|__ main.py
|__ README.md
|__ requirements.txt

```


## Authors

* **Your Name** - *Initial work* - [Your Github](https://github.com/username)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

## How to generate the report
- Run the jupyter notebook
`jupyter notebook`

- Run the cells of EDA.ipynb and model_selection.ipynb
- Run the following command in the command line
```
!jupyter nbconvert --to pdf --output-dir=reports EDA.ipynb
!jupyter nbconvert --to pdf --output-dir=reports model_selection.ipynb
```

This command will convert the EDA.ipynb and model_selection.ipynb to pdf format, which will be saved in the reports folder.
