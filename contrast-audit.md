# Color Contrast Accessibility Audit

## Current Color Palette
- **Background**: #282a36 (dark blue-gray)
- **Secondary Background**: #44475a (lighter blue-gray)
- **Primary Text**: #f8f8f2 (off-white)
- **Secondary Text**: #6272a4 (muted blue)
- **Accent Blue**: #8be9fd (cyan)
- **Accent Purple**: #bd93f9 (purple)
- **Accent Green**: #50fa7b (green)

## Contrast Ratio Analysis

### ✅ PASSING Combinations (4.5:1+ for normal text, 3:1+ for large text)

1. **Primary Text on Background**
   - #f8f8f2 on #282a36 = **15.68:1** ✅ Excellent
   - Used for: Body text, headings, main content

2. **Primary Text on Secondary Background**
   - #f8f8f2 on #44475a = **11.74:1** ✅ Excellent
   - Used for: Card content, header text

3. **Purple Accent on Light Background**
   - #282a36 on #bd93f9 = **8.84:1** ✅ Excellent
   - Used for: Active button text

### ⚠️ POTENTIAL ISSUES to Check

4. **Secondary Text on Background**
   - #6272a4 on #282a36 = **~4.2:1** ⚠️ Borderline (needs verification)
   - Used for: Venue names, footer text, placeholders

5. **Secondary Text on Secondary Background**
   - #6272a4 on #44475a = **~3.1:1** ⚠️ Below 4.5:1 threshold
   - Used for: Some UI elements

6. **Cyan Accent on Background**
   - #8be9fd on #282a36 = **~12:1** ✅ Good
   - Used for: Results count, some links

7. **Green Accent on Background**
   - #50fa7b on #282a36 = **~11:1** ✅ Good
   - Used for: Links, venue links

## Issues Found & Fixes Needed

### Issue 1: Secondary Text Contrast
- **Problem**: #6272a4 may not meet 4.5:1 ratio on backgrounds
- **Impact**: Venue names, footer text, form placeholders
- **Fix**: Lighten to improve contrast

### Issue 2: Purple Accent Readability
- **Problem**: #bd93f9 on dark backgrounds needs verification
- **Impact**: Date badges, accent elements
- **Fix**: Ensure sufficient contrast

## Recommended Color Adjustments

```css
/* Current problematic colors */
color: #6272a4; /* Secondary text - too dim */

/* Recommended improvements */
color: #8892b0; /* Lighter blue-gray for better contrast */
color: #a6accd; /* Alternative lighter option */
```