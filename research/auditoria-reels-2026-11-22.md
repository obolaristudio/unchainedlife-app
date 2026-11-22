# Auditoria: o que está travando os Reels (22/11/2026)

Base: research/revisoes.md (métricas lidas pela API do Instagram). Dados de 20/11 em diante não puderam ser lidos: o token do Instagram foi invalidado (OAuthException 190, senha trocada ou sessão encerrada pelo Facebook).

## Vencedores x travados
| Reel | Views 24 h | Envios/1k | Tempo médio | Abertura |
|---|---|---|---|---|
| Carboidrato | 4.818 | 16,8 | 25,6 s | afirmação forte no 1º s |
| Reta | 3.865 | 25,6 | 24,5 s | número ("1 aminoácido = 12 anos") |
| Cobre | 3.603 (42 h) | 33,3 | 17,8 s | vídeo real do Maxwell + curiosidade ampla |
| Resveratrol | 1.609 | 21,1 | 12,6 s | curiosidade ampla |
| BPC-157 | 323 | 12,4 | 28,0 s | nome técnico |
| Resistência à insulina | 281 | 7,1 | 7,1 s | cartão "Você sabia?" parado 1,3 s |
| DMSO | 247 | 0 | 7,7 s | cartão "Você sabia?" parado 1 s |

## Travas encontradas (ordem de impacto)
1. Bloqueio técnico: conexão do Instagram caiu. Sem ela não há publicação agendada, resposta de comentário, GUIA por DM nem leitura de métricas.
2. Primeiro segundo fraco: os 2 piores abrem com cartão parado; os 3 melhores abrem com número/afirmação concreta. Retenção caiu de ~18–25 s para ~7 s.
3. Volume excessivo: ~4 Reels/dia (rotina da madrugada + vídeos sob demanda), vários com <4 h de intervalo. Canibalização de alcance.
4. Nome técnico no gancho (BPC-157, DMSO, ARA-290): alta retenção de quem já é seguidor, mas não sai da base.
5. Ausência de revelação concreta/numérica nos últimos vídeos.
6. Vídeos de cartões de texto (rotina) puxam a média do perfil para baixo (300–950 views).
7. Comentário-pergunta não fixado (API não permite): pergunta fica escondida.

## Plano
- Reconectar o Instagram (link Composio).
- 2 Reels/dia fixos (12:10 e 20:10 ET), ≥6 h entre eles; a rotina da madrugada abastece esses 2 horários, não soma.
- Regra do 1º segundo: número ou afirmação concreta + imagem real; "Você sabia?" só como texto por cima, nunca cartão parado.
- 60–75 s; nome técnico só depois de ~3 s.
- Fixar manualmente o comentário-pergunta em cada post.
