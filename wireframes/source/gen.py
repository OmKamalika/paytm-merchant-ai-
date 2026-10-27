import os
OUT=os.path.dirname(os.path.abspath(__file__))+"/html/"
os.makedirs(OUT,exist_ok=True)

CSS="""
*{box-sizing:border-box;margin:0;padding:0}
body{background:transparent;font-family:'Inter','Noto Sans','DejaVu Sans',Arial,sans-serif;color:#1A1A1A;font-size:13px;line-height:1.35}
.bezel{width:388px;height:828px;background:#101828;border-radius:40px;padding:14px;margin:0}
.phone{width:360px;height:800px;background:#F4F6F9;border-radius:28px;overflow:hidden;position:relative}
.status{height:24px;background:#002E6E;color:#fff;font-size:11px;display:flex;justify-content:space-between;align-items:center;padding:0 16px}
.appbar{background:#002E6E;color:#fff;padding:8px 14px 12px;display:flex;align-items:center;gap:10px}
.appbar .back{font-size:18px;opacity:.9}
.appbar .t{font-size:15px;font-weight:700}
.appbar .s{font-size:11px;opacity:.8}
.logo{width:34px;height:34px;border:1.5px dashed #9FB4D6;border-radius:8px;font-size:8px;color:#9FB4D6;display:flex;align-items:center;justify-content:center;text-align:center}
.body{padding:0 0 70px 0}
.card{background:#fff;border-radius:12px;margin:8px 12px;padding:11px 12px;box-shadow:0 1px 2px rgba(16,24,40,.06)}
.card h4{font-size:10.5px;letter-spacing:.06em;color:#6B7280;text-transform:uppercase;margin-bottom:7px}
.row{display:flex;justify-content:space-between;align-items:center;gap:8px}
.big{font-size:22px;font-weight:800;color:#002E6E}
.muted{color:#6B7280}
.small{font-size:11px}
.chip{display:inline-block;border-radius:99px;padding:3px 9px;font-size:11px;background:#E6F7FD;color:#00749A;margin:2px 3px 2px 0;font-weight:600}
.chip.g{background:#DCFCE7;color:#166534}.chip.a{background:#FEF3C7;color:#92400E}.chip.r{background:#FEE2E2;color:#991B1B}.chip.n{background:#E5E9F0;color:#374151}
.btn{display:inline-block;border-radius:8px;padding:8px 12px;font-weight:700;font-size:12.5px;background:#00BAF2;color:#fff;text-align:center}
.btn.sec{background:#fff;color:#00749A;border:1.2px solid #00BAF2}
.btn.full{display:block;margin:8px 12px;padding:11px}
.btn.dark{background:#002E6E}
.btn.red{background:#fff;color:#B91C1C;border:1.2px solid #FCA5A5}
.alert{display:flex;gap:8px;padding:8px 0;border-top:1px solid #EEF1F6}
.alert:first-of-type{border-top:0}
.dot{width:9px;height:9px;border-radius:50%;margin-top:4px;flex:none}
.dot.a{background:#F59E0B}.dot.b{background:#00BAF2}.dot.g{background:#16A34A}.dot.r{background:#DC2626}
.mic{margin:8px 12px;background:#fff;border:1.2px solid #00BAF2;border-radius:99px;padding:10px 14px;color:#00749A;font-weight:700;display:flex;gap:8px;align-items:center}
.tabbar{position:absolute;bottom:0;left:0;right:0;height:56px;background:#fff;border-top:1px solid #E5E9F0;display:flex;justify-content:space-around;align-items:center;font-size:10.5px;color:#6B7280}
.tabbar div{text-align:center}.tabbar .ic{width:18px;height:18px;border-radius:5px;background:#CBD5E1;margin:0 auto 3px}
.tabbar .on{color:#00749A;font-weight:700}.tabbar .on .ic{background:#00BAF2}
.bub{border-radius:14px;padding:9px 11px;margin:8px 12px;max-width:290px}
.bub.u{background:#E6F7FD;margin-left:auto;color:#00526E}
.bub.m{background:#fff;box-shadow:0 1px 2px rgba(16,24,40,.06)}
table.t{width:100%;border-collapse:collapse;font-size:11.5px}
table.t td,table.t th{padding:5px 3px;text-align:right;border-bottom:1px solid #EEF1F6}
table.t td:first-child,table.t th:first-child{text-align:left;color:#374151}
table.t th{font-size:10.5px;color:#6B7280;text-transform:uppercase;font-weight:700}
.neg{color:#DC2626;font-weight:700}
.bar{height:10px;border-radius:5px;background:#E5E9F0;overflow:hidden}.bar i{display:block;height:100%;background:#00BAF2}
.ok{color:#16A34A;font-weight:700}
.sep{height:1px;background:#EEF1F6;margin:8px 0}
.lbl{display:flex;justify-content:space-between;padding:3px 0;font-size:12px}
.lbl b{font-weight:700}
.shield{display:inline-block;background:#00BAF2;color:#fff;border-radius:6px;padding:1px 6px;font-size:10px;font-weight:700;margin-left:6px}
.photo{width:62px;height:62px;background:repeating-linear-gradient(45deg,#E5E9F0,#E5E9F0 6px,#D6DCE6 6px,#D6DCE6 12px);border-radius:8px;border:1px solid #CBD5E1}
"""

