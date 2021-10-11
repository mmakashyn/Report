# Changelog

## Changes introduced by GK

### PR 1
* added .gitignore
* model modification: in ```content.py```, changed model ```LinkBlock(blocks.StructBlock)```, 
replacing id with ```other_link``` and adding ```page_link```. This resulted in migration #0002, included in the commit.
* temporary fix for frontpage image height on mobile 100vh -> 70vh (see below, needs better fix)
* added templates/snippets/navbar.html - a placeholder template snippet which will be automatically overriden
by our own navbar
* base.css - changed body to .report-content - see comment below
* removed subpage_types in ReportPage model to allow our other page types under the Report page.

### PR 2
* Executive summary block - wrong assignment, Title should be Text, Description - RichText; was reverse.
* Removed ActionCallLinkBlock from use, replaced with LinkBlock - 
it became useless after I modified LinkBlock to include both Page and URL link fields.


## Comments and requests for changes:

* Frontpage:
  * navbar was missing, added a placeholder snippet. Please adjust all other styles - e.g. right now the bg image 
  is too long, beyond bottom of the page, and thus buttons on front page are too low.
  * Could you modify the style of the buttons on the frontpage in such way, that if there are <4 present,
    (that is, just one row), that row is top-aligned rather than bottom-aligned?
  * the whole button should be a link, not just a text on the button 
  (maybe using bootstrap's .stretched-link class will require least amount of changes?) 
  * In mobile view (very narrow browser window) - none of the buttons are visible. I have
  implemented a temporary workaround by setting image height to 70 rather than 100vh.
  * the css is overriding some global properties - it is a big problem for us, as we intend to integrate the "report"
  app with the rest of the website, and conflicts will arise. 
  My temporary fix is to change base.css (body->.report-content)