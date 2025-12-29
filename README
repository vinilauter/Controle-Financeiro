# Financial Control Dashboard | Dashboard de Controle Financeiro

*[Português abaixo]*

## 🇺🇸 English

### About the Project
A personal finance dashboard designed to track income, expenses, and budget goals. Built with a focus on **Software Engineering principles**, this application moves beyond simple scripting by implementing a robust **MVC (Model-View-Controller)** architecture and a professional ETL pipeline connecting Google Sheets to a Python web interface.

**Key Features:**
* **Real-time Data:** Fetches data directly from Google Sheets via API.
* **Budgeting System:** Tracks spending limits per category and globally with visual progress bars.
* **Interactive Analysis:** Filter financial data by Year and Month.
* **Time Series:** Visualizes monthly spending evolution to identify trends.
* **UX/UI:** Clean interface built with Streamlit and Plotly interactive charts.

### Tech Stack
* **Language:** Python 3.x
* **Frontend:** Streamlit
* **Data Processing:** Pandas (ETL & Cleaning)
* **Visualization:** Plotly Express
* **Integration:** Google Sheets API (gspread)

### Project Architecture (MVC)
The project avoids the "spaghetti code" trap by modularizing responsibilities:
* **`app.py` (View):** Handles the UI/UX and user interaction.
* **`src/controller.py` (Controller):** Contains business logic, budget calculations, and data aggregation.
* **`src/etl.py` (Model):** Manages API connections, data extraction, and raw data transformation.
* **`src/utils.py`:** Stores constants, configuration dictionaries, and mapping rules.

### How to Run
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/financial-control.git](https://github.com/your-username/financial-control.git)
    cd financial-control
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Setup Credentials:**
    * Place your Google Cloud `service_account.json` file in the root directory.
    * *Note: This file is not included for security reasons.*
4.  **Run the App:**
    * **Via Terminal:** `streamlit run app.py`
    * **Via Launcher:** Double-click `execute.bat` (Windows only).

### License
**Source-Available / Proprietary.**
This software is provided for educational and portfolio demonstration purposes. The source code is available for viewing and auditing, but unauthorized commercial use, modification, or distribution is strictly prohibited. See the [LICENSE](LICENSE) file for details.

---

## 🇧🇷 Português

### Sobre o Projeto
Um dashboard de finanças pessoais desenvolvido para monitorar receitas, despesas e metas orçamentárias. Construído com foco em **princípios de Engenharia de Software**, esta aplicação vai além de scripts simples, implementando uma arquitetura **MVC (Model-View-Controller)** robusta e um pipeline de ETL profissional conectando Google Sheets a uma interface web em Python.

**Principais Funcionalidades:**
* **Dados em Tempo Real:** Busca dados diretamente do Google Sheets via API.
* **Sistema de Orçamento (Budgeting):** Monitora tetos de gastos por categoria e global com barras de progresso visuais.
* **Análise Interativa:** Filtra dados financeiros por Ano e Mês.
* **Série Temporal:** Visualiza a evolução mensal dos gastos para identificar tendências.
* **UX/UI:** Interface limpa construída com Streamlit e gráficos interativos Plotly.

### Tecnologias Utilizadas
* **Linguagem:** Python 3.x
* **Frontend:** Streamlit
* **Processamento de Dados:** Pandas (ETL e Limpeza)
* **Visualização:** Plotly Express
* **Integração:** Google Sheets API (gspread)

### Arquitetura do Projeto (MVC)
O projeto evita o código desorganizado ("spaghetti code") ao modularizar responsabilidades:
* **`app.py` (View):** Gerencia a interface (UI/UX) e interação do usuário.
* **`src/controller.py` (Controller):** Contém a regra de negócio, cálculos de orçamento e agregação de dados.
* **`src/etl.py` (Model):** Gerencia conexões de API, extração e transformação de dados brutos.
* **`src/utils.py`:** Armazena constantes, dicionários de configuração e regras de mapeamento.

### Como Executar
1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/financial-control.git](https://github.com/seu-usuario/financial-control.git)
    cd financial-control
    ```
2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure as Credenciais:**
    * Coloque seu arquivo `service_account.json` do Google Cloud na raiz do projeto.
    * *Nota: Este arquivo não está incluído por motivos de segurança.*
4.  **Execute o App:**
    * **Via Terminal:** `streamlit run app.py`
    * **Via Launcher:** Clique duas vezes em `iniciar.bat` (apenas Windows).

### Licença
**Source-Available / Proprietária.**
Este software é fornecido para fins educacionais e de demonstração de portfólio. O código-fonte está disponível para visualização e auditoria, mas o uso comercial, modificação ou distribuição não autorizados são estritamente proibidos. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
