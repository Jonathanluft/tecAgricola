# Registro de Colheita 

Aplicação Python que registra colheitas de hortaliças em JSON e também
insere os dados em um banco Oracle, cumprindo os requisitos da disciplina
(estruturas de dados, arquivos, subalgoritmos e banco).

## Como executar

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install cx_Oracle
python app.py              # edite as credenciais Oracle no topo de app.py
