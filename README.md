AIChat
AIChat é um projeto de chat simples que se comunica com um LLM (Large Language Model) via uma API FastAPI. 
Ele irá ter embeddings que se baseiam em manuais onde o usuário pode gerar txt para alimentar o chat, ele deve responder somente aquilo que está programado, nunca fugindo para outros temas.


Estrutura do Projeto
bash
Copiar código
project-root/
│
├── app/
│   ├── controllers/
│   │   └── langchain_controller.py  # Controlador para lidar com as requisições
│   │
│   ├── models/
│   │   └── langchain_model.py       # Modelo que interage com o LLMStudio
│   │
│   ├── services/
│   │   └── langchain_service.py     # Lógica de negócio
│   │
│   ├── views/
│   │   └── response_format.py       # Formatação das respostas da API
│   │
│   └── main.py                      # Ponto de entrada para o FastAPI
│
├── frontend/
│   ├── index.html                   # Página do chat (HTML)
│   ├── styles.css                   # Estilos para a interface de chat (CSS)
│   └── script.js                    # Lógica de comunicação e manipulação do chat (JavaScript)
│
├── tests/                           # Testes unitários e de integração
│   └── test_langchain.py
│
├── .env                             # Variáveis de ambiente
├── requirements.txt                 # Dependências do projeto
└── README.md                        # Documentação do projeto


Funcionalidades
Back-end com FastAPI: Interface de comunicação com o LLMStudio, modularizado em controladores, serviços e modelos.
Front-end em HTML/CSS/JavaScript: Interface de chat onde o usuário pode enviar mensagens e visualizar as respostas.
Integração com LLMStudio: Backend comunica com o LLMStudio para processar prompts e receber respostas.
Requisitos
Python 3.10+
Node.js (se necessário para gerenciamento de pacotes no front-end)
FastAPI e Uvicorn para rodar o back-end
LLMStudio como o modelo AI rodando localmente para processamento de linguagem natural
Instalação
Clone o repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/aichat.git
cd aichat
Crie e ative um ambiente virtual (opcional, mas recomendado):

bash
Copiar código
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Configurar as variáveis de ambiente:

Crie um arquivo .env na raiz do projeto com as seguintes variáveis (ajustando conforme necessário):

bash
Copiar código
PORT=8001
LLM_API_KEY=lm-studio
LLM_API_ENDPOINT=http://localhost:1234/v1
Rodando o Back-End
Inicie o servidor FastAPI:

bash
Copiar código
uvicorn app.main:app --reload
O back-end estará disponível em http://127.0.0.1:8001.

Interaja com o LLMStudio:

Certifique-se de que o LLMStudio está rodando na máquina local e disponível no endpoint configurado no .env.

Rodando o Front-End
Abra o arquivo frontend/index.html no navegador:

Isso pode ser feito abrindo diretamente no navegador ou rodando um servidor local simples:

bash
Copiar código
cd frontend
python -m http.server 5500  # Para rodar na porta 5500
A interface do chat estará disponível em http://127.0.0.1:5500.

Testes
Rodar testes unitários:

bash
Copiar código
pytest tests/
Isso vai executar todos os testes unitários configurados no projeto.

Melhorias Futuras
Salvar histórico de mensagens: Implementar uma funcionalidade para salvar e carregar o histórico de conversas do usuário.
Autenticação de Usuário: Adicionar um sistema de login e autenticação para múltiplos usuários.
Anexos e Imagens: Suporte para envio de imagens e anexos no chat.
Estilo responsivo: Melhorar o layout do chat para ser completamente responsivo em dispositivos móveis.
Contribuição
Fork o projeto.
Crie um branch com sua funcionalidade: git checkout -b minha-funcionalidade.
Commit suas mudanças: git commit -m 'Minha nova funcionalidade'.
Envie o branch: git push origin minha-funcionalidade.
Abra um Pull Request.
Licença
Este projeto está licenciado sob os termos da Licença MIT.
