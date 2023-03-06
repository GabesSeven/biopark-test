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

<hr>

## 🖥️ Banco de Dados

<!--sec data-title="Prompt: OS X and Linux" data-id="OSX_Linux_prompt" data-collapse=true ces-->

O projeto foi construído utilizando banco de dados MySQL, integrado ao django, para execução do programa é necessário criar um banco de dados "biopark" e conceder privilégios para que o aplicativo.
No caso de executar em um terminal linux com MySQL instalado, basta digitar os comandos:

    $ service mysql start 
    $ sudo mysql -p
    -> create database biopark;
    -> grant all privileges on biopark.* to 'biopark'@'localhost';
    -> quit;
    
<!--endsec-->  

O banco de dados possui o modelo relacional onde

<hr>

## 🖥️ Usabilidade
  
OBS.: Projeto ainda em aperfeiçoamento, como melhorias sugiro: <br>
 <ul>
  <li>criar uma página de autenticação para realizar o cadastro.</li>
  <li>melhorar layout da página.</li>
  <li>realizar filtros para apresentar somente imóveis alugados e somente imóveis disponíveis.</li>
 </ul>
 

<!--sec data-title="Prompt: OS X and Linux" data-id="OSX_Linux_prompt" data-collapse=true ces-->

O programa foi desenvolvido usando Django versão 4.1.7 e como depêndencia possui as seguintes bibliotecas

    $ pip install 

To run the "search.py" program, it is necessary to have an input file with the strings to be scraped: <br>

    $ ls input-file.txt 
    user1
    user2
    user3
    user4
    ...

The program is executed passing the input file as the first parameter and the output file as the second parameter: <br>  

    $ python search.py input-file.txt output-file.txt

Finally, the ID of each user separated by pipeline will be returned, if the number of users found corresponding to the searched string is less than four: <br>

    $ ls output-file.txt 
    user1
    |id1,id2,id3
    user2
    |id1,id2
    user3
    |id1
    user4
    |
    ...
    
In the previous example, user1 found four users, user2 two users, user3 one user, and user4 found more than four users.

<!--endsec-->



## 📁 Project access

You can [access the project's source code](https://github.com/GabesSeven/instagram-id-scraper-api/) or [download it](https://github.com/GabesSeven/instagram-id-scraper-api/archive/refs/heads/main.zip).

<hr>

## ✔️ Techniques and technologies used

- ``Python``

<hr>

## 🧑‍💻 Developer

| [<img src="https://avatars.githubusercontent.com/u/37443722?v=4" width=115><br><sub>Gabriel Ferreira</sub>](https://github.com/GabesSeven)
| :---: 
