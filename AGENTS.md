# Iron Meridian

Modpack de **tecnologia e construção** para **Minecraft 1.21.1 NeoForge**, singleplayer, sem magia. É distribuído com **packwiz** a partir de `github.com/marcelofabianov/iron-meridian`, público e com licença MIT. O repositório **não tem nenhum `.jar`**.

O usuário fala português. Responda, documente e escreva os commits, as issues e os PRs em português.

## Regras do pack (siga à risca)

As regras completas estão no `README.md`, em *Regras de construção do pack*.

1. **Compatibilidade:** o mod precisa ter versão para **NeoForge 1.21.1**.
2. **Sem magia:** sem exceções.
3. **Sem conflitos nem duplicidade:** não adicione um mod que repete a função de outro que o pack já tem.
4. **Dependências primeiro:** só remova um mod se nenhum outro depender dele. Confira com `python3 scripts/mods.py who-needs <modId>`.
5. **Qualidade:** prefira mods bem avaliados e **mantidos**, com versão recente para a 1.21.1. Um mod abandonado não entra, mesmo que seja popular.
6. **Verificação:** antes de adicionar, confira as dependências e a faixa de versão no `neoforge.mods.toml` do jar. Depois, **teste numa instância temporária**.
7. **Fontes:** **Modrinth primeiro**, com o hash conferido. Use o CurseForge se o mod não existir no Modrinth ou se a versão estável mais nova só estiver lá (regra 9).
8. **Pasta limpa:** durante os testes, os mods removidos ficam como `.disabled`, e são apagados depois que a mudança é aprovada.
9. **Sempre a versão estável mais nova:** use a release mais recente para a 1.21.1. Beta ou alpha só entram se o mod não tiver nenhuma versão estável.

Ao sugerir mods:
- Avalie cada candidato por essas regras e diga por que cada descartado ficou de fora.
- **Confira antes o `docs/MODS-REMOVIDOS.md`.** Mods que já saíram, como Squat Grow, Just Dire Things e LaserIO, não voltam sem um motivo novo.
- Leia as dependências no `neoforge.mods.toml` do jar, inclusive as opcionais com faixa de versão. Uma opcional instalada fora da faixa também impede o jogo de abrir: foi o caso do Applied Oritech, que pedia o ExtendedAE 2.2.36 ou mais novo.
- Compare a versão do Modrinth com a do CurseForge. Alguns mods param num site e continuam no outro (ExtendedAE e Replication).

## Fluxo de trabalho

- **Anote no `PENDENTES.txt`.** Toda mudança é registrada nesse arquivo na raiz, que é local e fica fora do git e do pack.
- **Versão:** toda mudança define a casa da versão pelo `docs/VERSIONAMENTO.md`. Uma versão com mudanças de vários tipos fica com a casa mais alta.
- **Git:** branches, commits, PRs e releases seguem a seção *Git* abaixo.
- **Listas numeradas:** numere sempre as listas de mods, porque o usuário escolhe pelo número.
- **Uma instância por vez:** ao pedir "nova instância", crie uma só. Mantenha uma instância aberta por vez.

## Como trabalhar

### Decisões bloqueantes

É bloqueante qualquer ponto com mais de um caminho defensável em que a escolha altere os mods do pack, as dependências, o processo, os mundos do jogador, as teclas ou a progressão.

1. Identifique a decisão e pare antes de implementá-la.
2. Apresente as alternativas, com a sua recomendação e, de forma explícita, a opção "Nenhuma das opções".
3. Espere a confirmação explícita.
4. Implemente e registre a resposta em `docs/decisoes.md`, com o próximo número livre. Resposta que muda outra aponta para ela.

Autorização para começar um trabalho não resolve os bloqueios dele, mesmo que a decisão pareça pequena ou reversível. A autorização de uma ação pontual (commit, push, apagar uma branch) não entra no `docs/decisoes.md`.

### Início e fim de tarefa

- **Alinhamento:** ao iniciar uma tarefa, descreva em poucas linhas o que vamos fazer e pergunte se o desenvolvedor tem algo a acrescentar, antes da rodada de decisões, da issue e da branch.
- **Encerramento do PR:** depois do merge de um PR, nesta ordem, peça autorização para apagar a branch local e a remota, apresente no que vai atuar em seguida e pergunte se o desenvolvedor quer algum ajuste no roteiro das próximas tarefas.

### Validação no PR

A descrição do PR informa os documentos conferidos e a evidência de cada um. Numa mudança de mod, isso inclui:
- as regras do pack (`README.md`) e o `docs/MODS-REMOVIDOS.md`;
- a casa da versão pelo `docs/VERSIONAMENTO.md`;
- as teclas no `docs/TECLAS.md`;
- o resultado do teste na instância temporária: crash, mixins, KubeJS e mundos.

## Git

