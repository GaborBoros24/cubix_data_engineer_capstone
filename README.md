Cubix Data Engineer Capstone

This project implements an end-to-end data processing pipeline on the Databricks platform, following the principles of the Medallion architecture. The goal is to build a reliable, scalable, and automated data system that supports decision-making and business intelligence.


📌 Project Objective

The purpose of this project is to create a data pipeline that:

- Collects data from various sources

- Applies the Medallion architecture (Bronze, Silver, Gold) for data refinement

- Handles slowly changing dimensions (SCD2)

- Integrates seamlessly with the Databricks environment for scalability and performance


🛠️ Technologies Used

Programming Languages & Libraries:

- Python

- PySpark

- Delta Lake

Platforms & Tools:

- Azure Data Lake Storage (ADLS)

- Databricks

- Poetry (dependency & packaging)

- pre-commit (code quality checks)


🧠 Applied Concepts

Medallion Architecture – Multi-layer architecture for organizing and refining data:

- Bronze: raw data

- Silver: cleaned and enriched data

- Gold: business-ready, aggregated data

- SCD2 (Slowly Changing Dimensions – Type 2) – Tracks historical changes in dimensional tables


🚀 Running the Project on Databricks

1. Set up your environment:

    - Create a Databricks cluster with appropriate Spark configuration

    - Ensure access to Azure Data Lake Storage (via credentials or mount)

2. Import the code:

    - Clone the repository into your Databricks workspace

    - Import src/cubix_data_engineer_capstone as notebooks or modules

3. Execute the pipeline:

    - Run the data processing steps in sequence:

      - Bronze → Silver → Gold

    - Use the SCD2 logic for managing dimension changes
  
📁 Project Structure

cubix_data_engineer_capstone/
- .github/workflows/        # CI/CD workflows
-  src/

   └── cubix_data_engineer_capstone/  # Core application code
- tests/                    # Unit tests
- .gitignore
- .pre-commit-config.yaml   # pre-commit config
- pyproject.toml            # Poetry config
- poetry.lock               # Dependency lock file
-  README.md

📦 Installing Dependencies

This project uses Poetry for dependency management.

1. Install Poetry:
    - curl -sSL https://install.python-poetry.org | python3 -

2. Install dependencies:
    - poetry install


✅ Running Tests

Tests are located in the tests/ directory. To run them:

  - poetry run pytest

🧹 Code Quality with pre-commit Hooks

This project uses pre-commit for ensuring code quality.

1. Install hooks:

    - poetry run pre-commit install

2. Run hooks manually:
   
    - poetry run pre-commit run --all-files
