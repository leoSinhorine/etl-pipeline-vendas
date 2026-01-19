CREATE TABLE vendas (
    id_venda SERIAL PRIMARY KEY,
    data_venda DATE,
    produto TEXT,
    quantidade INT,
    preco NUMERIC(10,2),
    total NUMERIC(10,2)
);

CREATE TABLE vendas_agrupadas_por_dia AS
SELECT
    data_venda,
    SUM(total) AS faturamento_total,
    SUM(quantidade) AS unidades_vendidas
FROM vendas
GROUP BY data_venda
ORDER BY data_venda;
