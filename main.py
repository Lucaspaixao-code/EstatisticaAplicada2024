from fastapi import FastAPI, HTTPException
from Model.FinanciamentoInput import FinanciamentoInput
from Class.Veiculo import Veiculo
from Class.Imovel import Imovel

# Definindo a classe da aplicação FastAPI
app = FastAPI()

# Rota para calcular o valor financiado
@app.post("/Veiculo/calcular_valor_financiado/")
async def calcular_valor_financiado(FinanciamentoInput: FinanciamentoInput):
    try:
        veiculo = Veiculo(**FinanciamentoInput.dict())
        valor_financiado = veiculo.qtde_parcela*veiculo.calcular_valor_parcela()
        return HTTPException(status_code=200, detail=valor_financiado)
    except:
         raise HTTPException(status_code=404, detail="Erro ao calcular valor do financimento")

# Rota para calcular o valor financiado do Imovel
@app.post("/Imovel/calcular_valor_financiado/")
async def calcular_valor_financiado(FinanciamentoInput: FinanciamentoInput):
    try:
        veiculo = Imovel(**FinanciamentoInput.dict())
        valor_financiado = veiculo.qtde_parcela*veiculo.calcular_valor_parcela()
        return HTTPException(status_code=200, detail=valor_financiado)
    except:
         raise HTTPException(status_code=404, detail="Erro ao calcular valor do financimento")
