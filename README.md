# nomogram

Esse é um script em python muito simples que plota um nomograma dos protocolos de amostragem segunda a teoria de Pierre Gy. O script tem como dependências os pacotes numpy, pandas e matplotlib.

`pip install numpy pandas matplotlib`

Os protocolos são informados a partir de um arquivo `.csv` como o exemplo abaixo. Onde cada linha representa uma etapa do protocolo. É importante que o cabeçalho seja exatamente igual ao do exemplo:

* ml: massa do lote;
* ms: massa da amostra;
* dn: top size da amostra;
* c: constante de amostragem;

```
ml,ms,dn,c
5728,5728,5,37.24
5728,5728,0.6350,104.52
5728,1432,0.6350,104.52
1432,1432,0.2,186.24
1432,300,0.2,186.24
300,300,0.0160,266666.66
300,50,0.0160,266666.66
```

Para rodar o script basta o comando `python nomograma.py protocolo.csv`. Uma imagem será salva no mesmo diretório do arquivo `nomograma.py`.

