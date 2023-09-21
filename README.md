# API_Controle_Disciplinas_Tarefas
Esta API foi desenvolvida no intuito de fazer o gerenciamento de alunos, disciplinas e tarefas, sendo possivel a criação, atualização, consulta e exclusão de alunos, disciplinas e tarefas, também é possivel a associação das tarefas com as disciplinas e com os alunos.

# Modelos de Dados
- **Aluno:** Representa um aluno com campos `nome` e `email`.
- **Disciplina:** Representa uma disciplina com campos `nome` e `descricao`.
- **Tarefa:** Representa uma tarefa com campos `titulo`, `descricao`, `data`, `completo`, associação há alunos `alunosTarefas`, associação há tarefas `disciplinasTarefas`.

# EndPoints da API
1. Consulta de Alunos:
   - `/api/alunos/`: (metodo GET) Retorna a lista de todos os alunos.

2. Criação de um Aluno:
   - `/api/alunos/`: (metodo POST) Permite a criação de um novo aluno.

3. Detalhes do Aluno:
   - `/api/alunos/<id>/`: (metodo GET) Retorna detalhes de um aluno específico com base no ID.

4. Atualização de um Aluno:
   - `/api/alunos/<id>/`: (metodo PUT) Permite a atualização dos detalhes de um aluno específico com base no ID.

5. Exclusão de um Aluno:
   - `/api/alunos/<id>/`: (metodo DELETE) Permite a exclusão de um aluno específico com base no ID. Todas as tarefas associadas a esse aluno serão excluídas ou desassociadas.

6. Busca de todas as tarefas de um determinado aluno:
   - `/api/alunos/<id>/tarefas`: (medoto GET) Pr=ermite a busca de todas as tarefas de um único aluno 
  
(as URLS permanecem as mesmas para diciplinas e tarefas, apenas com a alteração da palavra alunos por `disciplinas` e `tarefas`)

# Exemplos de Testes
1. Alunos:
   - {
    "nome": "Luana",
    "email": "luana@gmail.com"
     }

2. Disciplinas:
   - {
    "nome": "Programação",
    "descricao": "Aulas de Pyhton e Django"
     }

3. Tarefas:
   - { 
    "titulo": "Criar um API", 
    "descricao": "Criar uma API com a funcionalidade básica", 
    "data": "2023-09-21", 
    "completo": false, 
    "alunosTarefas": 2, 
    "disciplinasTarefas": [1, 3] 
    }
