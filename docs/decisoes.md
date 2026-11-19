# Decisões do Iron Meridian

Registro das decisões tomadas pelo desenvolvedor quando havia mais de um caminho defensável (veja *Decisões bloqueantes* no `AGENTS.md`). Cada decisão leva o próximo número livre. Uma decisão que muda outra aponta para ela.

## 1. Onde ficam as regras para agentes de IA

- **Data:** 12/11/2026
- **Decisão:** as regras ficam no `AGENTS.md`, e o `CLAUDE.md` tem só a linha `@AGENTS.md`, como no Redweave.
- **Por quê:** outras ferramentas de IA também leem o `AGENTS.md`, e as regras ficam num lugar só.

## 2. Fluxo de branches

- **Data:** 12/11/2026
- **Decisão:** Gitflow sem `homolog`. `feature/{issue}-{slug}` sai do `develop` e volta para ele; ao fechar a versão, uma `release/X.Y.Z` sai do `develop` e vai para o `main` e de volta para o `develop`; `hotfix/{issue}-{slug}` sai do `main`.
- **Alternativas recusadas:** o fluxo completo do Redweave, com `homolog`; e o fluxo simples, sem `release/X.Y.Z` fora das versões MAJOR.
- **Por quê:** o teste na instância temporária, feito na `release/X.Y.Z`, já faz o papel da `homolog`.

## 3. Toda tarefa começa por uma issue

- **Data:** 12/11/2026
- **Decisão:** toda tarefa tem uma issue no GitHub. A branch leva o número dela (`feature/12-inventory-hud`), e o PR traz `Closes #n`.
- **Alternativas recusadas:** issue só para mudanças grandes; branch sem número de issue.

## 4. Regras de processo trazidas do Redweave

- **Data:** 12/11/2026
- **Decisão:** entram as *Decisões bloqueantes*, o *Início e fim de tarefa* e a *Validação no PR*. Também entram, sem precisar de escolha, a autorização por ação, o merge feito só pelo desenvolvedor, a autoria sem IA, a assinatura SSH, os commits atômicos e a proibição do `--no-verify`.
- **Alternativa recusada:** o prompt de continuidade em `tmp/prompt/` quando o contexto passa de 80%.

## 5. Issue do PR que criou a regra das issues

- **Data:** 19/11/2026
- **Decisão:** o PR #3, aberto antes da decisão 3, ganha a issue #5 e o `Closes #5`. A branch continua `docs/fluxo-git`, porque trocar o nome fecharia o PR.
- **Alternativa recusada:** deixar o #3 sem issue, como exceção.
- **Aplica:** a decisão 3.

## 6. Portal Gun 3.0.0 fora das atualizações do ciclo 2.2.1

- **Data:** 19/11/2026
- **Decisão:** as outras 26 atualizações entram na 2.2.1, que continua PATCH. O Portal Gun fica na 2.1.1, no `scripts/update-ignore.json`, até ser testado com um mundo existente (issue #9).
- **Alternativa recusada:** aplicar as 27 de uma vez, o que faria o ciclo virar 2.3.0.
- **Por quê:** a 3.0.0 refaz o Large Button e o Pedestal Button e o sistema de variantes, o que pode quebrar mundos existentes.

## 7. Tecla do "Lock hotbar slot" do SCC 1.6.5

- **Data:** 19/11/2026
- **Decisão:** a ação nova `key.scc.lock_slot` fica em **Alt + L**. O padrão do mod, Alt + K, colidia com os detalhes do último pedido, que já estavam nessa tecla.
- **Alternativa recusada:** deixar a ação sem tecla.

## 8. O ciclo 2.2.1 passa a ser 2.3.0

- **Data:** 19/11/2026
- **Decisão:** a tecla nova do SCC (decisão 7) é uma mudança de teclas, que o `docs/VERSIONAMENTO.md` trata como MINOR. Na dúvida, vale a casa mais alta, e o ciclo fecha como **2.3.0**.
- **Alternativa recusada:** manter 2.2.1 (PATCH), porque nenhuma tecla que o jogador já usava mudou.
- **Muda:** a abertura do ciclo 2.2.1 (PR #7).

## 9. Portal Gun continua na 2.1.1

- **Data:** 19/11/2026
- **Decisão:** o Portal Gun (Aperture Innovations) fica na 2.1.1, no `scripts/update-ignore.json`, até o autor corrigir a 3.0.0. A issue #9 continua aberta.
- **Alternativa recusada:** atualizar na 2.3.0 com um aviso para quebrar e recolocar os botões, porque perder dados de bloco num mundo existente seria MAJOR.
- **Por quê:** no teste, a 3.0.0 lançou `ArrayIndexOutOfBoundsException` em `LargeButtonBlockEntity.loadAdditional` ao carregar o Large Button e o Pedestal Button colocados na 2.1.1, e o jogo descartou os dados dos dois. A Antline passou.
- **Confirma:** a decisão 6.

## 10. Botões do pack num resource pack próprio

- **Data:** 19/11/2026
- **Decisão:** os botões, sliders e o logo do título vêm do resource pack **Iron Meridian UI** (`resourcepacks/Iron Meridian UI/`), ativado por padrão no `configureddefaults/options.txt`, acima do Default Dark Mode. Assim o visual chega a todas as telas que usam os botões do Minecraft, inclusive as dos mods.
- **Alternativa recusada:** aplicar a textura só nas telas editadas pelo FancyMenu.
- **Contexto:** a arte (fundos, emblema, nome e textura de metal) foi gerada por IA a partir de prompts do próprio pack; os sprites com medida exata saem dela por script (`scripts/gera-arte-telas.py`).

## 11. Telas da primeira etapa da personalização

- **Data:** 19/11/2026
- **Decisão:** entram a tela inicial (fundo e logo), a tela de carregamento do Drippy (fundo, emblema e barra ciano), a pausa, as opções, a seleção e a criação de mundo e a lista de mods (fundo desfocado, pelo layout universal do FancyMenu) e o ícone da instância no zip de importação.

## 12. Sai o fundo antigo da tela inicial

- **Data:** 19/11/2026
- **Decisão:** o `technoverse_frontier_v7_background.png` sai do pack.
- **Alternativa recusada:** mantê-lo guardado, sem uso.
- **Por quê:** a imagem parecia vir de outro modpack, e a licença MIT do repositório cobre só os arquivos próprios do pack.

## 13. Sai o Universal Keybinds

- **Data:** 19/11/2026
- **Decisão:** o Universal Keybinds sai na 2.5.0. As teclas passam a ficar só no `options.txt` de cada instância, e o mapa do pack continua chegando pelo `configureddefaults/options.txt`.
- **Alternativa recusada:** manter o mod e explicar a tela de perfil no INSTALL.md.
- **Por quê:** o mod (1.0.0, a única versão) abre uma tela de perfil em toda instalação nova, sem opção para desligar, e derruba o jogo quando o jogador salva um perfil com um nome que já existe (`IllegalStateException: Profile already exists`). Ele também grava as teclas de uma instância nova no perfil global, desfazendo as das outras instâncias. Nenhum mod depende dele.
