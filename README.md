# Curso Python

# Mundo 1

O primeiro mundo foi pensando de forma a apresentar a linguagem ao aluno, o professor irá introduzir a linguagem, seus conceitos, montar o primeiro programa e ensinar alguns recursos básicos.

## Módulo 1 - Introdução ao Mundo da Programação

### [Aula 1 - Seja um programador](https://www.cursoemvideo.com/course/python-3-mundo-1/aulas/introducao-ao-mundo-da-programacao-3/modulos/seja-um-programador/)

Você está pensando em ser um Programador e não sabe por onde começar? Pois nessa aula vamos te dar todas as informações e mostrar o caminho a seguir.

## Módulo 2 - Primeiros passos com o Python

### [Aula 2 – Para que serve o Python?](https://www.cursoemvideo.com/course/python-3-mundo-1/aulas/primeiros-passos-com-o-python/modulos/para-que-serve-o-python/)

De onde vem o Python? Por que esse nome? Quais são as grandes empresas mundiais que usam Python em seus softwares? Essas e muitas outras perguntas serão respondidas nessa aula.

- Respostas
    - De onde vem o Python?

    *Python foi criado por Guido Van Hossum em 1989, e ele criou essa linguagem de programação para ser simples diferente das linguagens que existiam na época (ABC e ALGOL).*

    - Por que esse nome?

    *Guido Van Hossum escolheu esse nome baseado em seu programa de humor favorito.*

    - O que é o Python?
        - *Linguagem de propósito geral*
        - *Fácil e intuitivo*
        - *Multiplataforma*
        - *Batteries included*
        - *Livre (Código-aberto)*
        - *Organizada*
        - *Orientada a objetos*
        - *Muitas bibliotecas*
    - Zen of Python
        - *Bonito é melhor que feio*
        - *Explícito é melhor que implícito*
        - *Simples é melhor que complexo*
        - *Complexo é melhor que complicado*
        - *Linear é melhor do que aninhado*
        - *Esparso é melhor que denso*
        - *Legibilidade conta*
        - *Casos especiais não são especiais o bastante para quebrar as regras*
        - *Ainda que praticidade vença a pureza*
        - *Erros nunca devem passar silenciosamente*
        - *A menos que sejam explicitamente silenciados*
        - *Diante da ambiguidade, recuse a tentação de adivinhar*
        - *Deveria haver um — e preferencialmente só um — modo óbvio para fazer algo*
        - *Embora esse modo possa não ser óbvio a princípio a menos que você seja holandês*
        - *Agora é melhor que nunca*
        - *Embora nunca frequentemente seja melhor que **já***
        - *Se a implementação é difícil de explicar, é uma má ideia*
        - *Se a implementação é fácil de explicar, pode ser uma boa ideia*
        - *Namespaces são uma grande ideia — vamos ter mais dessas!*
    - Principais áreas
        - *Inteligência Artificial*
        - *Biotecnologia*
        - *Computação 3D*
    - Quem usa Python?
        - *ZOPE*
        - *Django*
        - *Air Canada*
        - *BitTorrent*
        - *Globo*
        - *Google*
        - *YouTube*
        - *NASA*
        - *Industrial Light & Magic*
        - *Autodesk*
        - *Blender*
        - *GIMP*
        - *RaspberryPi*
        - *Arduino*
        - Jogos feitos em Python
            - *Frets on Fire*
            - *Jewel Quest*
            - *EVE Online*
            - *Civilization IV*
            - *Battlefield 2*

### [Aula 3 – Instalando o Python3 e o IDLE](https://www.cursoemvideo.com/course/python-3-mundo-1/aulas/primeiros-passos-com-o-python/modulos/instalando-o-python3-e-o-idle/)

Entenda como funciona um Interpretador e veja como o Python funciona. Depois aprenda como instalar o Python 3.0 e o IDLE em seu computador com Windows, Linux ou Mac OS.

### [Aula 4 – Primeiros comandos em Python3](https://www.cursoemvideo.com/course/python-3-mundo-1/aulas/primeiros-passos-com-o-python/modulos/primeiros-comandos-em-python3/)

Agora chegou a hora de aprender os comandos básicos do Python e fazer os primeiros programas em Linguagem Python.

- Comandos

    ```python
    # print() ➡ Escreve algo na tela

    # Mensagens devem ficar entre aspas
    # Números não precisam ficar entre aspas
    # Se você colocar números como mensagens (strings), e somá-las elas irão se juntar
    # Para usar dois tipos diferentes é necessário usar vírgula

    print('Olá, Mundo!') # Olá, Mundo!
    print(7 + 4) # 11
    print('7' + '4') # '74'
    print('Olá' + 5) # Erro
    print('Olá', 5) # Olá 5

    # Variáveis

    nome = 'Heitor'
    idade = 13
    peso = 63.4

    # Como essas váriaveis todas são de tipos diferentes é necessário usar vírgula para mostrar na tela
    print(nome, idade, peso) # Heitor 13 63.4
    print(nome + idade + peso) # Erro

    # Interatividade com o usuário
    # Para você criar uma interatividade com usuário você deve usar um comando, chamado "input"

    # input() ➡ Pede para o usúario uma entrada (resposta)

    nome = input('Qual é seu nome? ') # Qual é seu nome? *Heitor*
    idade = input('Qual é sua idade? ') # Qual é sua idade? *13*
    peso = input('Qual é seu peso? ') # Qual é seu peso? *63.4*

    print(nome, idade, peso) # Heitor 13 63.4
    ```
