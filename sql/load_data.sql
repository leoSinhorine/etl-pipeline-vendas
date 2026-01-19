COPY vendas (data_venda, produto, quantidade, preco, total)
FROM 'CAMINHO_DO_CSV'
DELIMITER ','
CSV HEADER;
