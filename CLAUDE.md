# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Trinly is a static website for a technology consultancy specializing in digital image processing, drone operations, photogrammetry, and digital transformation services. Built with HTML, CSS, JavaScript, Bootstrap 3, and Material Design 3 principles.

## Development Commands

### Local Development Server
```bash
# Python 3
python3 -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000

# Node.js (if http-server installed)
npx http-server -p 8000

# PHP (if installed)
php -S localhost:8000
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
- `index.html` - Main landing page with services, about, contact sections
- `specialties.html` - Drone specialties page
- `portfolio.html` - Portfolio page
- `team.html` - Team page
- `sms-consent.html` - SMS opt-in consent proof page for Twilio compliance (TCPA/CTIA)
- `assets/css/style.css` - Core styles and responsive design
- `assets/css/material.css` - Material Design 3 theme
- `assets/js/main.js` - Page initialization, animations, navigation
- `assets/lib/` - Third-party libraries (jQuery, Bootstrap, etc.)

### Key Libraries
- **Bootstrap 3.x** - Responsive grid system
- **jQuery** - DOM manipulation
- **WOW.js** - Scroll animations
- **Animate.css** - CSS animations
- **FlexSlider/Owl Carousel** - Content sliders
- **Magnific Popup** - Lightbox modals
- **Isotope** - Portfolio filtering

### CSS Classes & Patterns
- Module containers: `.module`, `.module-small`
- Grid: Bootstrap's `.container > .row > .col-md-*`
- Typography: `.font-alt`, `.module-title`, `.module-subtitle`
- Features: `.features-item`, `.features-icon`, `.features-title`
- Animations: `wow fadeInUp`, `wow fadeInLeft` (WOW.js)

### Material Design Colors
- Primary: `#6750A4`
- Background: `#FFFBFE`
- Surface variants for cards
- 16px border-radius for components

## Adding New Content

### New Service Card
```html
<div class="col-md-3 col-sm-6 col-xs-12">
  <div class="features-item">
    <div class="features-icon"><span class="icon-search"></span></div>
    <h3 class="features-title font-alt">Service Name</h3>
    <p>Service description</p>
  </div>
</div>
```

### Background Images
Add `data-background="path/to/image.jpg"` to section elements. JavaScript in `main.js` handles application.

### Navigation Links
Update all pages when adding new pages. Maintain consistent structure across `index.html`, `specialties.html`, `portfolio.html`, `team.html`, and `sms-consent.html`.

## Testing & Validation

Since this is a static site with no build process:
1. Test locally using development server
2. Check responsive behavior at different breakpoints
3. Verify navigation links work
4. Test animations and interactive elements
5. Validate HTML structure

## Deployment

Site deploys automatically to GitHub Pages from `main` branch. Domain configured via `CNAME` file.