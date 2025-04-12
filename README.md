# 📝 Projeto To-Do List — Engenharia de Software 2

Esse projeto foi um exercício feito durante as aulas de **Engenharia de Software 2**, onde a proposta era criar um sisteminha simples de **controle de tarefas (to-do list)** usando Python, aplicando os conceitos do padrão arquitetural **MVC (Model-View-Controller)**.

A ideia era botar em prática o que a gente tava vendo na teoria, sem complicar demais — só o básico bem feito!

---

## 🎯 O que esse projeto faz?

Esse to-do list é simples e direto ao ponto. Com ele, você pode:

✅ Adicionar novas tarefas (com título e descrição)  
📋 Ver todas as tarefas cadastradas  
✔️ Marcar uma tarefa como concluída  
🗑️ Remover tarefas que já não fazem mais sentido  

Tudo isso direto pelo terminal, naquele estilo raiz 🖥️

---

## 🧠 E o tal do MVC?

Então... não tá separado em pastinhas como `model`, `view` e `controller`, mas a lógica tá ali:

- **Model:** As tarefas em si, armazenadas numa lista com seus dados.
- **View:** A parte que interage com o usuário via terminal (menus e prints).
- **Controller:** As funções que fazem a mágica acontecer (adicionar, listar, concluir, remover).

Foi nossa primeira experiência prática com o padrão, então a ideia era entender os princípios, não seguir a risca ainda.

---

## ▶️ Como rodar o projeto

1. Garante que o Python (3.6 ou superior) tá instalado aí.
2. Baixa ou clona o repositório.
3. Abre o terminal na pasta do projeto.
4. Roda o comando:

```bash
python app.py
