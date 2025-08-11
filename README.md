# Complex Fractals

Geração e visualização de fractais clássicos do plano complexo — **Mandelbrot**, **Julia** e **Burning Ship** — com foco na comparação entre diferentes conjuntos e análise de padrões.

## Conteúdo

- **`mandelbrot.ipynb`** — geração do conjunto de Mandelbrot, com:
  - Comparação visual com o **Diagrama de Bifurcação** da Equação Logística.
  - Relações com a **equação logística** e **teoria do caos**.

- **`julia.ipynb`** — geração de famílias de conjuntos de Julia para diferentes valores de **c**:
  - Visualização de como pequenas variações em **c** mudam a geometria.

- **`burning_ship.ipynb`** — implementação do fractal Burning Ship:
  - Visualização do fractal.

- **`utils.py`** — implementação da classe **`ComplexNumber`**, criada para manipulação de números complexos sem depender do tipo `complex` nativo do Python.  
  Essa classe é utilizada para cálculos nos fractais e fornece métodos para operações aritméticas, funções matemáticas e propriedades úteis.

### Métodos da classe `ComplexNumber`

#### Construtor e atributos
- `__init__(x, y)` — inicializa o número complexo com parte real `x` e parte imaginária `y`, calculando módulo (`mod`) e argumento (`argument`).

#### Operadores aritméticos
- `__add__` / `__radd__` — soma entre complexos ou entre complexo e número real.
- `__sub__` / `__rsub__` — subtração entre complexos ou entre complexo e número real.
- `__mul__` / `__rmul__` — multiplicação entre complexos ou entre complexo e número real.
- `__truediv__` / `__rtruediv__` — divisão entre complexos ou entre complexo e número real.
- `__pow__` / `__rpow__` — exponenciação com expoente real ou complexo.

#### Comparações
- `__eq__` — igualdade entre complexos ou com número real.
- `__ne__` — diferença entre complexos ou com número real.

#### Funções matemáticas (estáticas)
- `exp(complex)` — exponencial de número complexo.
- `ln(complex)` — logaritmo natural de número complexo.
- `log(complex, base)` — logaritmo de número complexo em base arbitrária.

#### Operadores unários
- `__pos__` — retorna o próprio número.
- `__neg__` — retorna o número oposto.

#### Conversões e utilidades
- `__bool__` — retorna `False` se o número for `0 + 0i`, caso contrário `True`.
- `__str__` — representação como string no formato `a + bi`.
- `__getitem__(index)` — acesso por índice: `0` para parte real, `1` ou `-1` para parte imaginária.
- `__len__` — retorna `2`, número de componentes do complexo.
