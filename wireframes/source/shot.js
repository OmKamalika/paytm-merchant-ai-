const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 388, height: 828 }, deviceScaleFactor: 2 });
  fs.mkdirSync(__dirname + '/png', { recursive: true });
  for (const f of fs.readdirSync(__dirname + '/html').filter(x => x.endsWith('.html')).sort()) {
    const p = await ctx.newPage();
    await p.goto('file://' + __dirname + '/html/' + f);
    // overflow check: content bottom vs tab bar
    const over = await p.evaluate(() => { const bd = document.querySelector('.body'); const ph = document.querySelector('.phone'); return bd&&ph ? Math.round(bd.getBoundingClientRect().bottom - ph.getBoundingClientRect().bottom) : 0; });
    await p.locator('.bezel, .stage').first().screenshot({ omitBackground: true, path: __dirname + '/png/' + f.replace('.html', '.png') });
    console.log(f, 'body bottom beyond phone by', over, 'px');
    await p.close();
  }
  await b.close();
})();