- **Autorização:** nunca faça commit, push, PR, tag ou release sem autorização explícita para aquela ação. Antes, mostre os arquivos, o resumo e a mensagem ou o título e a descrição propostos.
- **Merge:** somente o desenvolvedor faz.
- **Autoria:** nunca atribua autoria ou coautoria a uma IA, nem em commits, PRs, issues, tags, releases ou comentários.
- **Assinatura:** os commits feitos na máquina do desenvolvedor são assinados com SSH. Não desligue a assinatura.
- **Remote:** `git@github.com-zenndg:zenndg/iron-meridian.git`. Não troque por HTTPS nem por `git@github.com:`, que caem na conta profissional.
- **Conta do `gh`:** esta é a conta `zenndg`. Se o `gh api user --jq .login` mostrar outra, prefixe o comando com `GH_TOKEN=$(gh auth token --user zenndg)`.

### Fluxo de branches

O repositório segue o Gitflow, com Semantic Versioning (adaptado em `docs/VERSIONAMENTO.md`) e Conventional Commits.

| Branch | Sai de | Volta para | Papel |
|---|---|---|---|
| `main` | — | — | Versão publicada. Quem já instalou recebe o que entra aqui na próxima abertura do jogo. Cada merge vira uma tag |
| `release/X.Y.Z` | `develop` | `main` e `develop` | Fechamento da versão: `CHANGELOG.md`, `version` do `pack.toml` e teste na instância temporária |
| `develop` | `main` | `release/X.Y.Z` | Integração do ciclo em andamento. É a branch padrão no GitHub |
| `feature/{issue}-{slug}` | `develop` | `develop` | Mod novo, removido ou atualizado, config, KubeJS, documentação ou tarefa técnica |
| `hotfix/{issue}-{slug}` | `main` | `main` e `develop` | Correção urgente do que já foi publicado, como um pack que não abre |
| `v1` | — | — | Linha 1, congelada na 1.1.20 |

Uma `release/X.0.0` (MAJOR) só vai para o `main` depois de passar nos testes, inclusive com um mundo existente.

### Regras de Git

- **Proibido:** commit direto em `main` ou `develop`; usar `--no-verify` (o hook `scripts/pre-push` valida o índice); misturar várias mudanças lógicas num commit.
- **Issue:** toda tarefa começa por uma issue, e a branch leva o número dela. O nome da branch fica em inglês e em `kebab-case`: `feature/12-inventory-hud`.
- **PR:** todo merge é feito por PR, com `Closes #n` na descrição.
- **Commits:** em Conventional Commits, em português, e atômicos: `feat: adiciona o InventoryHUD+`, `fix: corrige a receita do ...`, `chore: abre o ciclo 2.2.1`, `docs: ...`. Os títulos de PR seguem o mesmo formato.
- **Versão:** a casa segue o `docs/VERSIONAMENTO.md`, com tag anotada `vX.Y.Z` no `main`. Tag e release só quando pedirem, pelo processo da seção 9 de `docs/MANUTENCAO.md`.

## Comandos

```bash
~/go/bin/packwiz modrinth add --project-id <id> --version-id <id> -y   # adicionar mod (Modrinth)
~/go/bin/packwiz curseforge detect                                     # adicionar mod (jar do CurseForge em mods/)
~/go/bin/packwiz remove <nome-sem-.pw.toml>
~/go/bin/packwiz refresh
python3 scripts/mods.py sync            # gera de novo o mods.json e o docs/MODS.md
python3 scripts/mods.py check           # lista as versões estáveis novas
python3 scripts/mods.py update [--apply] [--only <nome>]
python3 scripts/mods.py who-needs <modId>
```

- O `packwiz` não está no PATH. Use `~/go/bin/packwiz`.
- **Não use `packwiz curseforge add -y` nem `packwiz update --all`.** Eles trocam a origem das dependências e duplicam entradas.
- Depois de `packwiz modrinth add`, confira o `git status`: ele também pode trocar a origem de uma dependência ou criar uma entrada duplicada (aconteceu com o Sophisticated Backpacks e o Productive Bees).
- Para deixar um mod de fora das atualizações, coloque o nome e o motivo em `scripts/update-ignore.json`.
- O `mods.py check` só compara com a mesma fonte do `.pw.toml`. Ele não avisa quando o outro site tem uma versão mais nova.
- Use a API do Modrinth (`api.modrinth.com/v2`) com `loaders=["neoforge"]` e `game_versions=["1.21.1"]` para achar a versão estável e as dependências.

## Ao adicionar ou remover um mod, atualize junto

1. `python3 scripts/mods.py sync`.
2. `docs/GUIA-DOS-MODS.md`: um resumo de 3 linhas na categoria certa, em ordem alfabética, renumerando os seguintes, e o total no topo.
3. O total de mods no `README.md` (duas ocorrências) e no `INSTALL.md` (duas ocorrências).
4. A lista de destaques do `README.md`, se fizer sentido.
   - Se o mod novo usar uma biblioteca, acrescente-o na linha "Exigida por" dela no guia.
   - Se ele mudar algo do jogo, atualize o `docs/PROGRESSAO.md` e o `docs/COMANDOS.md` quando couber.
