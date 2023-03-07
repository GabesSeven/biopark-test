<h1 align="center">Teste Treinee Biopark </h1>

<hr>

## 📋 Descrição do Projeto

<p align="justify">
  <br>
  Programa teste da terceira etapa do programa Treinee na empresa Biopark (<a href='https://www2.biopark.com.br/programa-trainees/'>https://www2.biopark.com.br/programa-trainees/</a>). <br>
  <br>
   O objetivo do teste foi contruir um aplicativo responstável por alugar imóveis, tal aplicativo deveria ser capaz de: <br>
   <ul>
    <li>permitir cadastrar edifícios e apartamentos</li>
    <li>permitir visualizar a disponibilidade dos apartamentos</li>
    <li>alugar um apartamento para um locatário</li>
    <li>visualizar o locatário do apartamento</li>
   </ul>
   <br>
</p>

<hr>

## 💽 Banco de Dados

<!--sec data-title="Prompt: OS X and Linux" data-id="OSX_Linux_prompt" data-collapse=true ces-->

O projeto foi construído utilizando banco de dados MySQL, integrado ao django, para execução do programa é necessário criar um banco de dados "biopark" e conceder privilégios para o aplicativo.
No caso de executar em um terminal linux com MySQL instalado, basta digitar os comandos:

    $ service mysql start 
    $ sudo mysql -p
    -> create database biopark;
    -> create user 'biopark'@'localhost' identified by 'biopark';
    -> grant all privileges on biopark.* to 'biopark'@'localhost';
    -> quit;
    
<!--endsec-->  

O banco de dados possui o modelo relacional com três tabelas: Edifício, Apartamento e Cliente. A relação entre elas pode ser observada na imagem abaixo: <br>

![Untitled Diagram drawio](https://user-images.githubusercontent.com/37443722/223207621-62bab491-60af-45f4-b98a-6db004a76ab3.png)

<hr>

## 🖥️ Usabilidade
  
OBS.: Projeto ainda em aperfeiçoamento, como melhorias sugiro: <br>
 <ul>
  <li>criar uma página de autenticação para realizar o cadastro.</li>
  <li>melhorar layout da página.</li>
  <li>realizar filtros para apresentar somente imóveis alugados e somente imóveis disponíveis.</li>
 </ul>
 

<!--sec data-title="Prompt: OS X and Linux" data-id="OSX_Linux_prompt" data-collapse=true ces-->

O programa foi desenvolvido usando Django versão 4.1.7 e como depêndencia possui as seguintes bibliotecas instalas em Python:

    $ pip3 install django django-bootstrap4 django-stdimage pymysql mysqlclient

Ao executar no Ubuntu, ocorreu um erro na biblioteca Pillow, para concertar o erro:

    $ python -m pip install --upgrade pip
    $ python -m pip install --upgrade Pillow

Enfim, para executar o Django, basta executar os comandos para migrar os dados para o banco de dados, criar um novo super usuário e executar o servidor: <br>  

    $ python3 manage.py makemigrations
    $ python3 manage.py migrate
    $ python3 manage.py createsuperuser
     -> user: biopark
     -> password: biopark
    $ python3 manage.py runserver

Ao acessar o endereço "http://127.0.0.1:8000/", tem-se acesso a página inicial do programa que possui as seguintes características: <br>

<ul>
  <li>Página Inicial, lhe mostrará todos os imóveis disponíveis e oculpados. No caso de mais de quatro imóveis cadastrado, o programa abre uma páginação para melhor visualização dos imóveis</li>
  <li>Página Imóvel, ao clicar em um imóvel na página inicial, a página é redirecionado para outra página que mostra o apartamento em maior detalhe, um formmuário que fica disponível somente se imóvel não houver inquilino, caso contrário, aparece os dados do inquilino.</li>
  <li>Página de Cadastro, onde é possível cadastrar imóvel</li>
</ul>
<br>
⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
<ul>
  <li>Ao <strong>primeiro acesso</strong>, a tela inicial <strong>não terá nenhum imóvel</strong>, sendo necessário cadastrá-los.</li>
  <li>Para cadastrar um imóvel, primeiramente deve-se <strong>realizar autenticação na aba "Administrar"</strong>, voltar para "Página Inicial", depois ir em "Cadastrar".</li>
  <li>Caso contrário o programa lhe informará uma mensagem de <strong>"Usuário não autenticado, entre na guia "Cadastro", digite usuário e senha. "</strong></li>
</ul>
⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
<br>
<br>
<p align="center">
  <img src="https://user-images.githubusercontent.com/37443722/223296327-a88d6678-c750-4110-9dfb-159ecc70acec.png" width="500" height="300"/>
</p>
<br>
<br>
<!--endsec-->



## 📁 Acesso ao projeto

Você pode [acessar o código fonte do projeto](https://github.com/GabesSeven/biopark-test/) ou [baixá-lo](https://github.com/GabesSeven/biopark-test/archive/refs/heads/main.zip).

<hr>

## ✔️ Tecnologias utilizadas

- ``Python``
- ``Django``
- ``MySQL``
- ``Bootstrap``
- ``HTML``
- ``CSS``
- ``JS``

<hr>

## 🧑‍💻 Desenvolvedor

| [<img src="https://avatars.githubusercontent.com/u/37443722?v=4" width=115><br><sub>Gabriel Ferreira</sub>](https://github.com/GabesSeven)
| :---: 
