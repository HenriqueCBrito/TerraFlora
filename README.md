# Farm Management System

## Descrição
O **Farm Management System** é uma aplicação web desenvolvida com **Python** e **Django**, projetada para ajudar pequenos agricultores no gerenciamento de suas atividades agrícolas. A plataforma oferece uma variedade de ferramentas, como planejamento de safra, recomendações de pareamento de plantas, gestão de estoque, previsão do tempo, entre outros. Seu objetivo é tornar o gerenciamento agrícola mais eficiente e produtivo.

---

## Funcionalidades Principais

### 1. Calendário de Plantio, Manejo e Colheita
- Planeje e organize todas as fases do cultivo de forma visual.
- Receba alertas automáticos para atividades de manejo e colheita.

### 2. Auxílio para Compra de Plantio com Base na Renda Familiar
- Ferramenta que sugere o melhor tipo de cultivo com base na renda disponível.

### 3. Dicas de Fertilização e Irrigação
- Receba sugestões sobre como otimizar a fertilização e irrigação conforme o tipo de plantio e estação.

### 4. Descrição de Plantios e Compatibilidade (Consórcios e Plantas Inimigas)
- Visualize descrições detalhadas de culturas e saiba quais podem ser plantadas juntas ou devem ser evitadas.

### 5. Previsão do Tempo e Auxílio para o Melhor Momento de Plantio
- Acesse previsões do tempo diretamente no painel e veja o melhor momento para plantar de acordo com as condições climáticas.

### 6. Banco de Dados de Culturas
- Um banco de dados que inclui informações sobre uma ampla variedade de culturas e plantas.

### 7. Calculadora de Plantio
- Estime a quantidade de sementes necessárias para atingir uma produção específica.

### 8. Tabela de Pragas e Ervas Daninhas
- Consulte uma tabela de pragas e ervas daninhas, com dicas sobre como preveni-las ou controlá-las.

### 9. Controle de Estoque
- Gerencie o estoque de insumos e produtos de maneira eficaz com alertas automáticos de reposição.

### 10. Checklist Diário de Atividades
- Organize as tarefas diárias de manejo com um checklist interativo.

### 11. Divisão de Lavoura em Partes
- Gerencie diferentes seções da sua fazenda e distribua as atividades de acordo com cada área.

### 12. Recomendações Baseadas em Atividades do Agricultor
- Receba recomendações personalizadas de ferramentas e técnicas com base nas suas atividades.

### 13. Processo Agrícola e Financeiro
- Acompanhe todas as etapas do processo agrícola e financeiro em tempo real.

---

## Requisitos

Para rodar este projeto, você precisará ter instalado:
- **Python 3.8+**
- **Django 3.2+**
- **SQLite** ou **PostgreSQL** (para produção)
- **pip** (para instalar dependências)

---

## Instalação

```bash
# 1. Clone o repositório:
git clone https://github.com/seu-usuario/farm-management-system.git
   
# 2. Acesse o diretório do projeto:
cd farm-management-system

# 3. Crie e ative um ambiente virtual (opcional, mas recomendado):
python -m venv env
source env/bin/activate  # ou "env\Scripts\activate" no Windows

# 4. Instale as dependências:
pip install -r requirements.txt

# 5. Realize as migrações do banco de dados:
python manage.py migrate

# 6. Execute o servidor de desenvolvimento:
python manage.py runserver
```

---

## Como Usar

1. Acesse o navegador e entre na aplicação pelo endereço: http://127.0.0.1:8000/

2. Registre-se como um novo usuário ou faça login.

3. Explore as funcionalidades no painel de controle para:
- Planejar suas safras
- Consultar o banco de dados de culturas
- Controlar o estoque de produtos
- Gerar relatórios de produtividade

---