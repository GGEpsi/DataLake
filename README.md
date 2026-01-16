# DataLake / Spark 

## Architecture

* **`.venv/`**
* **`config/`**
* **`data/`**
    * `raw/`
    * `staging/`
    * `curated/`
* **`jobs/`**
* **`notebooks/`**
* **`src/`**
* **`pyproject.toml`**
* **`uv.lock`**

##  Guide de Démarrage Rapide

1.  **Synchronisation de l'environnement** :
    ```bash
    uv sync
    ```

2.  **Exécution du pipeline principal** :
    ```bash
    uv run python main.py
    ```

3.  **Lancement des notebooks** :
    ```bash
    uv run jupyter lab
    ```