def tabbar(active):
    items=["Home","Outlets","Munim","Capital","More"]
    h="".join(f'<div class="{"on" if i==active else ""}"><div class="ic"></div>{i}</div>' for i in items)
    return f'<div class="tabbar">{h}</div>'

def page(fname,title,body,sub=None,back=True,tab="Munim",logo=False,statusbar=True):
    left=('<div class="logo">brand logo</div>' if logo else ('<span class="back">&#8249;</span>' if back else ''))
    subh=f'<div class="s">{sub}</div>' if sub else ''
    tb=tabbar(tab) if tab else ''
    html=f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="bezel"><div class="phone"><div class="status"><span>9:41</span><span>4G &#9679;&#9679;&#9679;&#9679; 78%</span></div>
<div class="appbar">{left}<div><div class="t">{title}</div>{subh}</div></div>
<div class="body">{body}</div>{tb}</div></div></body></html>"""
    open(OUT+fname+".html","w",encoding="utf-8").write(html)

# ---------- 1 HOME (W1)
page("01_home","Sharma General Stores","""
<div class="card"><div class="row"><h4>Today on Paytm · till 7 pm</h4></div>
<div class="big">&#8377;10,140</div>
<div style="margin-top:6px"><span class="chip">Dadar &#8377;4,980</span><span class="chip">Matunga &#8377;3,120</span><span class="chip">Sion &#8377;2,040</span></div></div>
<div class="card"><h4>AI Munim</h4>
<div class="alert"><div class="dot a"></div><div style="flex:1"><b>Cash runs &#8377;1.8 lakh short on 5 Nov</b><div class="small muted">Diwali stock-up, rent</div></div><span class="chip">See plan</span></div>
<div class="alert"><div class="dot a"></div><div style="flex:1"><b>Matunga, Thursday evenings</b><div class="small muted">Below expected 3 times in 4 weeks</div></div><span class="chip">Check</span></div>
<div class="alert"><div class="dot b"></div><div style="flex:1"><b>October: Sion lost &#8377;6,200</b><div class="small muted">Dadar and Matunga carry it</div></div><span class="chip">Why</span></div></div>
<div class="card"><div class="row"><div><h4>Capital</h4><b>3 pre-approved lines</b><div class="small muted">up to &#8377;5 lakh</div></div><span class="btn">Open</span></div></div>
<div class="card"><h4>October profit by outlet</h4>
<div class="lbl"><span>Dadar</span><b>&#8377;37.4K</b></div><div class="bar"><i style="width:100%"></i></div>
<div class="lbl"><span>Matunga</span><b>&#8377;23.9K</b></div><div class="bar"><i style="width:64%"></i></div>
<div class="lbl"><span>Sion</span><b class="neg">&minus;&#8377;6.2K</b></div><div class="bar"><i style="width:8%;background:#DC2626"></i></div></div>
<div class="mic"><span style="font-size:16px">&#127908;</span> Ask your Munim, Hindi or English</div>
""",sub="3 outlets",back=False,tab="Home",logo=True)

# ---------- 2 CONSENT (W2)
page("02_consent","Connect your data","""
<div class="card"><h4>Consent 1 · for your Munim</h4>
<div class="lbl"><span class="muted">Receiver</span><b>Paytm Payments Services (FIU)</b></div>
<div class="lbl"><span class="muted">Through</span><b>your Account Aggregator</b></div>
<div class="lbl"><span class="muted">Data</span><b>Bank a/c &middot;&middot;4521, GSTR-1, GSTR-3B</b></div>
<div class="lbl"><span class="muted">Purpose</span><b>Reporting for you</b></div>
<div class="lbl"><span class="muted">Fetch</span><b>Bank daily · GST monthly</b></div>
<div class="lbl"><span class="muted">Valid</span><b>12 months, stop any time</b></div>
<div class="btn full" style="margin:10px 0 2px">Approve on your AA app</div></div>
<div class="card" style="opacity:.8"><h4>Consent 2 · only if you use Capital</h4>
<div class="small muted">Each lender asks you separately, for its own underwriting. Lenders see your Paytm collections only if you say yes.</div></div>
<div class="card"><div class="small"><b>No GSTR-1 or 3B?</b> (composition scheme) The Munim works without GST data.</div></div>
<div class="card"><div class="small muted">Stop sharing any time: More &rsaquo; Consents</div></div>
""",sub="One time",tab=None)

# ---------- 3 MANDATE (W3)
page("03_mandate","Your rules","""
<div class="card"><h4>Who can do what <span class="shield">Intent Guard</span></h4>
<div class="lbl"><span><b>Cashier</b><div class="small muted">payments, check, refund up to &#8377;500, close shift</div></span><span class="chip n">&#8377;2,000/day</span></div>
<div class="lbl"><span><b>Manager</b><div class="small muted">refunds up to &#8377;5,000</div></span></div>
<div class="lbl"><span><b>You</b><div class="small muted">everything else</div></span></div></div>
<div class="card"><h4>Money rules</h4>
<div class="lbl"><span>Approved suppliers</span><span><b>6</b> <span class="chip">edit</span></span></div>
<div class="lbl"><span>Approved lenders</span><span><b>3</b> <span class="chip">edit</span></span></div>
<div class="sep"></div>
<div class="small">Credit cap: all EMIs &le; 8% of daily collections</div>
<div class="bar" style="margin:6px 0 3px"><i style="width:60%"></i></div><div class="small muted">&#8377;1.52 lakh a month today</div></div>
<div class="card"><h4>Always ask me for</h4>
<span class="chip a">New payee</span><span class="chip a">Changed bank account</span><span class="chip a">Drawdowns above &#8377;50,000</span><span class="chip a">Refunds above &#8377;5,000</span></div>
<div class="mic"><span>&#127908;</span> "Sion ka refund limit 300 karo"</div>
<div class="btn full">Save rules</div>
""",sub="Only you can change these",tab=None)

# ---------- 4 ASK (W4)
page("04_ask_diwali","Munim","""
<div class="bub u"><div class="small muted">You &middot; 30 Oct, 7:12 pm &#127908;</div>"Diwali ke liye kitna maal uthaun, aur paisa kahan se aayega?"</div>
<div class="bub m"><div class="small muted">Munim &middot; speaks Hindi, shows English &#128266;</div>
Last Diwali week sold <b>1.8x</b> a normal week at Dadar and <b>1.5x</b> at Matunga and Sion. Buy <b>&#8377;9.6 lakh</b> of stock by 4 Nov.
<div style="margin-top:6px">Cash runs <b class="neg">&#8377;1.8 lakh short on 5 Nov</b> and is back above zero on 7 Nov.</div></div>
<div class="card"><h4>Three ways to cover 5 Nov</h4>
<div class="alert"><div class="chip">1</div><div style="flex:1"><b>Ask Gupta for 15 days on &#8377;2 lakh</b><div class="small muted">Cost &#8377;0 if he agrees</div></div><span class="chip">Draft msg</span></div>
<div class="alert"><div class="chip">2</div><div style="flex:1"><b>Draw &#8377;2 lakh on 4 Nov, repay by 30 Nov</b><div class="small muted">about &#8377;2,600 interest</div></div></div>
<div class="alert"><div class="chip">3</div><div style="flex:1"><b>Buy &#8377;1.8 lakh less</b><div class="small muted">risks about &#8377;27,000 of Diwali margin</div></div></div></div>
<div class="btn full">See the 90-day plan</div>
<div class="mic"><span>&#127908;</span> Ask a follow-up</div>
""",tab="Munim")

# ---------- 5 CASH PLAN (W5)
pts=[(0,4.5),(2,1.2),(5,-1.5),(6,-1.8),(8,0.6),(10,1.4),(12,2.0)]
def X(d):return 20+d*(320/12)
def Y(v):return 70-v*14   # zero line at y=70... value range -2..5
poly=" ".join(f"{X(d):.0f},{Y(v):.0f}" for d,v in pts)
area=f"{X(5):.0f},{Y(0):.0f} "+" ".join(f"{X(d):.0f},{Y(v):.0f}" for d,v in [(5,-1.5),(6,-1.8),(7,-0.6)])+f" {X(7):.0f},{Y(0):.0f}"
svg=f"""<svg width="316" height="130" viewBox="0 0 360 130" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="{Y(0)}" x2="340" y2="{Y(0)}" stroke="#CBD5E1" stroke-dasharray="3 3"/>
<polygon points="{X(4.4):.0f},{Y(0):.0f} {X(5):.0f},{Y(-1.5):.0f} {X(6):.0f},{Y(-1.8):.0f} {X(7.2):.0f},{Y(-0.4):.0f} {X(7.6):.0f},{Y(0):.0f}" fill="#FEE2E2"/>
<polyline points="{poly}" fill="none" stroke="#00BAF2" stroke-width="3" stroke-linejoin="round"/>
<circle cx="{X(6):.0f}" cy="{Y(-1.8):.0f}" r="5" fill="#DC2626"/>
<text x="{X(2.2):.0f}" y="{Y(-1.8)+16:.0f}" font-size="10" fill="#DC2626" font-weight="700">Lowest -&#8377;1.8L on 5 Nov</text>
<line x1="{X(8):.0f}" y1="10" x2="{X(8):.0f}" y2="120" stroke="#F59E0B" stroke-dasharray="3 3"/>
<text x="{X(8)+3:.0f}" y="18" font-size="10" fill="#92400E">Diwali 8 Nov</text>
<text x="20" y="126" font-size="9" fill="#6B7280">30 Oct</text><text x="{X(12)-18:.0f}" y="126" font-size="9" fill="#6B7280">11 Nov</text></svg>"""
page("05_cash_plan","Cash plan","""
<div class="card"><h4>Combined cash and bank · next 90 days</h4>"""+svg+"""
<div class="small muted">Showing first 2 weeks. 90-day view on tap.</div></div>
<div class="card"><h4>Coming up</h4>
<table class="t">
<tr><td>31 Oct &middot; Patel Traders</td><td class="neg">&minus;&#8377;2,90,000</td></tr>
<tr><td>1 Nov &middot; Salaries, 7 staff</td><td class="neg">&minus;&#8377;1,05,000</td></tr>
<tr><td>1 Nov &middot; Mehta Dry Fruits</td><td class="neg">&minus;&#8377;1,50,000</td></tr>
<tr><td>4 Nov &middot; Gupta Distributors</td><td class="neg">&minus;&#8377;5,20,000</td></tr>
<tr><td>5 Nov &middot; Rent, 3 outlets</td><td class="neg">&minus;&#8377;1,07,000</td></tr>
<tr><td>5 Nov &middot; Diwali bonus</td><td class="neg">&minus;&#8377;52,500</td></tr>
<tr><td>20 Nov &middot; GST for October</td><td class="neg">&minus;&#8377;42,000</td></tr>
<tr><td>Jan &middot; UPI charges above &#8377;2,000</td><td class="muted">about &minus;&#8377;650/mo</td></tr></table></div>
<div class="card" style="background:#FEF3C7"><div class="row"><b>5 Nov gap: 3 ways to cover it</b><span class="btn">Open</span></div></div>
<div class="card"><div class="small muted">Assumes Diwali week sells like last year's: 1.8x at Dadar, 1.5x elsewhere.</div><span class="chip">Change this</span></div>
""",tab="Munim")

# ---------- 6 CAPITAL OFFERS (W6)
def offer(name,typ,line,apr,emi,pen):
    return f"""<div class="card"><div class="row"><b>{name} &middot; {typ}</b><span class="chip n">APR {apr}</span></div>
