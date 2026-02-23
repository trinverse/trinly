# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Trinly is a static website for a technology consultancy specializing in digital image processing, drone operations, photogrammetry, and digital transformation services. Built with HTML, Tailwind CSS (CDN), and vanilla JavaScript. Supports light and dark themes with a toggle.

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
- `index.html` - Main landing page with hero, services, partners, about, contact sections
- `specialties.html` - Drone specialties page
- `portfolio.html` - Portfolio page with filterable project cards
- `team.html` - Team page with member cards and culture section
- `sms-consent.html` - SMS opt-in consent proof page for Twilio compliance (TCPA/CTIA)
- `assets/js/theme.js` - Dark mode toggle (class-based, respects OS preference, persists to localStorage)
- `assets/js/app.js` - Page utilities: loader fadeout, mobile menu, scroll-to-top, portfolio filtering, smooth scroll
- `assets/images/` - All image assets, logos, favicons

### Stack
- **Tailwind CSS** via CDN (`https://cdn.tailwindcss.com`) with inline config
- **Inter** font from Google Fonts
- **Vanilla JavaScript** — no jQuery or other libraries
- **No build process** — all CDN-based

### Design System (ChatGPT aesthetic, monochromatic)
| Token | Light | Dark |
|-------|-------|------|
| Background | `#FFFFFF` | `#212121` |
| Surface alt | `#F7F7F8` | `#2F2F2F` |
| Input bg | `#F4F4F4` | `#2F2F2F` |
| Text primary | `#0D0D0D` | `#ECECEC` |
| Text muted | `#6B7280` | `#8E8EA0` |
| Accent/CTA | `#0D0D0D` | `#ECECEC` |
| Border | `#E5E5E5` | `#3A3A3A` |

### Dark Mode
- Class-based (`html.dark`) via `theme.js`
- Respects OS preference on first visit
- Persists choice to `localStorage` key `trinly-theme`
- Toggle button in navbar calls `window.__toggleTheme()`
- Anti-FOUC: inline script in `<head>` calls `window.__applyTheme()` before paint

### Key Patterns
- **Navbar**: Sticky, white/dark bg, border-bottom, logo left, links right, green Contact CTA, theme toggle, vanilla JS hamburger menu (`#mobile-menu-btn` / `#mobile-menu`)
- **Cards**: `bg-[#F7F7F8] dark:bg-[#2F2F2F] border border-[#E5E5E5] dark:border-[#3A3A3A] rounded-xl p-6`
- **Buttons**: Monochrome `bg-[#0D0D0D] dark:bg-[#ECECEC] text-white dark:text-[#0D0D0D] rounded-lg`, outline variant with border
- **Icons**: All inline SVGs (no icon fonts)
- **Footer**: Minimal single-line with subtle top border

## Adding New Content

### New Service Card
```html
<div class="bg-[#F7F7F8] dark:bg-[#2F2F2F] border border-[#E5E5E5] dark:border-[#3A3A3A] rounded-xl p-6">
  <div class="w-10 h-10 mb-4 text-[#0D0D0D] dark:text-[#ECECEC]">
    <!-- Inline SVG icon here -->
  </div>
  <h3 class="text-lg font-semibold mb-2">Service Name</h3>
  <p class="text-sm text-[#6B7280] dark:text-[#8E8EA0]">Service description</p>
</div>
```

### Navigation Links
Update all 5 pages when adding new pages. The navbar is duplicated across pages (no templating).

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
9. Verify all navigation links work across pages

## Deployment

Site deploys automatically to GitHub Pages from `main` branch. Domain configured via `CNAME` file.
