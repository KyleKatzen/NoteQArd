NoteQArd
==============================

# Creates notecards from informative text

## How to turn text into Questions and Answers:

```{python}

from noteqard import noteqard
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

george_washington_text = """
George Washington (February 22, 1732 – December 14, 1799) was an American military officer, statesman, and Founding Father who served as the first president of the United States from 1789 to 1797. Appointed by the Second Continental Congress as commander of the Continental Army in June 1775, Washington led Patriot forces to victory in the American Revolutionary War and then served as president of the Constitutional Convention of 1787, which created and ratified the Constitution of the United States and the American federal government. Washington has been called the "Father of his Country" for his manifold leadership in the nation's founding.
"""

qas = noteqard.text_to_question_answer(george_washington_text)

print(qas)
```

```
[{'Q': "Q: What are the dates of George Washington's life?",
  'A': 'A: February 22, 1732 – December 14, 1799.'},
 {'Q': "Q: What were George Washington's roles in American history?",
  'A': 'A: George Washington was an American military officer, statesman, and Founding Father. He served as the first president of the United States, led the Continental Army during the American Revolutionary War, and was president of the Constitutional Convention.'},
 {'Q': 'Q: When did George Washington serve as the president of the United States?',
  'A': 'A: George Washington served as the first president of the United States from 1789 to 1797.'},
 {'Q': 'Q: What is George Washington known as?',
  'A': 'A: George Washington is known as the "Father of his Country" for his leadership in the nation\'s founding.'},
 {'Q': 'Q: What significant role did George Washington play in the American Revolutionary War?',
  'A': 'A: George Washington led the Patriot forces to victory during the American Revolutionary War as the commander of the Continental Army.'},
 {'Q': 'Q: What did George Washington do at the Constitutional Convention of 1787?',
  'A': 'A: George Washington served as the president of the Constitutional Convention of 1787, which created and ratified the Constitution of the United States and established the American federal government.'}]
```

## How to turn Questions and Answers into Anki Flashcards

```{python}
noteqard.export_qa_to_tsv("question_answer.tsv", qas)
```

Then go to anki, click import file, and select the file you exported.



Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── setup.cfg          <- makes project pip installable (pip install -e .) so src can be imported
    ├── pyproject.toml     <- makes project pip installable (pip install -e .) so src can be imported
    ├── src/noteqard                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