<div class="small muted">Line &#8377;{line}</div><div class="small">{emi}</div><div class="small muted">Penal charge: {pen} a year on overdue</div>
<div class="row" style="margin-top:7px"><span class="chip">Key facts (KFS)</span><span class="btn">Choose</span></div></div>"""
page("06_capital_offers","Capital &middot; &#8377;2,00,000 on 4 Nov","""
<div class="card" style="background:#E6F7FD"><div class="small">For <b>Gupta Distributors</b>, invoice GD-1182. Paid straight to Gupta's verified account.</div></div>
<div class="small muted" style="margin:6px 14px 0">All matching offers &middot; sorted by APR, lowest first</div>"""
+offer("Lender A","bank","3,00,000","18.5%","&#8377;2 lakh over 3 months: &#8377;68,730/month","2%")
+offer("Lender B","NBFC","2,50,000","22.0%","&#8377;2 lakh over 3 months: &#8377;69,130/month","3%")
+offer("Lender C","NBFC","5,00,000","26.5%","&#8377;2 lakh over 6 months: &#8377;35,960/month","4%")+"""
<div class="card"><div class="small"><b>Didn't match:</b> Lender D (minimum &#8377;5 lakh) &middot; Lender E (needs 24 months of GST filings)</div></div>
<div class="small muted" style="margin:4px 14px">Paytm isn't the lender and charges you nothing. You repay the lender directly by UPI AutoPay. Open to every Paytm merchant.</div>
""",tab="Capital")

# ---------- 7 GUARD (W7)
page("07_intent_guard","Intent Guard &middot; Before paying","""
<div class="card"><h4>Drawdown &#8377;2,00,000 &middot; Lender A</h4>
<div class="lbl"><span class="muted">Pay to</span><b>Gupta Distributors</b></div>
<div class="lbl"><span class="muted">For</span><b>invoice GD-1182 (&#8377;5,20,000)</b></div></div>
<div class="card"><div class="row"><h4>Rules</h4><span class="chip g">5 of 5</span></div>
<div class="small"><span class="ok">&#10003;</span> Lender A is on your list</div>
<div class="small"><span class="ok">&#10003;</span> Gupta's bank account unchanged since Mar 2024</div>
<div class="small"><span class="ok">&#10003;</span> Matches the invoice, no duplicate</div>
<div class="small"><span class="ok">&#10003;</span> EMIs after this &#8377;90,730, under your cap of &#8377;1.52 lakh</div>
<div class="small"><span class="ok">&#10003;</span> Inside your Diwali stock budget</div></div>
<div class="card"><h4>AI check &middot; can stop, never approve</h4>
<div class="small"><span class="ok">&#10003;</span> Matches the plan you asked for on 30 Oct. Nothing to escalate.</div></div>
<div class="card" style="background:#FEF3C7"><b>Needs you</b><div class="small">Drawdowns above &#8377;50,000 always need your PIN.</div></div>
<div class="btn full">Approve with PIN</div>
<div class="btn full sec" style="margin-top:0">Not now</div>
<div class="small muted" style="margin:2px 14px">Saved to evidence pack EP-2611</div>
""",tab=None,sub="Rules, then AI check, then you")

# ---------- 8 SHIFT CHECK (W8)
page("08_shift_check","Shift check &middot; Matunga","""
<div class="card"><h4>Thu 29 Oct &middot; evening, 3 pm to 10 pm</h4>
<div class="lbl"><span class="muted">Expected (your last 12 weeks)</span><b>&#8377;16,900 to &#8377;18,300</b></div>
<div class="lbl"><span class="muted">Collected</span><b>&#8377;14,470</b></div>
<div class="small muted" style="margin-left:8px">Paytm (exact) &#8377;4,120 &middot; Other QRs (entered) &#8377;6,350 &middot; Cash (counted) &#8377;4,000</div>
<div class="sep"></div><div class="row"><b class="neg">Below expected</b><b class="neg">&#8377;2,430 to &#8377;3,830</b></div></div>
<div class="card" style="background:#DCFCE7"><div class="small"><span class="ok">&#10003;</span> Bank data this morning matches the other-QR totals of all 3 outlets</div></div>
<div class="card"><h4>Pattern</h4><div class="small">3 of the last 4 Thursday evenings ran below expected. The other 53 shifts were within range.</div>
<div style="margin-top:6px;letter-spacing:4px"><span style="color:#16A34A">&#9679;&#9679;&#9679;</span><span style="color:#F59E0B">&#9679;</span> <span style="color:#16A34A">&#9679;&#9679;&#9679;</span><span style="color:#F59E0B">&#9679;</span> <span style="color:#16A34A">&#9679;&#9679;&#9679;</span><span style="color:#F59E0B">&#9679;</span> <span style="color:#16A34A">&#9679;&#9679;&#9679;&#9679;</span></div></div>
<div class="card"><h4>High-value shelf &middot; dry fruits</h4><div class="row"><div class="small">9 packs moved between 3 pm and 10 pm</div><div style="display:flex;gap:6px"><div class="photo"></div><div class="photo"></div></div></div></div>
<div class="card"><div class="small muted">Patterns by shift, never by person. Know why? Mark it:</div>
<span class="chip">Given on credit</span><span class="chip">Damaged</span><span class="chip">Moved to another outlet</span><span class="chip">Talk to the manager</span></div>
""",tab="Outlets")

# ---------- 9 CASHIER CLOSE SHIFT (F1)
page("09_cashier_close_shift","Sion counter &middot; Cashier","""
<div class="card"><h4>Today on Paytm</h4><div class="row"><div class="big">&#8377;2,040</div><span class="muted">31 payments</span></div></div>
<div style="margin:8px 12px;display:grid;grid-template-columns:1fr 1fr;gap:8px">
<div class="btn sec" style="padding:12px 6px">Create payment request</div><div class="btn sec" style="padding:12px 6px">Check a payment landed</div>
<div class="btn sec" style="padding:12px 6px">Refund (up to &#8377;500)</div><div class="btn" style="padding:12px 6px">Close my shift</div></div>
<div class="card"><h4>Close shift &middot; 4 steps</h4>
<div class="alert"><span class="chip g">1</span><div style="flex:1"><b>Count cash</b></div><b>&#8377;3,100</b></div>
<div class="alert"><span class="chip g">2</span><div style="flex:1"><b>Cash expenses</b><div class="small muted">chai &#8377;400, auto &#8377;250 &#127908;</div></div><b>&#8377;650</b></div>
<div class="alert"><span class="chip g">3</span><div style="flex:1"><b>Other QRs</b><div class="small muted">QR 2 &#8377;2,450 &middot; QR 3 &#8377;1,180</div></div></div>
<div class="alert"><span class="chip a">4</span><div style="flex:1"><b>Photograph 2 shelves</b><div class="small muted">dry fruits, personal care</div></div><span class="chip">1 of 2</span></div>
<div class="btn full" style="margin:8px 0 0">Hand over to the next shift</div></div>
<div class="small muted" style="margin:4px 14px">You can't see other outlets, profit or settings.</div>
""",sub="Restricted staff view",tab=None,back=False)

# ---------- 10 VOICE EXPENSE (W17b)
page("10_voice_expense","Check what I heard","""
<div class="bub u"><div class="small muted">&#127908; You said</div>"Chai-paani 400, auto 250, bijli ka bill 1,800"</div>
<div class="card"><h4>Expenses</h4>
<table class="t"><tr><td>Chai-paani</td><td>&#8377;400</td><td><span class="chip n">Sion</span></td></tr>
<tr><td>Transport</td><td>&#8377;250</td><td><span class="chip n">Sion</span></td></tr>
<tr><td>Electricity</td><td>&#8377;1,800</td><td><span class="chip a">which outlet?</span></td></tr></table>
<div style="margin-top:6px"><span class="chip">Dadar</span><span class="chip">Matunga</span><span class="chip">Sion</span><span class="chip">Split</span></div></div>
<div class="card"><div class="row"><b>Total &#8377;2,450</b><span class="muted small">paid from cash</span></div>
<div class="sep"></div><div class="small">Paid from the till, or from your pocket?</div>
<div style="margin-top:4px"><span class="chip g">&#9679; Till</span><span class="chip n">&#9675; My pocket</span></div></div>
<div class="card" style="background:#E6F7FD"><div class="small">Cash the shift check expects goes from <b>&#8377;14,200</b> to <b>&#8377;11,750</b></div></div>
<div class="btn full">Save</div><div class="btn full sec" style="margin-top:0">Say it again</div>
""",sub="Check before saving",tab=None)

# ---------- 11 COST RULES (W18a)
page("11_cost_rules","Your costs","""
<div class="small muted" style="margin:8px 14px 0">4 of 6 confirmed</div>
<div class="card"><h4>Found in your bank data</h4>
<b>&#8377;30,000 on the 5th to "R K Estates"</b><div class="small muted">Looks like: Rent</div>
<div style="margin:5px 0"><span class="chip">Dadar</span><span class="chip">Matunga</span><span class="chip g">Sion</span></div>
<span class="btn" style="padding:6px 10px">Yes, that's right</span> <span class="btn sec" style="padding:6px 10px">Not rent</span></div>
<div class="card"><b>&#8377;1,05,000 on the 1st, 7 transfers</b><div class="small muted">Looks like: Salaries, matched to your staff list</div>
<span class="btn" style="padding:6px 10px;margin-top:6px">Confirm by outlet</span></div>
<div class="card"><h4>Shared costs</h4><div class="lbl"><span>Electricity (one bill)</span><b>&#8377;5,400</b></div>
<div class="small">Split by <span class="chip g">&#9679; Sales</span><span class="chip n">Equal</span><span class="chip n">Custom</span></div>
<div class="small muted">Dadar 45% &middot; Matunga 30% &middot; Sion 25%</div></div>
<div class="card" style="background:#FEF3C7"><h4>What this changes</h4><div class="small">Sion's October profit: <b class="neg">&minus;&#8377;6,200</b></div></div>
<div class="mic"><span>&#127908;</span> "Dadar ka kiraya 45,000 karo"</div>
<div class="btn full">Save costs</div>
""",sub="You confirm, we never assume",tab="Outlets")

# ---------- 12 PROFIT BY OUTLET (W9)
page("12_profit_by_outlet","Profit by outlet &middot; October","""
<div class="card"><table class="t"><tr><th></th><th>Dadar</th><th>Matunga</th><th>Sion</th></tr>
<tr><td>Sales</td><td>&#8377;9.0L</td><td>&#8377;6.0L</td><td>&#8377;4.0L</td></tr>
<tr><td>Gross margin</td><td>&#8377;1.35L</td><td>&#8377;90K</td><td>&#8377;60K</td></tr>
<tr><td>Rent</td><td>&#8377;45K</td><td>&#8377;30K</td><td>&#8377;32K</td></tr>
<tr><td>Staff</td><td>&#8377;45K</td><td>&#8377;30K</td><td>&#8377;28K</td></tr>
<tr><td>Other</td><td>&#8377;7.6K</td><td>&#8377;6.1K</td><td>&#8377;6.2K</td></tr>
<tr><td><b>Profit</b></td><td><b>&#8377;37.4K</b></td><td><b>&#8377;23.9K</b></td><td class="neg">&minus;&#8377;6.2K</td></tr></table></div>
<div class="card"><h4>Why Sion loses money</h4>
<div class="small">&bull; Rent is 8% of sales (Dadar: 5%)</div><div class="small">&bull; Evening sales are down 14% since Aug</div><div class="small">&bull; Third loss-making month in a row</div></div>
<div class="card"><h4>How sure is this</h4>
<div class="lbl"><span>Paytm collections</span><span class="chip g">Exact</span></div>
<div class="lbl"><span>Other QRs and cash</span><span class="chip">Bank-checked</span></div>
<div class="lbl"><span>Rent and staff</span><span class="chip n">Your rules</span></div></div>
<div class="mic"><span>&#127908;</span> "Sion mein shaam ka ek staff kam karein toh kya hoga?"</div>
""",tab="Outlets")

# ---------- 13 PLAN & RECEIPT (W11)
page("13_plan_receipt","Your plan","""
<div class="card"><div class="row"><div><h4>Membership</h4><b>3 outlets &middot; first 5 included</b></div><div class="big">&#8377;199</div></div></div>
<div class="card"><h4>Passes and extras</h4>
<div class="lbl"><span>Shift-check pass &middot; 3 outlets</span><b>&#8377;297</b></div>
<div class="lbl"><span>CA pack</span><b>&#8377;99</b></div></div>
<div class="card" style="background:#E6F7FD"><div class="row"><b>Next charge</b><b>&#8377;595 + GST on 1 Dec</b></div>
<div class="small muted">By UPI AutoPay. We remind you here 2 days before. Price locked till Oct 2027. Cancel in one tap.</div></div>
<div class="card"><h4>October: what you paid, what it found</h4>
<div class="lbl"><span>You paid</span><b>&#8377;595</b></div>
<div class="lbl"><span>Shift shortfalls flagged</span><b>&#8377;7,300 to &#8377;11,500</b></div>
<div class="lbl"><span>Sion's monthly loss spotted</span><b>&#8377;6,200</b></div>
<div class="lbl"><span>Diwali cash gap planned</span><b>&#8377;1.8 lakh</b></div></div>
<div style="margin:8px 12px;display:flex;gap:8px"><span class="btn red">Cancel</span><span class="btn sec">Bill history</span><span class="btn sec">Help</span></div>
""",sub="Billed on its own line, not with the Soundbox",tab="More")
print("done")

# ---------- 14 SOUNDBOX shift close (F2)
sb=f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}
.stage{{width:388px;height:828px;background:transparent;display:flex;align-items:center;justify-content:center}}
.dev{{width:330px;background:#16233B;border-radius:34px 34px 22px 22px;padding:18px 16px 22px;color:#fff;box-shadow:0 12px 30px rgba(16,24,40,.35)}}
.top{{background:#0B1424;border-radius:10px;padding:8px 10px;font-size:12px;color:#7DD3FC;text-align:center;border:1px solid #28406B}}
.front{{background:#F4F6F9;color:#1A1A1A;border-radius:14px;margin-top:14px;padding:12px;min-height:330px}}
.spk{{margin:14px auto 0;width:150px;height:34px;background:repeating-linear-gradient(90deg,#2A3B5C 0 4px,#16233B 4px 9px);border-radius:8px}}
</style></head><body><div class="stage"><div class="dev">
<div class="top">Shift close due &middot; 10 pm &nbsp;&middot;&nbsp; step 2 of 4</div>
<div class="front">
<div class="small muted">AI Soundbox &middot; Sion counter</div>
<div class="row" style="margin:4px 0 8px"><b>Today on Paytm</b><b>&#8377;2,040 &middot; 31 payments</b></div>
<div class="card" style="margin:0 0 8px;background:#E6F7FD"><b>Aaj ka kharcha?</b><div class="small muted">Hold the button and speak</div>
<div style="margin-top:6px">&#127908; "Chai 400, auto 250"</div></div>
<div class="card" style="margin:0 0 8px"><div class="small muted">Heard</div><b>Chai &#8377;400 &middot; Auto &#8377;250</b>
<div class="row" style="margin-top:6px"><span class="small">Total &#8377;650 from the till</span><span><span class="btn" style="padding:5px 10px">Yes</span> <span class="btn sec" style="padding:5px 10px">No</span></span></div></div>
<div class="small muted">&#128266; Hindi: "Chhe sau pachaas ka kharcha. Theek hai?"</div>
<div class="small" style="margin-top:6px">Next: other QRs &rarr; shelf photos in the Business app</div></div>
<div class="spk"></div></div></div></body></html>"""
open(OUT+"14_soundbox_shift_close.html","w",encoding="utf-8").write(sb)
