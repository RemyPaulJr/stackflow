### StackFlow
Personal Finance Platform

### What It Does
StackFlow is a personal finance application used to track my personal finances. It uses object-oriented programming and object-relational mapping to add finance data to a Postgres Database hosted on a docker container locally.

### Data Sources
My primary data source is done by the scripts/seed_database.py script where I used **Gen AI** to generate random fictional data using the python faker and random library.

The script uses my create/add methods I created on the table classes themselves.

Another Data Source is the CoinGecko Free API. This API is used to grab the live prices of crypto and perform aggregations.

### Data Ingestion
The data is ingested through my create/add methods as I mentioned. I can at any point create a script to add data to my database in Postgres. This is all manual at the moment as there is no automated way to add data.

### Data Modeling
> ERD Diagram can be viewed in the docs [here](docs/erd.png).

### Data Flow
> Architecture diagram with a basic overview of the data flow can be found in the docs [here](docs/architecture.png).

### Tech Stack
- **Backend**: Python
- **Frontend**: Streamlit
- **Database**: Postgres
- **Containerization**: Docker
- **Version Control**: Github/Git

### Run Application Locally
1. Clone Github repository.
```bash
git clone "https://github.com/RemyPaulJr/stackflow.git"
```
2. Create python virtual environment and initialize it.
> Mac and Linux only. Windows Powershell will require different set of commands.
```bash
python3 -m venv .venv
```
```bash
source .venv/bin/activate
```
3. Install python dependencies.
```bash
python install -r requirements.txt
```
4. Start docker container.
> Docker desktop needs to be installed.
```bash
docker compose up
```
5. Start streamlit application for frontend.
```bash
python -m streamlit run /ui/app.py
```
### Video Walkthrough
[![Video Walkthrough](https://img.youtube.com/vi/Zgqh7NTTI3Q/0.jpg)](https://www.youtube.com/watch?v=Zgqh7NTTI3Q)
