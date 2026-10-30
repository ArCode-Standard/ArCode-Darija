# IDRIS Website

The public-facing bilingual landing page for **IDRIS — ArCode Darija**.

## Structure

- `index.html` — responsive Arabic-first / English-toggle landing page.
- Shared visual identity is loaded from `../assets/idris-logo.svg`.

## Design principles

The interface uses an original visual system informed by platform-native design principles: clarity, hierarchy, restraint, consistency, responsive behavior, accessible controls, and reduced-motion support. It does not copy Apple's proprietary assets or interface.

## Publish with GitHub Pages

1. Open **Settings → Pages** in the repository.
2. Set **Build and deployment → Source** to **GitHub Actions**.
3. The `Deploy IDRIS website` workflow publishes this directory after pushes to `main`.
4. The site URL will appear in the Pages settings once the first deployment completes.

## Content accuracy

The roadmap identifies corpus development as the current focus. The page does not claim that a model checkpoint, approved corpus, training run, or benchmark result already exists.

## Research and developer pages

- `index.html` — bilingual project site, architecture overview, language examples, research dashboard, contribution pathways, and a clearly gated Live Demo placeholder.
- `model-api.html` — dedicated model/API release status and planned developer interface. It explicitly states that no public checkpoint or live endpoint is currently available.

The website uses repository-backed status statements. Illustrative Darija examples are labeled as authored examples, not model outputs or benchmark data.
