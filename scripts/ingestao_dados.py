import pandas as pd
from sqlalchemy import create_engine, text
import os

# 1. Configurações de Conexão
USUARIO = 'postgres'
SENHA = '2806' 
HOST = 'localhost'
PORTA = '5432'
BANCO = 'etl_vendas'

engine = create_engine(f'postgresql://{USUARIO}:{SENHA}@{HOST}:{PORTA}/{BANCO}')

# 2. Caminho do arquivo
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_csv = os.path.join(diretorio_atual, '..', 'data', 'vendas.csv')

try:
    # 3. Extração: Lendo o CSV
    print(f"Lendo dados de: {caminho_csv}")
    df = pd.read_csv(caminho_csv)

    # 4. Carga (Layer Raw): Enviando para a vendas_raw
    print("Enviando dados para a camada 'vendas_raw'...")
    df.to_sql('vendas_raw', engine, if_exists='replace', index=False)

    # 5. Transformação/Carga (Layer Trusted): SQL para atualizar a tabela final
    print("Atualizando tabela principal 'vendas' via SQL...")
    
    query_transferencia = """
    TRUNCATE TABLE vendas; 
    INSERT INTO vendas (id_venda, data_venda, produto, quantidade, preco)
    SELECT 
        ROW_NUMBER() OVER () as id_venda, 
        CAST(v.data_venda AS DATE), 
        v.produto, 
        v.quantidade, 
        CAST(v.preco AS NUMERIC)
    FROM vendas_raw v;
    """
    
    with engine.connect() as conexao:
        conexao.execute(text(query_transferencia))
        conexao.commit()

    print("✅ Sucesso! Pipeline completo: CSV -> vendas_raw -> vendas.")

except Exception as e:
    print(f"❌ Erro no pipeline: {e}")