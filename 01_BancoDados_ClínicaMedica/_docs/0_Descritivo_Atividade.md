##Projeto de Banco de Dados: Gestão de Clínica Médica##

Este projeto foca na criação de um **banco de dados `clinica_medica`** para centralizar e gerenciar as informações essenciais de uma clínica. O objetivo é otimizar processos e garantir acesso rápido a dados importantes.


### **Estrutura Essencial**

O banco de dados é composto por tabelas chave:

* **Clínica**: Detalhes sobre as unidades e especialidades oferecidas.
* **Médico**: Informações dos profissionais de saúde.
* **Paciente**: Dados completos dos pacientes.
* **Plano de Saúde**: Registros dos planos aceitos e suas coberturas.
* **Consulta**: Detalhes de cada atendimento (data, paciente, médico, diagnóstico).
* **Exames**: Registro dos exames solicitados e seus resultados.
* **Históricos Médicos**: Visão completa da saúde pregressa do paciente.
* **Secretaria**: Dados da equipe administrativa.



### **Relacionamentos e Funcionalidades**

As tabelas estão interligadas por **chaves estrangeiras** para manter a integridade dos dados, permitindo que um paciente tenha várias consultas, exames e um histórico médico detalhado.

O sistema suporta **operações básicas** como inserir novos dados e **consultas flexíveis**, como buscar pacientes por nome, listar consultas de um médico específico ou verificar exames solicitados.

