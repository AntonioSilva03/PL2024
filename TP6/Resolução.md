# Gramática Independente de Contexto LL(1) para as Frases Exemplo

Para fazer esta gramática foi preciso criar símbolos não-terminais auxiliares para esta não possuir ambiguidade.

## Símbolos terminais:

- **Input**: ` ? `
- **Print**: ` ! `
- **Atribuição**: ` = `
- **Operadores aritméticos**: ` + | - | * | / `
- **Parênteses**: `( | )`
- **Número**: `num`
- **Variável**: `var`
- **Nova_Linha**: `\n`

## Símbolos não terminais:

- **Frase**: ` Frase `
- **Expressão**: `Exp`
- **Expressão Auxiliar**: `ExpAux`
- **Componente**: `Comp`
- **Componente Auxiliar**: `CompAux`
- **Elemento**: `Elem`

## Produções:

```
p1: Frase -> '?' Exp Nova_Linha
p2: Frase -> '!' Exp Nova_Linha
p3: Frase -> 'var' '=' Exp Nova_Linha
p4: Frase -> ε

p5: Exp -> Comp ExpAux
p6: ExpAux -> '+' Exp
p7: ExpAux -> '-' Exp
p8: ExpAux -> ε

p9: Comp -> Elem CompAux
p10: CompAux -> '*' Comp
p11: CompAux -> '/' Comp
p12: CompAux -> ε

p13: Elem -> '(' Exp ')'
p14: Elem -> num
p15: Elem -> var

p16: Nova_Linha -> '\n' Nova_Linha Frase
p17: Nova_Linha -> ε
```

## Look Aheads:

**LA(p1)**: `?`

**LA(p2)**: `!`

**LA(p3)**: `var`

**LA(p4)**: Follow(Frase) = `$`(EOF)

---

**LA(p5)**: FirstN(Comp) = FirstN(Elem) = `( num var`

**LA(p6)**: `+`

**LA(p7)**: `-`

**LA(p8)**: Follow(ExpAux) = Follow(Exp) = `)` U FirstN(Nova_Linha) U Follow(Nova_Linha) =  `) \n` U FirstN(Frase) U Follow(Frase) = `) \n ? ! var $`

---
**LA(p9)**: FirstN(Elem) = `( num var`

**LA(p10**): `*`

**LA(p11)**: `/`

**LA(p12)**: Follow(CompAux) = Follow(Comp) = FirstN(ExpAux) = `+ -` U Follow(ExpAux) = `+ -` U `) \n ? ! var $` = `+ - ) \n ? ! var $`
##### Follow(ExpAux) é igual ao LA(p8)

---
**LA(p13)**: `(`

**LA(p14)**: `num`

**LA(p15)**: `var`

---
**LA(p16)**: `\n`

**LA(p17)**: Follow(Nova_Linha) = FirstN(Frase) U Follow(Frase) = `? ! var $`

## Interseções dos Look Aheads:

- LA(p1) ∩ LA(p2) ∩ LA(p3) = `?` ∩ `!` ∩ `var` = `Ø`

- LA(p6) ∩ LA(p7) ∩ LA(p8) = `+` ∩ `-` ∩ `) \n ? ! var $` = `Ø`

- LA(p10) ∩ LA(p11) ∩ LA(p12) = `*` ∩ `/` ∩ `+ - ) \n ? ! var $` = `Ø`

- LA(p13) ∩ LA(p14) ∩ LA(p15) = `(` ∩ `num` ∩ `var` = `Ø`

- LA(p16) ∩ LA(p17) = `\n` ∩ `? ! var $` = `Ø`