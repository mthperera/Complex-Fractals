# Complex Fractals

Geração e visualização de fractais clássicos do plano complexo — **Mandelbrot**, **Julia** e **Burning Ship** — com foco na comparação entre diferentes conjuntos e análise de padrões.

## Estrutura

```
Complex-Fractals/
├── src/
│   └── complex_number.py   # classe ComplexNumber
├── notebooks/
│   ├── mandelbrot.ipynb
│   ├── julia.ipynb
│   └── burning_ship.ipynb
└── requirements.txt
```

## Conteúdo

- **`notebooks/mandelbrot.ipynb`** — geração do conjunto de Mandelbrot, com:
  - Comparação visual com o **Diagrama de Bifurcação** da Equação Logística.
  - Relações com a **equação logística** e **teoria do caos**.

- **`notebooks/julia.ipynb`** — geração de famílias de conjuntos de Julia para diferentes valores de **c**:
  - Visualização de como pequenas variações em **c** mudam a geometria.

- **`notebooks/burning_ship.ipynb`** — implementação do fractal Burning Ship:
  - Visualização do fractal.

- **`src/complex_number.py`** — implementação da classe **`ComplexNumber`**, criada para manipulação de números complexos sem depender do tipo `complex` nativo do Python.  
  Essa classe é utilizada para cálculos nos fractais e fornece métodos para operações aritméticas, funções matemáticas e propriedades úteis.

### Métodos da classe `ComplexNumber`

Os objetos são **imutáveis**: depois de criados, `x` e `y` não podem ser alterados.

#### Construtor e atributos
- `ComplexNumber(x, y)` — cria o número `x + yi`. Aceita qualquer número real, inclusive tipos do NumPy (`bool` não é aceito). Os valores são guardados como `float`.
- `x`, `y` — partes real e imaginária (somente leitura).
- `mod` — módulo `|z|`.
- `argument` — argumento principal, no intervalo `(-π, π]`.

#### Operadores aritméticos
- `+`, `-`, `*`, `/` — entre complexos ou entre complexo e número real, nos dois sentidos (`z + 1` e `1 + z`).
- `**` — expoente real ou complexo, nos dois sentidos (`z ** 2` e `2 ** z`).
  - Expoentes inteiros usam só multiplicações, então `z ** 2` sai exato, sem erro de arredondamento de `cos`/`sin`.
  - Os demais usam o valor principal `exp(w · ln z)`.
  - `0 ** w` vale `0` quando `Re(w) > 0` e lança `ZeroDivisionError` quando `Re(w) ≤ 0` (exceto `w = 0`, que dá `1`).

#### Comparações e hash
- `==` / `!=` — entre complexos ou com número real.
- `hash(z)` — permite usar em `set` e como chave de `dict`. Quando `y = 0`, o hash é igual ao do número real `x`.

#### Funções matemáticas (estáticas)
- `exp(z)` — exponencial.
- `ln(z)` — logaritmo natural principal: `ln|z| + i·arg(z)`.
- `log(z, base)` — logaritmo principal em base real ou complexa (padrão: `e`).

#### Operadores unários
- `+z` — o próprio número.
- `-z` — o número oposto.
- `abs(z)` — o módulo (igual a `mod`).

#### Conversões e utilidades
- `bool(z)` — `False` se o número for `0 + 0i`, caso contrário `True`.
- `str(z)` — formato `a + bi` ou `a - bi`.
- `repr(z)` — formato `ComplexNumber(a, b)`.
- `z[i]` — `0` ou `-2` para a parte real, `1` ou `-1` para a parte imaginária. Também permite desempacotar: `x, y = z`.
- `len(z)` — retorna `2`, número de componentes do complexo.
- Operações com escalares do NumPy (`np.float64(2) * z`) devolvem `ComplexNumber`.
