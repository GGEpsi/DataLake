# DataLake / Spark 

## Architecture

<br>**`.venv/`
<br>`config/`
<br>`data/`
    <br><br>`raw/`
    <br><br>`staging/` 
    <br><br>`curated/` 
<br>`jobs/`
<br>`notebooks/`
<br>`src/` 
<br>`pyproject.toml`
<br>`uv.lock`

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
