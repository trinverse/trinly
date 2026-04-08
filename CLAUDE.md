# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Trinly is a static website for an AI-first technology consultancy specializing in RAG systems, model training & fine-tuning, context engineering, AI agents, data pipelines, and MLOps. Built with HTML, Tailwind CSS (CDN), and vanilla JavaScript. Supports light and dark themes with a toggle. Dark-first design with electric violet/indigo gradient accents.

## Development Commands

### Local Development Server
```bash
# Python 3
python3 -m http.server 8000

# Node.js (if http-server installed)
npx http-server -p 8000
```

### Git Workflow
```bash
# Check current status
git status

# Stage changes
git add <files>

# Commit (avoid auto-closing keywords)
git commit -m "Update: description"

# View recent commits
git log --oneline -10
```

## Architecture

### File Structure
- `index.html` - Main landing page with hero, AI capabilities, how we work, stats, partners, about, contact
- `services.html` - AI services deep-dive with specialties and industries sections
- `showcase.html` - Showcase page for AI apps built (placeholder cards for future content)
- `team.html` - Team page with member cards and culture section
- `sms-consent.html` - SMS opt-in consent proof page for Twilio compliance (TCPA/CTIA)
- `assets/js/theme.js` - Dark mode toggle (class-based, respects OS preference, persists to localStorage)
- `assets/js/app.js` - Page utilities: loader fadeout, mobile menu, scroll-to-top, scroll-reveal, smooth scroll
- `assets/images/` - All image assets, logos, favicons

### Stack
- **Tailwind CSS** via CDN (`https://cdn.tailwindcss.com`) with inline config
- **Sora** for headings, **Inter** for body, **JetBrains Mono** for code accents (all from Google Fonts)
- **Vanilla JavaScript** -- no jQuery or other libraries
- **No build process** -- all CDN-based

### Design System (AI-first, dark-first with violet/indigo accents)
| Token | Light | Dark |
|-------|-------|------|
| Background | `#FAFAFE` | `#0A0A0F` |
| Surface | `#F0F0F8` | `#111118` |
| Card bg | `#FFFFFF` | `#16161E` |
| Text primary | `#0A0A1A` | `#F0F0F5` |
| Text muted | `#64648A` | `#8888A0` |
| Accent | `#7C3AED` (violet) | `#7C3AED` / `#A78BFA` |
| Accent secondary | `#4F46E5` (indigo) | `#4F46E5` |
| CTA gradient | `from-[#7C3AED] to-[#4F46E5]` | same |
| Border | `#E0E0EC` | `#1E1E2E` |
| Glow | `rgba(124,58,237,0.1)` | `rgba(124,58,237,0.1)` |

### Dark Mode
- Class-based (`html.dark`) via `theme.js`
- Respects OS preference on first visit
- Persists choice to `localStorage` key `trinly-theme`
- Toggle button in navbar calls `window.__toggleTheme()`
- Anti-FOUC: inline script in `<head>` calls `window.__applyTheme()` before paint

### Key Patterns
- **Navbar**: Sticky, frosted glass (`backdrop-blur-xl`), border-bottom, logo left, links right, gradient Contact CTA, theme toggle, vanilla JS hamburger menu (`#mobile-menu-btn` / `#mobile-menu`)
- **Cards**: `bg-white dark:bg-[#16161E] border border-[#E0E0EC] dark:border-[#1E1E2E] rounded-xl p-6` with glow-on-hover: `hover:border-[#7C3AED]/40 hover:shadow-[0_0_30px_rgba(124,58,237,0.1)]`
- **CTA Buttons**: Gradient `bg-gradient-to-r from-[#7C3AED] to-[#4F46E5] text-white rounded-lg shadow-lg shadow-[#7C3AED]/25`
- **Outline Buttons**: `text-[#7C3AED] dark:text-[#A78BFA] border border-[#7C3AED]/30 hover:border-[#7C3AED]`
- **Badges/Pills**: `font-mono text-xs text-[#7C3AED] dark:text-[#A78BFA] bg-[#7C3AED]/10 rounded-full border border-[#7C3AED]/20`
- **Headings**: Use `font-heading` class (Sora)
- **Code accents**: Use `font-mono` class (JetBrains Mono) for stats, badges, tech labels
- **Icons**: All inline SVGs in accent color `text-[#7C3AED]`
- **Scroll reveal**: Cards use `data-reveal` attribute with `opacity-0 translate-y-4` initial state
- **Hero glow**: Radial gradient blob behind hero text (CSS only, no images)
- **Footer**: Two-column with copyright and tagline "AI-First Technology Solutions"

## Adding New Content

### New AI Service Card
```html
<div data-reveal class="opacity-0 translate-y-4 transition-all duration-700 bg-white dark:bg-[#16161E] border border-[#E0E0EC] dark:border-[#1E1E2E] rounded-xl p-6 hover:border-[#7C3AED]/40 dark:hover:border-[#7C3AED]/40 hover:shadow-[0_0_30px_rgba(124,58,237,0.1)] transition-all duration-300">
  <div class="w-10 h-10 flex items-center justify-center text-[#7C3AED] mb-4">
    <!-- Inline SVG icon here -->
  </div>
  <h3 class="font-heading text-base font-semibold text-[#0A0A1A] dark:text-[#F0F0F5] mb-2">Service Name</h3>
  <p class="text-sm text-[#64648A] dark:text-[#8888A0] leading-relaxed">Service description</p>
</div>
```

### Navigation Links
Update all 5 pages when adding new pages. The navbar is duplicated across pages (no templating).
Nav order: About | Services | Showcase | Our Team | [Contact CTA] | [Theme Toggle]

### Contact Form
Uses Web3Forms API (access key in `index.html`). AJAX submission via inline `<script>` on index.html.

## Testing & Validation

Since this is a static site with no build process:
1. Serve locally with `python3 -m http.server 8000`
2. Test all 5 pages in both light and dark themes
3. Test responsive: mobile (375px), tablet (768px), desktop (1200px+)
4. Verify mobile hamburger menu opens/closes
5. Verify contact form submission works (Web3Forms)
6. Verify SMS consent form proof-of-record displays
7. Verify dark mode toggle persists across page navigation
8. Check no broken images or missing icons
9. Verify all navigation links work across all 5 pages
10. Verify scroll-reveal animations trigger on scroll
11. Verify gradient glow effects in hero sections

## Deployment

Site deploys automatically to GitHub Pages from `main` branch. Domain configured via `CNAME` file.
