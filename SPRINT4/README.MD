# Sprint 4 - Docker, Python e AWS Partner Accreditation

## Introdução
A Sprint 4 foi focada em aprofundar conhecimentos sobre Docker, Python e credenciamento técnico em AWS. Ao longo dessa sprint, trabalhamos desde os fundamentos de containers Docker até o uso de Python integrado com Docker, além de concluir o credenciamento técnico para AWS Partner.

## Abordamos

### 1. Docker - Do Básico ao Avançado
Nesta parte, foi feita uma imersão completa no Docker, começando pelos conceitos básicos, como containers, imagens e Dockerfiles, até tópicos mais avançados, como:
- **Imagens e Containers**: Aprendemos a criar e gerenciar imagens e containers.
- **Dockerfiles**: Configuração de imagens personalizadas para diferentes aplicações.
- **Volumes e Networks**: Gerenciamento de volumes de dados e redes dentro dos containers.
- **Execução de Aplicações em Containers**: Executamos aplicações Python, como o script `carguru.py` e o gerador de hash, utilizando containers Docker.

#### Desafio Docker
Um dos principais desafios da Sprint foi criar containers para executar scripts Python, o que foi dividido em três etapas:
1. **Criação de uma imagem Docker para rodar o script `carguru.py`**, que escolhia aleatoriamente um carro de uma lista e exibia o resultado.
2. **Reutilização de containers**: Aprendemos a verificar e reiniciar containers que foram parados.
3. **Criação de um novo script `hash_generator.py`**, que recebia uma string como input e gerava um hash SHA-1. Esse script foi executado em um container interativo.

### 2. Python
A linguagem Python foi amplamente utilizada no desafio para integrar o uso de containers Docker. Os pontos principais abordados incluíram:
- **Manipulação de listas e aleatoriedade** com o script `carguru.py`.
- **Uso de bibliotecas Python**, como `hashlib`, para gerar hashes criptográficos com o script `hash_generator.py`.
- **Integração com Docker**, onde os scripts foram executados em ambientes isolados utilizando imagens base do Python e Dockerfiles.

### 3. AWS Partner: Credenciamento Técnico (Português)
Outro componente crucial da Sprint 4 foi o credenciamento técnico na AWS. O módulo forneceu uma visão geral dos principais serviços AWS e melhores práticas para parceiros. Entre os tópicos cobertos estão:
- **Introdução à AWS Cloud**: Explicação dos principais serviços AWS, como EC2, S3, e RDS.
- **Boas práticas de arquitetura**: Foco nas práticas recomendadas para garantir alta disponibilidade, escalabilidade e segurança em ambientes AWS.
- **Casos de uso**: Exemplo de como parceiros AWS podem aplicar esses serviços para entregar soluções de qualidade.

## Conclusão
A Sprint 4 proporcionou um conhecimento sólido sobre Docker, sua integração com Python, e também o credenciamento técnico na AWS. Com isso, não apenas ganhamos experiência prática com containers e execução de aplicações em ambientes isolados, mas também aprofundamos nossos conhecimentos sobre a AWS, ampliando as habilidades para atuar em ambientes de nuvem e containers de forma mais eficaz.
