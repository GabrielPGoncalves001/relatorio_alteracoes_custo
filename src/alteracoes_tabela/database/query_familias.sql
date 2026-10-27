SELECT
    f.seqfamilia,
    LISTAGG(DISTINCT p.seqproduto, ',')
        WITHIN GROUP (ORDER BY p.seqproduto) AS SEQPRODUTOS,
    f.familia,
    nivel_1.n1 AS N1,
    nivel_2.n2 AS N2,
    C.COMPRADOR

FROM consinco.map_produto p

JOIN consinco.map_familia f
    ON f.seqfamilia = p.seqfamilia

JOIN consinco.map_famembalagem mm
    ON mm.seqfamilia = f.seqfamilia
    AND mm.qtdembalagem = 1

JOIN consinco.map_famdivisao A
    ON A.seqfamilia = p.seqfamilia

JOIN consinco.max_comprador C
    ON C.seqcomprador = A.seqcomprador

JOIN consinco.map_famfornec D
    ON D.seqfamilia = A.seqfamilia
    AND D.principal = 'S'

JOIN consinco.ge_pessoa E
    ON E.seqpessoa = D.seqfornecedor

JOIN consinco.maf_fornecdivisao forn
    ON forn.seqfornecedor = E.seqpessoa
    AND forn.nrodivisao = A.nrodivisao

JOIN (
    SELECT DISTINCT
        cc.seqcategoria AS idn1,
        cc.categoria AS n1,
        ff.nrodivisao AS divisao,
        ff.seqfamilia
    FROM consinco.map_categoria cc

    JOIN consinco.map_famdivcateg ff
        ON ff.seqcategoria = cc.seqcategoria
        AND ff.nrodivisao = cc.nrodivisao

    WHERE cc.statuscategor = 'A'
      AND ff.status = 'A'
      AND cc.tipcategoria = 'M'
      AND cc.categoria IN (
          'PERECIVEIS',
          'MERCEARIA LIQUIDA',
          'NAO ALIMENTOS',
          'MERCEARIA SECA'
      )
      AND cc.nivelhierarquia = 1
) nivel_1
    ON nivel_1.seqfamilia = f.seqfamilia
    AND nivel_1.divisao = A.nrodivisao

JOIN (
    SELECT DISTINCT
        cc.seqcategoria AS idn2,
        cc.categoria AS n2,
        ff.nrodivisao AS divisao,
        ff.seqfamilia
    FROM consinco.map_categoria cc

    JOIN consinco.map_famdivcateg ff
        ON ff.seqcategoria = cc.seqcategoria
        AND ff.nrodivisao = cc.nrodivisao

    WHERE cc.statuscategor = 'A'
      AND ff.status = 'A'
      AND cc.tipcategoria = 'M'
      AND cc.nivelhierarquia = 2
) nivel_2
    ON nivel_2.seqfamilia = f.seqfamilia
    AND nivel_2.divisao = nivel_1.divisao

WHERE f.seqfamilia IN ({placeholders})
    AND nivel_1.n1 in ('MERCEARIA SECA','MERCEARIA LIQUIDA',
                       'NAO ALIMENTOS','PERECIVEIS')
GROUP BY
    f.seqfamilia,
    f.familia,
    nivel_1.n1,
    nivel_2.n2,
    C.COMPRADOR,
    E.NOMERAZAO

ORDER BY f.seqfamilia