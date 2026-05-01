RELATÓRIO DE IMPLEMENTAÇÃO DE SERVIÇOS AWS

Data: 30/04/2026
Empresa: Abstergo Industries
Responsável: David

INTRODUÇÃO

Este relatório apresenta o processo de implementação de ferramentas na empresa Abstergo Industries, realizado por David. O objetivo do projeto foi elencar 3 serviços AWS com foco direto na redução de custos operacionais, mantendo alta disponibilidade, escalabilidade e performance para o sistema de dados da empresa farmacêutica.

DESCRIÇÃO DO PROJETO

O projeto de implementação foi dividido em 3 etapas, cada uma focada em otimizar custos em diferentes camadas da arquitetura:

Etapa 1:
Ferramenta: Amazon S3
Foco: Armazenamento escalável e de baixo custo
Descrição de caso de uso:
A empresa armazena grandes volumes de dados como notas fiscais, relatórios e históricos de pedidos. Utilizando o S3 com políticas de ciclo de vida (como S3 Intelligent-Tiering), é possível mover automaticamente dados pouco acessados para camadas mais baratas.
Como reduz custos:
Elimina الحاجة de servidores físicos e reduz custos com armazenamento ativo desnecessário.
Principal ganho:
Alta durabilidade + armazenamento praticamente ilimitado com custo otimizado.
Etapa 2:
Ferramenta: Amazon EC2 Auto Scaling
Foco: Escalabilidade automática e otimização de recursos computacionais
Descrição de caso de uso:
O sistema de pedidos da empresa possui picos de uso (horários comerciais). Com Auto Scaling, as instâncias aumentam ou diminuem automaticamente conforme a demanda.
Como reduz custos:
Evita pagar por servidores ociosos fora do horário de pico.
Principal ganho:
Eficiência operacional + pagamento apenas pelo uso real.
Etapa 3:
Ferramenta: AWS Lambda
Foco: Processamento serverless
Descrição de caso de uso:
Processamento de eventos como validação de pedidos, envio de notificações e integrações com sistemas externos.
Como reduz custos:
Não há cobrança por servidores ativos — apenas pelo tempo de execução.
Principal ganho:
Eliminação de custos com infraestrutura + alta escalabilidade automática.
CONCLUSÃO

A implementação dessas ferramentas na empresa Abstergo Industries proporciona:

Redução significativa de custos operacionais
Melhor uso de recursos computacionais
Escalabilidade sob demanda
Alta disponibilidade e desempenho

Essas soluções permitem que a empresa pague apenas pelo que utiliza, aumentando a eficiência e competitividade no mercado farmacêutico. Recomenda-se a continuidade da estratégia e evolução da arquitetura com novos serviços AWS.
