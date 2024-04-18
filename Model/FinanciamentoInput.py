from pydantic import BaseModel

# Definindo a classe do modelo para entrada de dados
class FinanciamentoInput(BaseModel):
    valor: float
    valor_entrada: float = 0
    qtde_parcela: int
    taxa_juros: float