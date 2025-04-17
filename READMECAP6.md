# Registro de Colheita com alerta de estoque mínimo

Script em Python para controlar:

* **Entrada** de produtos (colheita)
* **Saída** de produtos (venda ou retirada)
* Saldo atualizado por tipo
* Alerta automático quando o estoque fica abaixo do mínimo definido

Os dados ficam salvos num arquivo **colheitas.json**.  
Se quiser, o mesmo registro é gravado em um banco Oracle (basta preencher usuário, senha e endereço no topo do `app.py`).

## Como rodar

```bash
# (opcional) criar ambiente virtual
python -m venv .venv
# Windows:  .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

# instalar driver Oracle só se for usar banco
pip install cx_Oracle

python app.py

