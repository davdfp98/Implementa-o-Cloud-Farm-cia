
# 📊 RELATÓRIO DE IMPLEMENTAÇÃO DE SERVIÇOS AWS

**Data:** 30/04/2026  
**Empresa:** Abstergo Industries  
**Responsável:** David  

---

## 📌 INTRODUÇÃO

Este relatório apresenta o processo de implementação de ferramentas na empresa **Abstergo Industries**.  
O objetivo do projeto foi **reduzir custos operacionais utilizando serviços AWS**, mantendo:

- Alta disponibilidade  
- Escalabilidade  
- Performance  

---

## 🧱 DESCRIÇÃO DO PROJETO

O projeto foi dividido em **3 etapas**, focadas em otimização de custos em diferentes camadas da arquitetura.

---

### 🔹 Etapa 1 — Amazon S3

**Foco:** Armazenamento escalável e de baixo custo  

**Caso de uso:**  
Armazenamento de notas fiscais, relatórios e histórico de pedidos.

**Estratégia:**  
Uso de lifecycle + S3 Intelligent-Tiering

**Redução de custo:**  
- Elimina servidores físicos  
- Move dados pouco acessados para camadas mais baratas  

**Principal ganho:**  
Alta durabilidade + armazenamento praticamente ilimitado  

---

### 🔹 Etapa 2 — Amazon EC2 Auto Scaling

**Foco:** Escalabilidade automática  

**Caso de uso:**  
Sistema com picos de acesso (horário comercial)

**Estratégia:**  
Escalar instâncias automaticamente conforme demanda  

**Redução de custo:**  
- Evita servidores ociosos  
- Uso sob demanda  

**Principal ganho:**  
Eficiência operacional  

---

### 🔹 Etapa 3 — AWS Lambda

**Foco:** Processamento serverless  

**Caso de uso:**  
Validação de pedidos e integrações  

**Estratégia:**  
Execução sob demanda  

**Redução de custo:**  
- Sem servidores ativos  
- Cobrança por execução  

**Principal ganho:**  
Escalabilidade automática + baixo custo  

---

## ✅ CONCLUSÃO

A implementação dessas soluções proporcionou:

- 💰 Redução significativa de custos  
- ⚙️ Melhor uso de recursos  
- 📈 Escalabilidade sob demanda  
- 🔒 Alta disponibilidade  

A arquitetura permite que a empresa **pague apenas pelo que utiliza**, aumentando sua eficiência e competitividade.

---

## 🚀 PRÓXIMOS PASSOS

- Implementar monitoramento com CloudWatch  
- Adicionar banco de dados gerenciado  
- Evoluir arquitetura para microsserviços  

---

## 👨‍💻 Autor

David Silva
