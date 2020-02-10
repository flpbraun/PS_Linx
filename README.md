# PS_Linx
Web application para Processo Seletivo Linx

# Part_01
  # prod_app.py
  
- Para esta primeira parte precisamos ter instalado no computador o Python 3.6 ou mais atual, para isso em seu terminal de comando Linux, digite:

>>> sudo apt-get update
>>> sudo apt-get install python3.6
>>> sudo apt install python3-pip

- Alem do Python precisamos instalar algumas outras dependencias como Flask e o Pytest, para isso digite:

>>> pip install -U pytest Flask

- Com estas dependencias ja podemos rodar o API.
- Para inicializar o servidor, va ate o diretorio onde se encontra o aplicativo prod_app.py e digite:

>>> python prod_app.py

- Assim o servidor ira comecar a rodar e podemos pelo terminal testa-lo requisitando a pagina principal, ou a pagina onde estarao guardados os novos produtos ou postando um novo produto:

>>> curl http://127.0.0.1:5000/      # pagina inicial

>>> curl http://127.0.0.1:5000/produts     # pagina de armazenamento

>>>curl -H "Content-Type: application/json" -d '{"name":"test_name","id":123}' http://127.0.0.1:5000/products

- Ao tentar postar o mesmo arquivo JSON num periodo menor que 10 minutos, uma mensagem de erro sera exibida e os novo produto nao entrara na base de dados.

  # test_core.py
 
- Precisamos primeiro mudar a variavel path dentro do pregrama test_core.py para o diretorio onde se esta rodando o programa.
- Estando no diretorio onde esta presente o test_core.py e o prod_app.py podemos rodar o teste de todas as funcionalidades do API digitando no terminal:

>>> py.test --cov=prod_app

- E receberemos a porcentagem dos testes feitos e passados/aprovados.

# Part_02

- Primeiro, precisamos instalar as dependencia dessa parte atraves do terminal:

>>> pip install pandas simplejson request

- Apos, podemos abrir o programa sanit_dump.py e mudar o path para onde se encontra o arquivos input-dump.json

- Para a segunda parte temos que estar no diretorio part_02 e no terminal colocar para rodar o agregador de URL que inicara um servidor:

>>> ruby url-aggregator-api.rb

- Pode-se entao rodar o programa sanit_dump.py digitando no terminal:

>>> python sanit_dump.py

- O programa ira testar todas as requisicoes no input-dump.json, eliminando as com mensagem 404 e ira salvar um arquivo de output com todos os produtcId, porem somente tres imagem de cada produto. Dentro do programa voce podera mudar o save_path para onde quiser tambem.




