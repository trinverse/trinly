# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

Trinly is a static website for a technology consultancy company specializing in digital image processing, drone software, photogrammetry, and digital transformation services. The website is built using HTML, CSS, and JavaScript with Bootstrap framework and follows Material Design 3 principles.

**Company Focus Areas:**
- Digital Image Processing
- Drone Operations and Software
- Photogrammetry
- Process Analysis/Automation
- Digital Transformation
- Advanced Technologies Integration

## Quick Start

To run the website locally:

```bash
# Serve the website using Python 3
python3 -m http.server 8000

# Or using Python 2
python -m SimpleHTTPServer 8000

# Or using Node.js http-server (if installed)
npx http-server -p 8000

# Or using PHP (if installed)
php -S localhost:8000
```

Then open `http://localhost:8000` in your browser.

## Development Commands

Since this is a static website with no build process, there are no npm scripts or build commands. Development involves:

```bash
# View the website
open index.html

# Or serve locally and view
python3 -m http.server 8000 && open http://localhost:8000

# Check git status
git status

# Add changes
git add .

# Commit changes (following rule: don't use keywords that auto-close PRs)
git commit -m "Update website content"
```

## Architecture Overview

### File Structure
```
trinly/
├── index.html              # Main landing page
├── specialties.html        # Drone specialties page
├── CNAME                   # GitHub Pages domain configuration
├── .nojekyll              # GitHub Pages Jekyll bypass
└── assets/
    ├── css/
    │   ├── style.css       # Main stylesheet
    │   ├── material.css    # Material Design 3 theme
    │   └── colors/         # Color variations
    ├── js/
    │   ├── main.js         # Main JavaScript functionality
    │   └── plugins.js      # Plugin configurations
    ├── images/             # Image assets and favicons
    └── lib/                # Third-party libraries
```

### Page Architecture

**index.html** - Main landing page with sections:
- Hero section with animated background (chicago-night.gif)
- Services grid (12 service tiles)
- About section
- Contact information
- Navigation linking to specialties page

**specialties.html** - Drone-focused page:
- Hero section with drone animation (drones.gif)
- Four specialty areas with visual icons
- Same navigation and footer structure

### CSS Organization

- **style.css**: Core styles, layout, components, responsive design
- **material.css**: Material Design 3 color system and component styling
- **Third-party styles**: Bootstrap, Font Awesome, Animate.css, FlexSlider, Owl Carousel, Magnific Popup

### JavaScript Structure

- **main.js**: Page initialization, animations, scroll effects, navigation behavior
- **plugins.js**: Third-party library configurations
- **Libraries**: jQuery, Bootstrap, WOW.js, FlexSlider, Owl Carousel, Isotope, Magnific Popup, Simple Text Rotator

## Technology Stack

**Core Technologies:**
- HTML5 semantic markup
- CSS3 with Flexbox/Grid
- Vanilla JavaScript + jQuery
- Bootstrap 3.x framework
- Material Design 3 color system

**Key Libraries:**
- **jQuery** - DOM manipulation and AJAX
- **Bootstrap** - Responsive grid and components
- **WOW.js** - Scroll-triggered animations
- **Animate.css** - CSS animation library
- **FlexSlider** - Image/content slider
- **Owl Carousel** - Touch-friendly carousel
- **Magnific Popup** - Lightbox/modal functionality
- **Isotope** - Filtering and sorting layouts
- **Simple Text Rotator** - Text animation effects

**Fonts & Icons:**
- Google Fonts: Roboto, Roboto Condensed, Volkhov, Open Sans
- Font Awesome icons
- ET Line Font icons

## Development Guidelines

### Adding New Pages
1. Copy the structure from `index.html` or `specialties.html`
2. Maintain consistent navigation structure
3. Update navigation links in existing pages
4. Follow the same asset loading pattern (CSS and JS)
5. Use the same footer structure with updated copyright year

### Adding New Sections
1. Use Bootstrap's grid system (`col-md-*` classes)
2. Wrap sections in `.module` or `.module-small` containers
3. Follow the pattern: `.container > .row > .col-*`
4. Add appropriate `id` attributes for navigation anchors
5. Use consistent typography classes (`.font-alt`, `.module-title`)

### Styling Conventions
- Use Material Design 3 CSS variables from `material.css`
- Follow BEM-like naming: `.features-item`, `.features-icon`, `.features-title`
- Responsive breakpoints follow Bootstrap 3 standards
- Animation classes from Animate.css prefixed with `animated`

### Image Management
- Store images in `assets/images/` directory
- Use descriptive filenames
- Optimize images for web (consider file size)
- Maintain consistent aspect ratios for service icons
- Use `.specialties-image` class for drone page images (100% width, 200px height)

### JavaScript Patterns
- Initialize components in `$(document).ready()`
- Use jQuery for DOM manipulation
- Configure third-party plugins in appropriate sections
- Add smooth scrolling for anchor links
- Implement responsive behavior checks with `mobileTest`

## Adding New Features

### Service Cards
1. Add new `.col-md-3` div in the services grid
2. Use `.features-item` container class
3. Include `.features-icon` with appropriate icon
4. Add `.features-title` with service name
5. Include descriptive paragraph

### Animations
1. Add WOW.js classes: `wow fadeInUp`, `wow fadeInLeft`, etc.
2. Use Animate.css classes for CSS animations
3. Control scroll-triggered effects in `main.js`
4. Test on mobile (animations are disabled on mobile devices)

### Background Images/Videos
1. Add `data-background` attribute to section elements
2. Images are automatically applied via JavaScript in `main.js`
3. For videos, use appropriate video background plugins

## Material Design Implementation

The site uses Material Design 3 color tokens:
- Primary: `#6750A4` (purple)
- Background: `#FFFBFE` (neutral light)
- Surface variants for cards and components
- Proper contrast ratios maintained

Components styled with Material Design principles:
- Rounded corners (16px border-radius)
- Elevated surfaces with subtle shadows
- Color-coded interactive elements
- Typography scale following Material guidelines

## Deployment

The site is deployed to GitHub Pages:
- Repository: `trinverse/trinly`
- Domain: Configured via `CNAME` file
- Branch: `main` (auto-deploys on push)
- Static assets served directly

## Important Notes

- **No build process**: Direct HTML/CSS/JS editing
- **Mobile responsive**: Bootstrap grid + custom responsive styles
- **Cross-browser compatible**: Modern browser support with graceful degradation
- **SEO considerations**: Semantic HTML structure, meta tags, proper heading hierarchy
- **Performance**: Optimize images and minimize HTTP requests when adding new assets
- **Accessibility**: Maintain proper heading structure and alt attributes for images

## Git Workflow

Follow existing branch conventions:
- Work on `atyagi` branch (as per user rules)
- Don't use auto-closing keywords in commit messages
- Test locally before pushing to avoid breaking GitHub Pages deployment
