# Project Name

## Data
- `data/`: Contains the raw and processed data used in the project. The `raw/` subdirectory contains the original data as it was downloaded, while the `processed/` subdirectory contains the data after any cleaning and preprocessing has been applied.

## Features
- `features/`: Contains the feature engineering code and any new features created.

## Models
- `models/`: Contains the code and files for each model trained and used in the project. Each model has its own subdirectory, containing the code and trained model files.

## Notebooks
- `notebooks/`: Contains Jupyter notebooks used for exploratory data analysis, model selection, and other tasks.

## Reports
- `reports/`: Contains any reports or visualizations generated during the project. The `figures/` subdirectory contains any images or figures used in the reports.

## Source Code
- `src/`: Contains the main code used in the project, including data loading and preprocessing, model training, and other utility functions.

## Additional files
- `.env`: File where the environment variables are stored
- `.gitignore`: Specifies files and directories that should be ignored by Git.
- `requirements.txt`: Lists all the Python packages that are required to run the code in the project.


```
project_name/
    data/
        raw/
            original_data.csv
        processed/
            processed_data.csv
    features/
        feature_engineering.py
        features.csv
    models/
        model1/
            model1.py
            model1.pkl
        model2/
            model2.py
            model2.pkl
    notebooks/
        EDA.ipynb
        model_selection.ipynb
    reports/
        figures/
            figure1.png
            figure2.png
        report.pdf
    src/
        __init__.py
        data.py
        model.py
        train.py
        utils.py
    .env
    .gitignore
    requirements.txt
```



