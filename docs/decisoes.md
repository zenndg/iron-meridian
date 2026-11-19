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
