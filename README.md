# Neurolabkit_wediagram_simple_python_use

O principal objetivo deste repositório é tornar um pouco mais simples o uso das ferraments criadas para se conectarem com o que já foi desenvolvido.

Vamos começar a partir das ferramenta principal. Eu considero a principal ferramenta aqui  o diagrama de blocos. Ou seja, uma vez que tudo estiver funcionando, será possível controlar tudo via página web e é por lá que todos os dados serão integrados e redirecionados. Tamém ela será usada para salvar e gerar informações necessárias para plotar gráficos.

Vamos começar com o básico. 

Qual o objetivo da ferramenta? Criar um ambiente integrado para que possamos fazer intervenções em geral usando jogos, processamento de dados e interação com dados de forma gráfica.

O que preciso pra iniciar? Precisa ter o programa docker instalado (windows ou linux) e clonado este repositório (por favor clone de forma oficial, não usando download para isso, não vai funcionar).

Qual o jeito mais fácil de iniciar? O jeito mais fácil é clonar este repositório e ir à pasta onde ele foi baixado, ir ao terminal e rodar o comando docker-compose up. Depois de esperar um tempo considerável, abrir o navegador e digitar http://localhost:5173, apertar no botão get blocks, conectar os blocos e depois apertar play.

O que este programa inicial faz? Ele é composto por alguns serviços: O primeiro acessa a câmera e detecta pontos anatômicos e envia via mqtt para o segundo bloco conectado a ele (ele usa deeplabcut para detectar os pontos); o segundo bloco é um broker mqtt, usado para conexão entre serviços; o terceiro é o serviço de diagramas e o último, contem 3 arquivos python que podem ser usados conforme a necessidade (processar dados, receber entradas e direcionar dados para uma saída).

Qual a melhor forma de adaptar este código às minhas necessidades? E criando um novo serviço. Para isso, você pode simplesmente copiar a parta processData, alterar o arquivo python de sua preferência e customizar isso nos arquivos docker-compose e dockerfile por similaridade. Também, sinta-se livre para remover o serviço de video2d ele é apenas para apresentação de outras ferramentas (iremos colocar outras no futuro).