# TPC6: Construção de uma Gramática Independente de Contexto LL(1)

## Autor:
- António Filipe Castro Silva
- A100533

## Objetivo:

Construir uma gramática independente de contexto para certas frases:

```
?a
b = a * 2/ (27-3)
!a+b
c = a*b / (a/b)
```

Temos de ter em conta:

- Prioridade dos operadores
- Garantir que é LL(1)
- Calcular os Look Ahead para todos os predicados

## Resumo:

- Comecei por determinar todos os símbolos terminais e não-terminais necessários de modo a que não existisse ambiguidade na gramática

- Tratei de todas as produções possíveis a partir desses símbolos

- Calculei todos os Look Aheads dessas produções de forma a que futuramente se conseguisse verificar a ambiguidade

- Com esses Look Aheads, fiz a interseção entre cada conjunto que vem das produções do mesmo símbolo não-terminal para verificar que não havia qualquer ambiguidade na gramática