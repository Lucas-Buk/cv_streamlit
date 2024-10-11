# Meu CV Interativo com Streamlit

Este repositório contém o código-fonte para um CV interativo criado usando o [Streamlit](https://streamlit.io/). O aplicativo permite que você exiba seu currículo de forma dinâmica e elegante diretamente na web.

## Demonstração

Você pode visualizar o CV interativo [aqui](https://lucasbuk.streamlit.app/).

## Como executar localmente

### Pré-requisitos

Certifique-se de que você tenha o **Python** instalado em seu ambiente. Você pode verificar a versão do Python com o seguinte comando:

```bash
python --version
```

### Instalação

1. Clone este repositório:

```bash
git clone https://github.com/Lucas-Buk/cv_streamlit
```

2. Navegue até o diretório do projeto:

```bash
cd cv_streamlit
```

3. Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
# No Windows
python -m venv venv
venv\Scripts\activate

# No Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

4. Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

### Executando o CV

Após instalar as dependências, você pode rodar o aplicativo usando o seguinte comando:

```bash
streamlit run app.py
```

Isso abrirá o CV interativo em seu navegador padrão.

### Estrutura do Projeto

- **`app.py`**: Arquivo principal que contém o código para o CV interativo em Streamlit.
- **`assets/`**: Pasta contendo imagens e outros recursos usados no CV.
- **`requirements.txt`**: Arquivo com as dependências necessárias para rodar o projeto.

### Personalização

Você pode facilmente modificar o conteúdo do CV alterando o arquivo `app.py`. Aqui, você poderá mudar os textos, informações de contato, links para redes sociais, e muito mais.

### Deploy

Caso queira disponibilizar o CV na web, você pode usar o [Streamlit Cloud](https://streamlit.io/cloud) para realizar o deploy diretamente do repositório GitHub.

1. Acesse o [Streamlit Cloud](https://streamlit.io/cloud) e crie uma nova aplicação.
2. Conecte seu repositório GitHub.
3. Selecione o arquivo `app.py` como o script principal.
4. Clique em "Deploy".

### Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Streamlit**: Framework para a criação de aplicativos web interativos.
- **Pandas**: Para manipulação e exibição de dados (se aplicável).
- **HTML/CSS**: Para estilização básica (se aplicável).

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Caso tenha alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato:

- Email: lucas.cardoso@maua.br
<!-- - LinkedIn: [Seu Nome](https://linkedin.com/in/seu-perfil) -->

---

Feito com ❤️ por [Lucas Buk Cardoso](https://github.com/Lucas-Buk)
```