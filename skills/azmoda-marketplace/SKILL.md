---
name: azmoda-marketplace
description: Build and operate the AZMODA marketplace end-to-end on WordPress/WooCommerce with Wildberries-level UX logic and AZMODA branding. Use when implementing or refining storefront flows (home, catalog, search, product page, favorites, cart, checkout, profile, order tracking, returns), responsive behavior (mobile/tablet/web), category architecture, and conversion-focused buyer journeys.
---

# AZMODA Marketplace Builder

Use this skill as the default implementation mode for the current project.

## Non-negotiable rules
- Keep AZMODA visual identity on every screen.
- Reuse WB logic patterns only for UX flow, not visual cloning.
- Build mobile-first, then tablet/web adaptations.
- Implement real click flows between pages; do not leave dead-end screens.
- After each block, provide short status: done / links / next block.

## Mandatory flow order
1. Catalog
2. Product page
3. Cart
4. Checkout
5. Order success
6. Profile orders + statuses
7. Returns/exchange

## Page requirements

### Home
- Search first, promo block, curated feed, tab bar.
- Distinct behavior for mobile vs desktop.

### Catalog
- Top categories and subcategories.
- Product grid with quick entry into product page.
- Filter/sort entry points.

### Product page
- Gallery hero, price + discount, size helper, delivery/returns block.
- Two CTAs: Buy now / Add to cart.

### Cart
- Editable quantities, promo code, delivery estimate, total.
- Direct transition to checkout.

### Checkout
- Minimal fields: customer, address, delivery, payment.
- Clear final amount and single confirmation action.

### Order success
- Order number, next steps, links to profile/home.

### Profile
- Orders list, order statuses, returns entry point.

## Technical implementation notes
- Use WordPress pages + WooCommerce logic for rapid rollout.
- Keep routes stable and human-readable.
- Ensure links between all core pages are working.
- Hide irrelevant default theme elements where they hurt UX.

## Working protocol
- Implement one production block at a time.
- Validate links manually after each update.
- Avoid repeated questions; proceed with best known requirements.
- If uncertain, prefer shipping a working flow over decorative changes.