5. **Teclas** (veja a seção abaixo).
6. Na remoção, ou quando um mod for testado e descartado, registre-o em `docs/MODS-REMOVIDOS.md`.
7. Uma linha no `PENDENTES.txt` e, no fim do ciclo, a seção da versão no `CHANGELOG.md`.

## Teclas

- A fonte de verdade é o `configureddefaults/options.txt` (só as linhas `key_`), e a documentação fica em `docs/TECLAS.md`.
- Ao adicionar um mod com teclas, leia os padrões no bytecode da classe que cria os `KeyMapping` (javap) e compare com o mapa.
- Resolva colisões no `options.txt`. Use `key.keyboard.unknown` para deixar uma ação sem tecla, ou o sufixo `:SHIFT`, `:ALT` ou `:CONTROL` para um modificador.
- Documente no `TECLAS.md`:
  - na tabela de principais teclas;
  - em *Sem tecla, de propósito*;
  - na seção do mod, em ordem alfabética.
- O `configureddefaults/options.txt` precisa manter a linha `version:` no topo. Sem ela, o jogo descarta o arquivo em instalações novas.
- O `configureddefaults/` só vale para instalações novas. Para mudar a instância do usuário, edite com o jogo fechado o `options.txt` dela **e** o perfil do Universal Keybinds, em `~/.config/JustKeybinds/profiles/default/keybinds.json`. Sem o perfil, o mod reverte as teclas.
- Ids que começam com `gui.` (por exemplo, `gui.xaero_*`) podem ser ações no mundo, não de tela.
- Ações que só funcionam dentro de telas não colidem com as do mundo.

## Testar numa instância temporária

O procedimento completo está na seção 6 de `docs/MANUTENCAO.md`.

1. **Feche o Prism Launcher antes.** Com ele aberto, o Prism grava de volta o `instance.cfg` e a cópia se atualiza pelo `main`.
2. Copie uma instância já instalada, sem os mundos, e deixe `PreLaunchCommand=` vazio.
3. Sirva o pack local com `packwiz serve -p 8766 --refresh=false`. Depois de adicionar arquivos, rode `packwiz refresh` e reinicie o serve.
4. Instale na cópia, dentro da pasta `minecraft` dela: `java -jar packwiz-installer-bootstrap.jar -g -s client http://localhost:8766/pack.toml`.
5. Abra o jogo e confira:
   - se houve crash;
   - se algum mixin falhou (`Mixin apply ... failed` no `logs/latest.log`);
   - se o KubeJS carregou com 0 erros (`logs/kubejs/server.log`);
   - se mundos novos e existentes carregam.
6. Para testar um mundo existente, copie também um mundo para a cópia e abra com `prismlauncher --launch <instância> --world <mundo>`.
7. Compare as linhas de erro com o `latest.log` da instância do usuário. Só as novas importam, e as conhecidas estão em `docs/KNOWN_ISSUES.md`.
8. Apague a cópia e pare o `packwiz serve`.

## Ambiente local

| O quê | Onde |
|---|---|
| Repositório | `~/Workspace/zenndg/iron-meridian` |
| Instância de jogo do usuário (1.x) | Prism, `~/.local/share/PrismLauncher/instances/IronMeridian-Prism/`, travada na tag `v1.1.20`. Mundo `saves/2026-10-21`, player "Zennd". |
| Instância da 2.x | Prism, `~/.local/share/PrismLauncher/instances/IronMeridian2/`, seguindo o `main`. Mundo `saves/20261109`, player "Zennd". |
| Java para o javap | `~/.local/share/PrismLauncher/java/java-runtime-delta/bin/` |
| Leitor de NBT (save, região, `level.dat`) | `~/.cache/iron-meridian/nbt.py`, com as funções `load`, `World`, `find` e `todict` |

- As duas instâncias dividem o perfil global do Universal Keybinds.
- O save só reflete o jogo depois que ele salva (Esc ou sair do mundo).
- Não mexa na instância do usuário com o jogo aberto.
- Não investigue dispositivos de entrada (`/dev/input`) sem pedir.
- Não use `pkill -f <padrão>` com um padrão que aparece no próprio comando: isso mata o shell.
- No zsh, `ls | grep` pode falhar por causa de aliases, e globs como `--include=*.toml` dão "no matches found". Prefira `find`, aspas ou Python.
- O Prism fica na versão 11.0.1 por escolha do usuário. Não sugira atualizar.

## Estrutura

- `pack.toml` e `index.toml` definem o pack.
- `mods/*.pw.toml` tem um arquivo por mod.
- `config/`, `defaultconfigs/` e `kubejs/` guardam configurações e scripts do pack. `kubejs/data/` substitui arquivos de dados dos mods (receitas e loot).
- `configureddefaults/` tem padrões que só valem na primeira abertura.
- Configurações de preferência do jogador recebem `preserve = true` no `index.toml`.
- `scripts/`, `release/`, `docs/`, `mods.json` e este arquivo ficam no `.packwizignore`, fora do download do jogador.
- O hook `scripts/pre-push` valida o índice antes do push.
