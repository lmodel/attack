---
type: Service
id: https://w3id.org/lmodel/attack/knowledge/services/documentation-site
genre: reference
title: Documentation site
description: The knowledge website at `https://lmodel.github.io/attack/`, a Hugo site in `website/` built from the README, `docs/`, the schema's pages and the knowledge bundle, which redirects the retired mkdocs site's addresses and serves the four `lokf export` files under `/knowledge/`.
resource: website/site.toml
sources:
  - id: site.toml
    resource: website/site.toml
    title: the site's address, title and redirects
  - id: website-readme.md
    resource: website/README.md
    title: how the site is built
  - id: knowledge-website.yaml
    resource: .github/workflows/knowledge-website.yaml
    title: the build and deploy jobs
generated:
  by: process:ktl-librarian
  at: "2026-11-15T02:27:06Z"
status: draft
---

# Documentation site

`website/` is the knowledge website, a Hugo site for `lmodel/attack` at `https://lmodel.github.io/attack`. It shows the README as its home page, the `docs/` pages, and a page for each schema element and each concept. It redirects each page of the retired mkdocs site, such as `/elements/Technique/`, to its successor or to the schema's index.[^site.toml] `website/README.md` says how to build it.[^website-readme.md] The Knowledge website workflow builds it and deploys it to GitHub Pages once `KNOWLEDGE_WEBSITE_ENABLED` is `true`.[^knowledge-website.yaml]

[^site.toml]: website/site.toml, the site's address, title and redirects
[^website-readme.md]: website/README.md
[^knowledge-website.yaml]: .github/workflows/knowledge-website.yaml, the build and deploy jobs
