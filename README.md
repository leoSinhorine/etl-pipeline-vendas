Pipeline ETL de Vendas
Projeto de Engenharia de Dados focado em automação de ponta a ponta: do CSV ao Dashboard.

🎯 Objetivo
Automatizar a ingestão e o tratamento de dados de vendas, utilizando uma estrutura de camadas para garantir dados limpos e prontos para análise.

🛠️ Tecnologias
Python (Pandas & SQLAlchemy) - Ingestão e automação.

PostgreSQL - Armazenamento e lógica de banco.

Power BI - Visualização e KPIs.

Batch Script - Execução com um clique.

🏗️ Arquitetura (Camadas)
Bronze (Raw): Dados brutos via Python (vendas_raw).

Silver (Trusted): Dados limpos e tipados via SQL (vendas).

Gold (Analytics): Dashboard conectado para tomada de decisão.

Destaque Técnico: Implementação de Generated Columns no SQL para cálculo automático de faturamento, centralizando a regra de negócio no banco de dados.

📂 Estrutura
Plaintext

 ├── dashboard/      # Power BI (.pbix)
 ├── data/           # CSVs Brutos
 ├── scripts/        # Python ETL
 ├── sql/            # Scripts do Banco
 └── executar_pipeline.bat # Execução rápida
 
🚀 Como usar
Configure sua senha no arquivo ingestao_dados.py.

Execute o arquivo executar_pipeline.bat.

Abra o Power BI e clique em Atualizar.