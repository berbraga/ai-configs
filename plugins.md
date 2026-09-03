# Plugins do Codex

Os conteúdos de plugins não são copiados: são dependências de terceiros e ficam no cache.
Reinstale-os a partir das fontes oficiais:

```bash
codex plugin marketplace add https://github.com/ayghri/i-have-adhd.git --ref main
codex plugin marketplace add https://github.com/affaan-m/ECC.git
codex plugin marketplace add https://github.com/obra/superpowers.git
codex plugin add i-have-adhd@i-have-adhd
codex plugin add ecc@ecc
codex plugin add superpowers@superpowers-dev
```

O arquivo `codex/config.toml` registra os nomes resolvidos dos marketplaces e plugins.
