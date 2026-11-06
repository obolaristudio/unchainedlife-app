# Google Flow MCP no Mac do Maxwell: auditoria + instalação

Repositório: https://github.com/GTAI-1/flow-mcp, commit auditado `84b548f3aa72b749b82cdbfbb6f91cadebae8642` (23/10/2026), licença ISC.

## Auditoria de segurança (feita em 06/11/2026, sem executar nada)
**O que é seguro:**
- Roda só na sua máquina. O servidor HTTP escuta apenas em 127.0.0.1, com token aleatório (arquivo `~/.flow-mcp/token`, permissão 600) e checagem de Host.
- Usa um **perfil do Chrome separado** (`~/.flow-mcp/chrome-profile`). O seu Chrome do dia a dia não é tocado.
- O login no Google é feito por você, à mão, na janela que abre. O código **não lê, exporta nem envia cookies, senhas ou tokens**.
- Conexões externas só para Google: flow.google.com e generativelanguage.googleapis.com (este só se você quiser a narração Gemini, com chave grátis). Além disso, huggingface.co para baixar o modelo de transcrição Whisper (148 MB), só se usar legendas. Nenhum servidor do autor.
- O `eval` no código roda só um trecho fixo do próprio código dentro da página do Flow, para identificar os vídeos.
- A ferramenta `flow_generate` confere o preço no próprio Flow antes de gastar (`max_credits`).

**Riscos (decisão sua):**
1. **Automação da interface do Google Flow.** Ele "clica" no site do Flow com pausas que imitam uma pessoa. Não é uma API oficial e pode contrariar os termos do Google. **Risco de bloqueio da conta Google.** Recomendação: usar uma conta Google separada da principal (Gmail/Drive), com o plano Google AI nela.
2. **Porta de depuração do Chrome (9333) aberta em localhost** enquanto a janela do Flow estiver aberta: qualquer programa no Mac pode controlar esse Chrome logado. Feche a janela do Flow quando não estiver usando.
3. Projeto de um autor só, versão 0.1.0. Instalar com `npm ci` (versões travadas pelo lockfile) e no commit auditado.
4. O repositório tem um CLAUDE.md grande (55 KB) que o Claude Code lê ao abrir a pasta. Abra o Claude Code na sua pasta de trabalho, não dentro de `~/flow-mcp`.

## Por que não foi instalado pela sessão na nuvem
A sessão do Claude Code em que a operação roda fica num servidor na nuvem, e o seu Mac não está conectado a ela. O Flow precisa de login no seu Chrome, então tem que ser no seu Mac.

## Instalação (cole no Terminal do Mac, um bloco por vez)
```bash
# 1. Verificação
sw_vers; node --version; npm --version; git --version; ls "/Applications/Google Chrome.app" >/dev/null && echo "Chrome OK"
# Node precisa ser 22+. Se faltar: brew install node   (ou baixe em nodejs.org)

# 2. Instalação no commit auditado
git clone https://github.com/GTAI-1/flow-mcp ~/flow-mcp
cd ~/flow-mcp && git checkout 84b548f3aa72b749b82cdbfbb6f91cadebae8642
npm ci && npm run build && ls -la dist/index.js

# 3. Login (abre uma janela própria do Chrome: faça o login nela, à mão, e abra/crie um projeto no Flow)
npm run login

# 4. Registrar no Claude Code (escopo de usuário, não mexe nos outros MCPs)
claude mcp list
claude mcp add --scope user flow -- node "$HOME/flow-mcp/dist/index.js"
claude mcp list        # "flow" deve aparecer como ✓ Connected
```

## Testes (no Claude Code do Mac, nenhum gasta crédito)
- "Check my Flow session": confirma o login, o plano e os créditos (`flow_status`).
- "Liste os modelos disponíveis no Flow": Veo 3.1 Lite/Fast/Quality, Omni Flash, Nano Banana.
- "Liste as ferramentas do servidor flow": devem aparecer flow_generate, flow_wait, flow_assets, flow_download, flow_agent_images, flow_edit, flow_continue, flow_narrate, flow_assemble, flow_captions etc.

## Custos (segundo o próprio projeto)
- Vídeo: Omni 1.1 Flash 7–12 créditos, Veo 3.1 Lite 10, Fast 20, Quality 100.
- Imagens (Nano Banana): 0 créditos.
- Conta grátis: 50 créditos por dia. Plano pago: mais créditos e download em 1080p.

## Exemplos de comandos (sempre pedir o orçamento antes)
- **Imagem, Nano Banana:** "No Flow, gere 1 imagem 9:16 com Nano Banana: corte 3D hiper-realista da pele em fundo preto, fibras de colágeno com brilho cobre, espaço vazio no topo para título, sem texto. Baixe em ~/Obolari/flow."
- **Vídeo, Veo 3.1 Fast:** "No Flow, anime essa imagem com Veo 3.1 Fast, 8 s, 9:16: aproximação lenta da câmera, partículas de cobre entram na pele e as fibras acendem. max_credits 20. Mostre o orçamento antes de gerar."
- **Lote de imagens grátis:** "Use flow_agent_images para gerar 6 imagens 9:16 de órgãos em estilo médico 3D (olho, cérebro, músculo, pele, coração, intestino) em fundo preto."
- **Montagem:** "Junte os clipes baixados com flow_assemble e coloque a música X."
