from pydantic import BaseModel

# Definindo a classe do modelo para entrada de dados
class FinanciamentoInput(BaseModel):
    valor: float
    valor_entrada: float
    qtde_parcela: int
    taxa_juros: float