# Prompt para design de efeitos sonoros
## Openverse + Real SFX + Earshot · Fluxo para reels, demos e vídeos curtos

> Transcrição traduzida para PT-BR do Google Doc original (em espanhol).

Use este prompt com um agente que consiga acessar o vídeo e executar ferramentas locais. Preencha os campos entre colchetes e anexe o MP4. Se tiver faixas separadas de voz, música ou efeitos, anexe também.

## Ferramentas oficiais
- **Openverse** (https://openverse.org/) — busca gravações e verifica a licença.
- **Real SFX da Clipwing** (https://clipwing.pro/skills/real-sfx) — posiciona os efeitos na timeline e gera a mixagem.
- **Earshot** (https://github.com/Leonxlnx/earshot) — compara e mede sons; gera um efeito pontual quando necessário.

---

# Prompt para copiar

Atue como designer de som e editor de áudio para vídeo curto. Trabalhe sobre o corte aprovado. Desenhe efeitos precisos que reforcem ações visíveis, mantenha a voz em primeiro plano e preserve a intenção da música. Use o Openverse para buscar gravações, o Earshot para compará-las e revisar o áudio, e o Real SFX para sincronizar e mixar.

## Dados do projeto
- Vídeo de referência ou caminho do arquivo: [MP4]
- Faixas separadas, se existirem: [voz / música / efeitos existentes]
- Formato e destino: [reel vertical, demo, anúncio ou outro]
- Estilo sonoro: [sutil e limpo / enérgico / cinematográfico / descreva uma referência]
- Restrições: [uso comercial, licenças aceitas, sons que devo manter, mudanças permitidas]
- Entrega: [pasta de saída]. Alvo de loudness: [padrão: cerca de −14 LUFS integrados para o reel e true peak máximo de −1 dBTP]

## 1. Revise o vídeo e monte a lista de cues
Verifique duração, frame rate e faixas de áudio disponíveis. Se houver timeline, marcadores de edição ou arquivo de cues, use como ponto de partida e confronte com o MP4 final. Identifique o que já está mixado e se há efeitos existentes que valha manter ou substituir. Se houver só uma mixagem estéreo, trate-a como faixa base única e aponte quais ajustes separados exigiriam stems.

Marque entradas de imagens, trocas de card, movimentos rápidos, ações de interface, impactos e revelações relevantes. Para cada cue registre: ID, tempo em milissegundos, frame (se possível), ação visível, família sonora, duração aproximada e prioridade. Confirme marcadores duvidosos frame a frame. Se o vídeo tiver frame rate variável, use os tempos reais de apresentação do arquivo.

Cada som precisa ter função: pop curto para uma aparição, clique discreto para interação, whoosh curto para deslocamento, impacto suave para chegada com peso. Omita movimentos decorativos que já se entendem e agrupe ações muito próximas se competirem com a voz.

## 2. Busque gravações no Openverse
Busque na categoria de áudio com termos curtos em português e inglês (ex.: soft mouth pop, short paper swish, tactile button click, muted wood tap). Para os cues prioritários, reúna 2–3 candidatos com ataque, textura e duração compatíveis com a imagem. Descarte gravações com voz, música, ruído dominante ou caudas que se sobreponham ao próximo evento.

Abra a ficha de origem de cada candidato e confirme que a licença permite o uso previsto. Priorize CC0. Use CC BY só se puder incluir a atribuição exigida. Para anúncio ou reel comercial, exclua material com cláusula não comercial e qualquer candidato cujas permissões ou autoria não possam ser verificadas. Guarde título, autor, URL de origem, licença e URL da licença. Baixe pela via autorizada do provedor.

Mantenha os originais numa pasta de fontes e crie cópias de trabalho para cortar ou converter. Prefira WAV ou FLAC. Mantenha um registro de qual gravação vai em cada cue.

## 3. Avalie e complete com o Earshot
Compare candidatos por caráter, clareza do ataque, duração útil, cauda e nível. Encontre o melhor trecho se o arquivo tiver várias tomadas. Para pop ou clique, localize o início perceptível. Para whoosh, distinga o início do pico que deve acompanhar o movimento. Verifique saturação, golpes duplos ou ruído antes de escolher.

Se nenhuma gravação servir e o projeto permitir síntese, use o Earshot para criar uma variante pontual. Defina caráter, duração e momento de chegada antes de gerar. Registre o preset/receita e marque o recurso como gerado. Se o Real SFX estiver configurado só para gravações, mantenha o som gerado num stem separado e integre no final com o mesmo tempo e nível.

Referência: `earshot sfx list` para explorar receitas e `earshot sfx check` para revisar uma tomada gerada. Confirme as opções na ajuda da sua versão. Combine as métricas com escuta humana quando possível e sinalize cues duvidosos para revisão.

## 4. Sincronize os efeitos com o Real SFX
Carregue a skill Real SFX num ambiente com Python, FFmpeg e acesso à pasta de gravações. Use a lista de cues aprovada como entrada. Revise o plano antes de renderizar: cada cue com o arquivo certo, posição, âncora de sincronia e ajuste de volume.

Para pops, cliques e impactos, alinhe o primeiro ataque audível com o evento visual. Para whoosh, deixe a subida acompanhar o movimento e coloque o pico na chegada quando fizer sentido. Se houver silêncio no início do arquivo, meça o início real antes de deslocar. Aplique fades curtos para evitar cortes bruscos e preserve a cauda natural se houver espaço.

Se um efeito já existir na mixagem base, não duplique. Use faixas separadas quando houver. Se não der para remover um efeito embutido sem afetar voz ou música, mantenha o original e marque o cue para revisão. Confira início, fim e duração do render contra o corte aprovado.

## 5. Nivele voz, música e efeitos
- **Voz:** narração na frente. Corrija variações evidentes de nível; compressão suave só se a dinâmica pedir. Preserve a naturalidade e ouça as consoantes nas frases que coincidem com efeitos.
- **Música:** sustenta o ritmo abaixo da narração. Se competir com a fala, abaixe (ducking) com entradas e saídas suaves. Deixe as pausas respirarem; evite subidas e quedas bruscas.
- **Efeitos:** cues prioritários audíveis, cliques secundários mais discretos. Ajuste cada evento ao que acontece no vídeo e ao redor. Se um efeito encobrir uma palavra, abaixe o cue ou troque o timbre antes de subir a voz do reel inteiro.
- **Mix final:** meça loudness integrado (LUFS) e true peak (dBTP). Referência inicial para reel: −14 LUFS integrados. Ajuste o nível geral e controle picos com moderação. Meça de novo o MP4 após codificar e confirme que a mixagem continua inteligível em mono.

## 6. Verifique e entregue
Revise os primeiros segundos, as transições mais rápidas, os efeitos que coincidem com palavras e o encerramento. Confirme que os cues principais seguem sincronizados após exportar e que o master mantém duração, enquadramento e velocidade do vídeo aprovado. Se possível, ouça em fone e em alto-falante de celular.

Entregue: MP4 com a mixagem final; WAV de efeitos isolados começando em 00:00 com a duração exata do vídeo; stems de voz e música (se disponíveis e editados); planilha de cues em CSV ou JSON com tempos, âncoras, arquivos, ganhos e fontes; arquivo de créditos e licenças.

Feche com um relatório curto: loudness e true peak medidos, quais cues foram gerados e quais momentos precisam de escuta final. Se faltou ferramenta, arquivo ou permissão de uso, identifique a etapa afetada e deixe disponíveis os materiais verificáveis que foi possível preparar.
