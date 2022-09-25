# Little Glue
Aquele programinha maroto pra fazer aquela colinha marota pras eleições!


## Descrição
Bom, devido as últimas decisões do TSE que desfavorecem o uso de celulares nas seções de votação, decidi criar este programa para as pessoas que possuem dificuldades de memorizar os vários números de diversos candidatos nas eleições presidenciais e municipais que ocorrerem.

É bem provável também que muita gente já tenha recebido o famoso "santinho" de seus candidatos ou já tenha preenchido os números com a famosa dupla Papel e Caneta, mas pensando em utilizar a mais alta tecnologia de ponta do Terminal do GNU/Linux aliado a linguagem Python de programação, decidi criar este pequeno programinha para gerar as famosas "colinhas" que podem ser usadas como guia na hora da votação. Você pode criar colinhas para você, seus amigos, parentes, ou qualquer outra pessoa que tenha interesse em ter uma colinha impressa com os candidatos que a pessoa quiser.

**Este programa consegue preencher, salvar e gerar uma colinha em formato HTML, PDF ou imagem JPG para que você possa imprimir e levar no dia da votação.**


## Instalação
É bem simples instalar esse programa, porém ele foi desenvolvido pensando na plataforma GNU/Linux e requer algumas dependências que, talvez, possam estar apenas disponível pra ela. Portanto, o tutorial abaixo seguirá presumindo que você esteja utilizando alguma distribuição baseada no Debian (como o Ubuntu ou Linux Mint, por exemplo).

- **Passo Um:** Baixe o programa clonando o projeto em sua máquina
```shell
git clone https://github.com/Wolfterro/Little-Glue.git
cd Little-Glue
```

- **Passo Dois:** Execute o comando abaixo
```shell
make install
```

- **Passo Trẽs:** Siga as instruções que aparecem no terminal
```shell
================================================================================
===!!! Você vai precisar criar agora uma virtualenv para rodar o projeto! !!!===
================================================================================
===!!! Para isso, execute: mkvirtualenv little-glue --python=python3 && workon little-glue

===!!! OU !!!===

===!!! Execute este: virtualenv little-glue --python=python3 && source little-glue/bin/activate
===!!! Após esse processo, execute o comando: pip install -r requirements.txt
===!!! E pronto, basta rodar o projeto usando o comando: make run
```

E pronto! Você poderá rodar o projeto rodando apenas o último comando do passo três!
```shell
make run
```

## Exemplos de Uso
É possível gerar as colinhas de duas maneiras: Através de um menu interativo ou pela linha de comando, passando o caminho de um arquivo JSON gerado pelo programa (ou manualmente criado por você).

Em todos os casos, após a colinha ser gerada, ela ficará localizada na pasta **generated_glues**, que se localiza na **raiz do projeto!**

### Menu
Para executar o programa via menu, basta rodar o comando abaixo:
```shell
make run
```

Que é a mesma coisa que rodar:
```shell
python main.py menu
```

### Linha de Comando
Para executar o programa via linha de comando, basta utilizar o comando abaixo como exemplo:
```shell
python main.py generate_from <CAMINHO DO ARQUIVO JSON>
```

O arquivo JSON já é gerado automaticamente quando você cadastra uma nova colinha. Caso queira gerar um arquivo JSON por conta própria, leve como base os arquivos abaixo:

#### JSON para Eleições Presidenciais
```json
{
  "candidates_data": {
    "federal_deputy": [
      {
        "number": "9999",
        "name": "João da Feira"
      }
    ],
    "state_deputy": [
      {
        "number": "99999",
        "name": "Marcos do Gás"
      }
    ],
    "senator": [
      {
        "number": "999",
        "name": "Toninho da Padaria"
      }
    ],
    "governor": {
      "number": "99",
      "name": "Delegado José"
    },
    "president": {
      "number": "99",
      "name": "Professor Pereira"
    }
  },
  "color_scheme": ["#ffffff", "#000000"],
  "export_format": "pdf",
  "font_configs": [12, 32, 15, "bold"],
  "election_type": "presidential"
}
```

#### JSON para Eleições Municipais
```json
{
  "candidates_data": {
    "alderman": [
      {
        "number": "99999",
        "name": "João da Feira"
      }
    ],
    "prefect": {
      "number": "99",
      "name": "Professor Pereira"
    }
  },
  "color_scheme": ["#ffffff", "#000000"],
  "export_format": "pdf",
  "font_configs": [12, 32, 15, "bold"],
  "election_type": "municipal"
}
```

Ambos os arquivos JSON de exemplo podem ser encontadas na pasta **example**, na raiz do projeto.
