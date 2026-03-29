"""
Build a self-contained index.html explorer for the Trump Money Map data.
Usage: python scripts/build_html.py
Output: index.html (open in any browser, no server needed)
"""
import json
from pathlib import Path
from datetime import date

BASE = Path(__file__).parent.parent
INCIDENTS_FILE = BASE / "data" / "incidents.json"
PARDONS_FILE = BASE / "data" / "pardons.json"
OUTPUT = BASE / "index.html"

with open(INCIDENTS_FILE, encoding="utf-8") as f:
    idata = json.load(f)
with open(PARDONS_FILE, encoding="utf-8") as f:
    pdata = json.load(f)

incidents = idata["incidents"]
pardons = pdata["pardons"]

CATEGORY_LABELS = {
    "selling_access":      "Selling Access",
    "crypto_sales":        "Crypto Sales",
    "business_payment":    "Business Payments",
    "family_enrichment":   "Family Enrichment",
    "foreign_investment":  "Foreign Investment",
    "foreign_gift":        "Foreign Gifts",
    "insider_trading":     "Insider Trading",
    "market_manipulation": "Market Manipulation",
    "power_abuse":         "Power Abuse",
    "retaliation_targeting": "Retaliation/Targeting",
    "public_praise":       "Public Praise",
    "pardon_financial":    "Pardons (Financial)",
    "pardon_political":    "Pardons (Political)",
    "state_damages":       "State Damages",
    "arms_deal_conflict":  "Arms Deal Conflicts",
}

CATEGORY_COLORS = {
    "selling_access":        "#e74c3c",
    "crypto_sales":          "#9b59b6",
    "business_payment":      "#e67e22",
    "family_enrichment":     "#d35400",
    "foreign_investment":    "#c0392b",
    "foreign_gift":          "#8e44ad",
    "insider_trading":       "#2980b9",
    "market_manipulation":   "#16a085",
    "power_abuse":           "#c0392b",
    "retaliation_targeting": "#7f8c8d",
    "public_praise":         "#f39c12",
    "pardon_financial":      "#1abc9c",
    "pardon_political":      "#27ae60",
    "state_damages":         "#2c3e50",
    "arms_deal_conflict":    "#e74c3c",
}

incidents_json = json.dumps(incidents, ensure_ascii=False)
pardons_json = json.dumps(pardons, ensure_ascii=False)
category_labels_json = json.dumps(CATEGORY_LABELS, ensure_ascii=False)
category_colors_json = json.dumps(CATEGORY_COLORS, ensure_ascii=False)

total_fines = sum(p.get("fines_forgiven_usd") or 0 for p in pardons)
total_res = sum(p.get("restitution_forgiven_usd") or 0 for p in pardons)
total_pardons_dollars = total_fines + total_res
top_incident = max(incidents, key=lambda x: x.get("amount_usd") or 0)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Trump Money Map</title>
<style>
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

  :root {{
    --bg: #0f1117;
    --surface: #1a1d27;
    --surface2: #22263a;
    --border: #2e3350;
    --text: #e8eaf6;
    --text-dim: #8892b0;
    --accent: #e74c3c;
    --accent2: #3498db;
    --gold: #f1c40f;
    --green: #2ecc71;
    --orange: #e67e22;
    --purple: #9b59b6;
    --radius: 8px;
    --sidebar-w: 240px;
  }}

  body {{
    background: var(--bg);
    color: var(--text);
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
    font-size: 14px;
    display: flex;
    flex-direction: column;
    min-height: 100vh;
  }}

  /* ── Header ── */
  header {{
    background: var(--surface);
    border-bottom: 1px solid var(--border);
    padding: 16px 24px;
    display: flex;
    align-items: center;
    gap: 20px;
    position: sticky;
    top: 0;
    z-index: 100;
  }}
  header h1 {{
    font-size: 18px;
    font-weight: 700;
    color: var(--accent);
    letter-spacing: -0.3px;
  }}
  header h1 span {{ color: var(--text-dim); font-weight: 400; font-size: 13px; margin-left: 8px; }}
  .stats-bar {{
    display: flex;
    gap: 20px;
    margin-left: auto;
    flex-wrap: wrap;
  }}
  .stat {{
    text-align: right;
  }}
  .stat-val {{
    font-size: 15px;
    font-weight: 700;
    color: var(--gold);
  }}
  .stat-label {{
    font-size: 11px;
    color: var(--text-dim);
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}

  /* ── Layout ── */
  .app {{
    display: flex;
    flex: 1;
    overflow: hidden;
  }}

  /* ── Sidebar ── */
  nav {{
    width: var(--sidebar-w);
    background: var(--surface);
    border-right: 1px solid var(--border);
    overflow-y: auto;
    flex-shrink: 0;
    padding: 12px 0 24px;
  }}
  .nav-section {{
    padding: 12px 14px 4px;
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: var(--text-dim);
    font-weight: 600;
  }}
  .nav-btn {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    padding: 8px 14px;
    background: none;
    border: none;
    color: var(--text);
    font-size: 13px;
    cursor: pointer;
    text-align: left;
    border-left: 3px solid transparent;
    transition: background 0.15s, border-color 0.15s;
    gap: 6px;
  }}
  .nav-btn:hover {{ background: var(--surface2); }}
  .nav-btn.active {{
    background: var(--surface2);
    border-left-color: var(--accent);
    color: #fff;
    font-weight: 600;
  }}
  .nav-btn .dot {{
    width: 8px; height: 8px;
    border-radius: 50%;
    flex-shrink: 0;
  }}
  .nav-btn .count {{
    font-size: 11px;
    color: var(--text-dim);
    margin-left: auto;
    background: var(--surface2);
    padding: 1px 6px;
    border-radius: 10px;
  }}
  .nav-divider {{ height: 1px; background: var(--border); margin: 8px 0; }}

  /* ── Main content ── */
  main {{
    flex: 1;
    overflow: auto;
    padding: 20px 24px;
  }}

  .view-header {{
    display: flex;
    align-items: baseline;
    gap: 12px;
    margin-bottom: 16px;
    flex-wrap: wrap;
  }}
  .view-title {{
    font-size: 18px;
    font-weight: 700;
  }}
  .view-count {{
    color: var(--text-dim);
    font-size: 13px;
  }}
  .view-total {{
    margin-left: auto;
    font-size: 16px;
    font-weight: 700;
    color: var(--gold);
  }}

  /* Search */
  .search-bar {{
    display: flex;
    gap: 10px;
    margin-bottom: 14px;
    align-items: center;
  }}
  .search-bar input {{
    flex: 1;
    background: var(--surface);
    border: 1px solid var(--border);
    color: var(--text);
    padding: 8px 12px;
    border-radius: var(--radius);
    font-size: 13px;
    outline: none;
  }}
  .search-bar input:focus {{ border-color: var(--accent2); }}
  .search-bar input::placeholder {{ color: var(--text-dim); }}

  /* ── Table ── */
  .table-wrap {{
    overflow-x: auto;
    border-radius: var(--radius);
    border: 1px solid var(--border);
  }}
  table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
  }}
  thead th {{
    background: var(--surface2);
    padding: 10px 12px;
    text-align: left;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.6px;
    color: var(--text-dim);
    font-weight: 600;
    border-bottom: 1px solid var(--border);
    white-space: nowrap;
    cursor: pointer;
    user-select: none;
    position: sticky;
    top: 0;
    z-index: 2;
  }}
  thead th:hover {{ color: var(--text); }}
  thead th.sort-asc::after {{ content: " ▲"; color: var(--accent2); }}
  thead th.sort-desc::after {{ content: " ▼"; color: var(--accent2); }}

  tbody tr {{
    border-bottom: 1px solid var(--border);
    transition: background 0.1s;
    cursor: pointer;
  }}
  tbody tr:hover {{ background: var(--surface2); }}
  tbody tr.expanded {{ background: var(--surface2); }}

  td {{
    padding: 10px 12px;
    vertical-align: top;
    max-width: 0;
  }}

  .td-date {{ white-space: nowrap; color: var(--text-dim); font-size: 12px; width: 90px; }}
  .td-amount {{
    font-weight: 700;
    color: var(--gold);
    white-space: nowrap;
    text-align: right;
    width: 130px;
  }}
  .td-amount.zero {{ color: var(--text-dim); font-weight: normal; }}
  .td-who {{ font-weight: 500; }}
  .td-title {{ font-weight: 500; }}
  .td-title .title-text {{
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }}

  /* Expanded detail row */
  .detail-row td {{
    padding: 0;
    background: #12151f;
    border-bottom: 2px solid var(--accent);
  }}
  .detail-inner {{
    padding: 16px 20px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    font-size: 13px;
  }}
  .detail-inner.single {{ grid-template-columns: 1fr; }}
  .detail-block h4 {{
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: var(--text-dim);
    margin-bottom: 6px;
  }}
  .detail-block p {{ line-height: 1.6; color: var(--text); }}
  .source-list {{ list-style: none; }}
  .source-list li {{ margin-bottom: 4px; }}
  .source-list a {{
    color: var(--accent2);
    text-decoration: none;
    font-size: 12px;
  }}
  .source-list a:hover {{ text-decoration: underline; }}
  .source-meta {{
    color: var(--text-dim);
    font-size: 11px;
    margin-left: 4px;
  }}

  /* Badges */
  .badge {{
    display: inline-block;
    padding: 2px 7px;
    border-radius: 10px;
    font-size: 11px;
    font-weight: 600;
    margin: 1px 2px 1px 0;
    white-space: nowrap;
  }}
  .badge-status-confirmed  {{ background: #1a4a2e; color: #2ecc71; }}
  .badge-status-alleged    {{ background: #4a3000; color: #f1c40f; }}
  .badge-status-suspected  {{ background: #2d1a4a; color: #9b59b6; }}
  .badge-status-denied     {{ background: #3a1a1a; color: #e74c3c; }}

  .badge-owed-private {{ background: #4a2000; color: #e67e22; }}
  .badge-owed-govt    {{ background: #00294a; color: #3498db; }}
  .badge-owed-both    {{ background: #2a004a; color: #9b59b6; }}

  .badge-type-pardon      {{ background: #1a3a2a; color: #27ae60; }}
  .badge-type-commutation {{ background: #2a2a00; color: #f1c40f; }}
  .badge-type-mass_pardon {{ background: #3a0000; color: #e74c3c; }}

  .badge-fin-yes  {{ background: #3a0000; color: #e74c3c; font-weight: 700; }}
  .badge-fin-no   {{ background: #1a2a1a; color: #7f8c8d; }}
  .badge-pol-yes  {{ background: #2a1a00; color: #e67e22; }}

  .badge-qpq {{ background: #3a0000; color: #e74c3c; font-weight: 700; }}

  .cat-badge {{
    display: inline-block;
    padding: 2px 7px;
    border-radius: 10px;
    font-size: 11px;
    font-weight: 600;
    margin: 1px 2px 1px 0;
    color: #fff;
    white-space: nowrap;
  }}

  /* Beneficiary chips */
  .ben-chip {{
    display: inline-block;
    padding: 1px 6px;
    border-radius: 4px;
    font-size: 11px;
    background: var(--surface2);
    color: var(--text-dim);
    margin: 1px;
    white-space: nowrap;
    border: 1px solid var(--border);
  }}

  /* Pardon-specific */
  .td-forgiven {{ font-weight: 700; text-align: right; white-space: nowrap; }}
  .forgiven-total {{ color: var(--accent); }}
  .forgiven-part  {{ color: var(--text-dim); font-size: 12px; }}

  /* No results */
  .no-results {{
    text-align: center;
    padding: 40px;
    color: var(--text-dim);
    font-size: 15px;
  }}

  /* Scrollbar */
  ::-webkit-scrollbar {{ width: 6px; height: 6px; }}
  ::-webkit-scrollbar-track {{ background: var(--bg); }}
  ::-webkit-scrollbar-thumb {{ background: var(--border); border-radius: 3px; }}
  ::-webkit-scrollbar-thumb:hover {{ background: #4a5070; }}

  @media (max-width: 768px) {{
    nav {{ width: 180px; }}
    .detail-inner {{ grid-template-columns: 1fr; }}
  }}
</style>
</head>
<body>

<header>
  <div>
    <h1>Trump Money Map <span>— Second Presidency, Jan 2025–</span></h1>
  </div>
  <div class="stats-bar">
    <div class="stat">
      <div class="stat-val">{len(incidents)}</div>
      <div class="stat-label">Incidents</div>
    </div>
    <div class="stat">
      <div class="stat-val">{len(pardons)}</div>
      <div class="stat-label">Pardons</div>
    </div>
    <div class="stat">
      <div class="stat-val">${total_pardons_dollars/1e9:.2f}B</div>
      <div class="stat-label">Pardons Forgiven</div>
    </div>
    <div class="stat">
      <div class="stat-val" id="view-total-header"></div>
      <div class="stat-label">Current View</div>
    </div>
  </div>
</header>

<div class="app">
  <nav id="sidebar">
    <div class="nav-section">Incidents</div>
    <button class="nav-btn" onclick="showView('all-incidents')" id="btn-all-incidents">
      <span class="dot" style="background:#e74c3c"></span>
      All Incidents
      <span class="count">{len(incidents)}</span>
    </button>
    <!-- Category buttons injected by JS -->
    <div id="cat-buttons"></div>

    <div class="nav-divider"></div>
    <div class="nav-section">Pardons</div>
    <button class="nav-btn" onclick="showView('all-pardons')" id="btn-all-pardons">
      <span class="dot" style="background:#27ae60"></span>
      All Pardons
      <span class="count">{len(pardons)}</span>
    </button>
    <button class="nav-btn" onclick="showView('pardons-financial')" id="btn-pardons-financial">
      <span class="dot" style="background:#e74c3c"></span>
      Financial Connection
    </button>
    <button class="nav-btn" onclick="showView('pardons-political')" id="btn-pardons-political">
      <span class="dot" style="background:#e67e22"></span>
      Political Connection
    </button>
    <button class="nav-btn" onclick="showView('pardons-private-victims')" id="btn-pardons-private-victims">
      <span class="dot" style="background:#e67e22"></span>
      Victims = Private
    </button>
    <button class="nav-btn" onclick="showView('pardons-govt')" id="btn-pardons-govt">
      <span class="dot" style="background:#3498db"></span>
      Victims = Taxpayers
    </button>
  </nav>

  <main>
    <div class="view-header">
      <div class="view-title" id="view-title">All Incidents</div>
      <div class="view-count" id="view-count"></div>
      <div class="view-total" id="view-total"></div>
    </div>
    <div class="search-bar">
      <input type="text" id="search" placeholder="Search name, title, counterparty, offense…" oninput="applySearch()">
    </div>
    <div class="table-wrap">
      <div id="table-container"></div>
    </div>
  </main>
</div>

<script>
const INCIDENTS = {incidents_json};
const PARDONS = {pardons_json};
const CAT_LABELS = {category_labels_json};
const CAT_COLORS = {category_colors_json};

let currentView = 'all-incidents';
let currentData = [];
let currentType = 'incident'; // 'incident' | 'pardon'
let sortCol = null;
let sortDir = 'desc';
let searchTerm = '';
let expandedRow = null;

// ── Build sidebar category buttons ────────────────────────────────────────────
function buildSidebar() {{
  const counts = {{}};
  INCIDENTS.forEach(i => (i.categories || []).forEach(c => counts[c] = (counts[c]||0)+1));
  const div = document.getElementById('cat-buttons');
  Object.entries(CAT_LABELS).forEach(([code, label]) => {{
    if (!counts[code]) return;
    const btn = document.createElement('button');
    btn.className = 'nav-btn';
    btn.id = 'btn-cat-' + code;
    btn.innerHTML = `<span class="dot" style="background:${{CAT_COLORS[code]||'#888'}}"></span>
      ${{label}}<span class="count">${{counts[code]}}</span>`;
    btn.onclick = () => showView('cat-' + code);
    div.appendChild(btn);
  }});
}}

// ── Formatting helpers ────────────────────────────────────────────────────────
function fmt(n) {{
  if (!n && n !== 0) return '—';
  if (n >= 1e9) return '$' + (n/1e9).toFixed(2) + 'B';
  if (n >= 1e6) return '$' + (n/1e6).toFixed(1) + 'M';
  if (n >= 1e3) return '$' + (n/1e3).toFixed(0) + 'K';
  return '$' + n.toLocaleString();
}}
function fmtFull(n) {{
  if (!n && n !== 0) return '—';
  return '$' + n.toLocaleString('en-US');
}}
function statusBadge(s) {{
  return `<span class="badge badge-status-${{s||'confirmed'}}">${{(s||'').toUpperCase()}}</span>`;
}}
function catBadge(c) {{
  const col = CAT_COLORS[c] || '#888';
  return `<span class="cat-badge" style="background:${{col}}22;color:${{col}};border:1px solid ${{col}}44">${{CAT_LABELS[c]||c}}</span>`;
}}
function benChips(bens) {{
  return (bens||[]).map(b => `<span class="ben-chip">${{b}}</span>`).join('');
}}
function escape(s) {{
  if (!s) return '';
  return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}}

// ── Views ─────────────────────────────────────────────────────────────────────
function showView(view) {{
  currentView = view;
  expandedRow = null;
  searchTerm = document.getElementById('search').value = '';
  sortCol = null; sortDir = 'desc';

  // Set active button
  document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
  const btn = document.getElementById('btn-' + view.replace('cat-','cat-'));
  if (btn) btn.classList.add('active');

  if (view === 'all-incidents') {{
    currentType = 'incident';
    currentData = [...INCIDENTS];
    document.getElementById('view-title').textContent = 'All Incidents';
    renderIncidents(currentData);
  }} else if (view.startsWith('cat-')) {{
    const cat = view.replace('cat-','');
    currentType = 'incident';
    currentData = INCIDENTS.filter(i => (i.categories||[]).includes(cat));
    document.getElementById('view-title').textContent = CAT_LABELS[cat] || cat;
    renderIncidents(currentData);
  }} else if (view === 'all-pardons') {{
    currentType = 'pardon';
    currentData = [...PARDONS];
    document.getElementById('view-title').textContent = 'All Pardons & Commutations';
    renderPardons(currentData);
  }} else if (view === 'pardons-financial') {{
    currentType = 'pardon';
    currentData = PARDONS.filter(p => p.financial_connection && p.financial_connection.exists === true);
    document.getElementById('view-title').textContent = 'Pardons — Financial Connection to Trump';
    renderPardons(currentData);
  }} else if (view === 'pardons-political') {{
    currentType = 'pardon';
    currentData = PARDONS.filter(p => p.political_connection && p.political_connection.exists === true);
    document.getElementById('view-title').textContent = 'Pardons — Political Connection';
    renderPardons(currentData);
  }} else if (view === 'pardons-private-victims') {{
    currentType = 'pardon';
    currentData = PARDONS.filter(p => p.restitution_owed_to === 'private_victims');
    document.getElementById('view-title').textContent = 'Pardons — Restitution Owed to Private Victims';
    renderPardons(currentData);
  }} else if (view === 'pardons-govt') {{
    currentType = 'pardon';
    currentData = PARDONS.filter(p => p.restitution_owed_to === 'government' || p.restitution_owed_to === 'both');
    document.getElementById('view-title').textContent = 'Pardons — Restitution Owed to Taxpayers/Government';
    renderPardons(currentData);
  }}
}}

function applySearch() {{
  searchTerm = document.getElementById('search').value.toLowerCase();
  expandedRow = null;
  if (currentType === 'incident') renderIncidents(currentData);
  else renderPardons(currentData);
}}

function filterData(data) {{
  if (!searchTerm) return data;
  return data.filter(item => {{
    const searchable = [
      item.title, item.summary, item.name, item.offense,
      (item.counterparty||{{}}).name, item.notes,
      (item.actors||[]).join(' '),
      (item.tags||[]).join(' ')
    ].join(' ').toLowerCase();
    return searchable.includes(searchTerm);
  }});
}}

// ── Incident table ────────────────────────────────────────────────────────────
const INC_COLS = [
  {{ key:'date',       label:'Date',          sortable:true  }},
  {{ key:'counterparty',label:'Counterparty', sortable:true  }},
  {{ key:'title',      label:'Title',         sortable:false }},
  {{ key:'categories', label:'Categories',    sortable:false }},
  {{ key:'status',     label:'Status',        sortable:true  }},
  {{ key:'qpq',        label:'QPQ',           sortable:false }},
  {{ key:'beneficiary',label:'Benefits',      sortable:false }},
  {{ key:'amount_usd', label:'Amount ↕',      sortable:true  }},
];

function renderIncidents(data) {{
  const filtered = filterData(data);
  filtered.sort((a,b) => sortByCol(a, b, sortCol || 'amount_usd', sortDir));

  const total = filtered.reduce((s,i) => s + (i.amount_usd||0), 0);
  updateCounts(filtered.length, total, 'Amount Involved');

  let html = `<table><thead><tr>`;
  INC_COLS.forEach((col,i) => {{
    let cls = '';
    if (col.sortable) {{
      if (sortCol === col.key || (!sortCol && col.key === 'amount_usd')) {{
        cls = sortDir === 'desc' ? ' sort-desc' : ' sort-asc';
      }}
    }}
    const onclick = col.sortable ? `onclick="sortBy('${{col.key}}')"` : '';
    html += `<th class="${{cls}}" ${{onclick}}>${{col.label}}</th>`;
  }});
  html += `</tr></thead><tbody>`;

  if (!filtered.length) {{
    html += `<tr><td colspan="8"><div class="no-results">No results found</div></td></tr>`;
  }}

  filtered.forEach((inc, idx) => {{
    const cp = inc.counterparty || {{}};
    const qpq = inc.quid_pro_quo || {{}};
    const amt = inc.amount_usd;
    const isExpanded = expandedRow === inc.id;

    html += `<tr onclick="toggleRow('${{inc.id}}')" class="${{isExpanded?'expanded':''}}">
      <td class="td-date">${{inc.date||''}}</td>
      <td class="td-who">
        <div style="font-weight:600">${{escape(cp.name||'')}}</div>
        <div style="font-size:11px;color:var(--text-dim)">${{escape(cp.type||'')}}&nbsp;${{cp.country||''}}</div>
      </td>
      <td class="td-title"><div class="title-text">${{escape(inc.title||'')}}</div></td>
      <td style="min-width:140px">${{(inc.categories||[]).map(catBadge).join('')}}</td>
      <td>${{statusBadge(inc.status)}}</td>
      <td>${{qpq.alleged ? '<span class="badge badge-qpq">YES</span>' : '<span style="color:var(--text-dim);font-size:12px">No</span>'}}</td>
      <td style="min-width:120px">${{benChips(inc.beneficiary)}}</td>
      <td class="td-amount ${{!amt?'zero':''}}">${{amt ? fmt(amt) : '—'}}</td>
    </tr>`;

    if (isExpanded) {{
      html += buildIncidentDetail(inc);
    }}
  }});

  html += `</tbody></table>`;
  document.getElementById('table-container').innerHTML = html;
}}

function buildIncidentDetail(inc) {{
  const cp = inc.counterparty || {{}};
  const fc = inc.financial_connection || {{}};
  const qpq = inc.quid_pro_quo || {{}};
  const srcs = inc.sources || [];

  return `<tr class="detail-row">
    <td colspan="8">
      <div class="detail-inner">
        <div class="detail-block" style="grid-column:1/-1">
          <h4>Summary</h4>
          <p>${{escape(inc.summary||'')}}</p>
        </div>
        <div class="detail-block">
          <h4>Counterparty</h4>
          <p><strong>${{escape(cp.name||'')}}</strong> &mdash; ${{escape(cp.description||'')}}</p>
          <p style="margin-top:4px;color:var(--text-dim);font-size:12px">Type: ${{cp.type||''}} | Country: ${{cp.country||''}}</p>
        </div>
        <div class="detail-block">
          <h4>Financial Connection</h4>
          <p><span class="badge badge-fin-${{fc.exists===true?'yes':'no'}}">${{fc.exists===true?'YES':'NO'}}</span>&nbsp;${{escape(fc.description||'')}}</p>
        </div>
        ${{qpq.alleged ? `<div class="detail-block">
          <h4>Alleged Quid Pro Quo</h4>
          <p><strong>Gave:</strong> ${{escape(qpq.gave||'')}}</p>
          <p style="margin-top:6px"><strong>Received:</strong> ${{escape(qpq.received||'')}}</p>
        </div>` : ''}}
        <div class="detail-block">
          <h4>Amount Note</h4>
          <p>${{escape(inc.amount_note||'—')}}</p>
        </div>
        <div class="detail-block">
          <h4>Actors</h4>
          <p>${{escape((inc.actors||[]).join(', '))}}</p>
        </div>
        <div class="detail-block">
          <h4>Sources (${{srcs.length}})</h4>
          <ul class="source-list">
            ${{srcs.map(s => `<li><a href="${{s.url}}" target="_blank">${{escape(s.title||s.url)}}</a>
              <span class="source-meta">${{s.outlet||''}} · ${{s.date||''}}</span></li>`).join('')}}
          </ul>
        </div>
        <div class="detail-block">
          <h4>Tags</h4>
          <p style="color:var(--text-dim)">${{(inc.tags||[]).join(', ')}}</p>
        </div>
      </div>
    </td>
  </tr>`;
}}

// ── Pardon table ──────────────────────────────────────────────────────────────
const PAR_COLS = [
  {{ key:'date',         label:'Date',          sortable:true  }},
  {{ key:'name',         label:'Name',          sortable:true  }},
  {{ key:'type',         label:'Type',          sortable:true  }},
  {{ key:'offense',      label:'Offense',       sortable:false }},
  {{ key:'fines',        label:'Fines/Forfeiture', sortable:true }},
  {{ key:'restitution',  label:'Restitution',   sortable:true  }},
  {{ key:'total',        label:'Total Forgiven ↕', sortable:true }},
  {{ key:'owed_to',      label:'Owed To',       sortable:true  }},
  {{ key:'financial',    label:'Fin. Conn.',    sortable:true  }},
  {{ key:'political',    label:'Pol. Conn.',    sortable:true  }},
]

function pardonTotal(p) {{
  return (p.fines_forgiven_usd||0) + (p.restitution_forgiven_usd||0);
}}

function renderPardons(data) {{
  const filtered = filterData(data);

  // sort
  const effectiveSort = sortCol || 'total';
  filtered.sort((a,b) => {{
    let av, bv;
    if (effectiveSort === 'total')       {{ av = pardonTotal(a); bv = pardonTotal(b); }}
    else if (effectiveSort === 'fines')  {{ av = a.fines_forgiven_usd||0; bv = b.fines_forgiven_usd||0; }}
    else if (effectiveSort === 'restitution') {{ av = a.restitution_forgiven_usd||0; bv = b.restitution_forgiven_usd||0; }}
    else if (effectiveSort === 'date')   {{ av = a.date||''; bv = b.date||''; }}
    else if (effectiveSort === 'name')   {{ av = a.name||''; bv = b.name||''; }}
    else if (effectiveSort === 'financial') {{ av = a.financial_connection?.exists?1:0; bv = b.financial_connection?.exists?1:0; }}
    else if (effectiveSort === 'political') {{ av = a.political_connection?.exists?1:0; bv = b.political_connection?.exists?1:0; }}
    else {{ av = a[effectiveSort]||''; bv = b[effectiveSort]||''; }}
    if (av < bv) return sortDir==='desc'?1:-1;
    if (av > bv) return sortDir==='desc'?-1:1;
    return 0;
  }});

  const totalForgiven = filtered.reduce((s,p) => s + pardonTotal(p), 0);
  updateCounts(filtered.length, totalForgiven, 'Total Forgiven');

  let html = `<table><thead><tr>`;
  PAR_COLS.forEach(col => {{
    let cls = '';
    if (col.sortable) {{
      const active = sortCol===col.key || (!sortCol && col.key==='total');
      if (active) cls = sortDir==='desc'?' sort-desc':' sort-asc';
    }}
    const onclick = col.sortable ? `onclick="sortBy('${{col.key}}')"` : '';
    html += `<th class="${{cls}}" ${{onclick}}>${{col.label}}</th>`;
  }});
  html += `</tr></thead><tbody>`;

  if (!filtered.length) {{
    html += `<tr><td colspan="10"><div class="no-results">No results found</div></td></tr>`;
  }}

  filtered.forEach(p => {{
    const fin = p.financial_connection || {{}};
    const pol = p.political_connection || {{}};
    const total = pardonTotal(p);
    const isExpanded = expandedRow === p.id;

    html += `<tr onclick="toggleRow('${{p.id}}')" class="${{isExpanded?'expanded':''}}">
      <td class="td-date">${{p.date||''}}</td>
      <td class="td-who" style="min-width:160px">
        <div style="font-weight:600">${{escape(p.name||'')}}</div>
        ${{p.group ? `<div style="font-size:11px;color:var(--text-dim)">${{escape(p.group)}}</div>` : ''}}
      </td>
      <td><span class="badge badge-type-${{p.type||'pardon'}}">${{(p.type||'').toUpperCase()}}</span></td>
      <td style="max-width:220px">
        <div style="display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;font-size:12px">
          ${{escape(p.offense||'')}}
        </div>
      </td>
      <td class="td-forgiven forgiven-part">${{p.fines_forgiven_usd ? fmt(p.fines_forgiven_usd) : '—'}}</td>
      <td class="td-forgiven forgiven-part">${{p.restitution_forgiven_usd ? fmt(p.restitution_forgiven_usd) : '—'}}</td>
      <td class="td-forgiven forgiven-total">${{total ? fmt(total) : '—'}}</td>
      <td>${{p.restitution_owed_to === 'private_victims'
          ? '<span class="badge badge-owed-private">Private Victims</span>'
          : p.restitution_owed_to === 'government'
          ? '<span class="badge badge-owed-govt">Government</span>'
          : p.restitution_owed_to === 'both'
          ? '<span class="badge badge-owed-both">Both</span>'
          : '<span style="color:var(--text-dim);font-size:12px">—</span>'}}</td>
      <td><span class="badge badge-fin-${{fin.exists===true?'yes':'no'}}">${{fin.exists===true?'YES':'No'}}</span></td>
      <td><span class="badge badge-pol-${{pol.exists===true?'yes':'no'}}">${{pol.exists===true?'YES':'No'}}</span></td>
    </tr>`;

    if (isExpanded) {{
      html += buildPardonDetail(p);
    }}
  }});

  html += `</tbody></table>`;
  document.getElementById('table-container').innerHTML = html;
}}

function buildPardonDetail(p) {{
  const fin = p.financial_connection || {{}};
  const pol = p.political_connection || {{}};
  const srcs = p.sources || [];
  const total = pardonTotal(p);

  return `<tr class="detail-row">
    <td colspan="10">
      <div class="detail-inner">
        <div class="detail-block">
          <h4>Full Offense</h4>
          <p>${{escape(p.offense||'')}}</p>
          <p style="margin-top:6px;color:var(--text-dim);font-size:12px">Original sentence: ${{escape(p.original_sentence||'—')}}</p>
        </div>
        <div class="detail-block">
          <h4>Financial Summary</h4>
          <p>Fines/Forfeiture: <strong style="color:var(--gold)">${{fmtFull(p.fines_forgiven_usd)}}</strong></p>
          <p>Restitution: <strong style="color:var(--gold)">${{fmtFull(p.restitution_forgiven_usd)}}</strong></p>
          <p>Owed to: ${{p.restitution_owed_to||'—'}}</p>
          ${{total ? `<p style="margin-top:6px"><strong style="color:var(--accent)">Total forgiven: ${{fmtFull(total)}}</strong></p>` : ''}}
        </div>
        <div class="detail-block">
          <h4>Financial Connection</h4>
          <p><span class="badge badge-fin-${{fin.exists===true?'yes':'no'}}">${{fin.exists===true?'YES':'No'}}</span>&nbsp;${{escape(fin.description||'None identified')}}</p>
        </div>
        <div class="detail-block">
          <h4>Political Connection</h4>
          <p><span class="badge badge-pol-${{pol.exists===true?'yes':'no'}}">${{pol.exists===true?'YES':'No'}}</span>&nbsp;${{escape(pol.description||'None identified')}}</p>
        </div>
        ${{p.notes ? `<div class="detail-block" style="grid-column:1/-1">
          <h4>Notes</h4>
          <p>${{escape(p.notes)}}</p>
        </div>` : ''}}
        <div class="detail-block">
          <h4>Sources (${{srcs.length}})</h4>
          <ul class="source-list">
            ${{srcs.map(s => `<li><a href="${{s.url}}" target="_blank">${{escape(s.title||s.url)}}</a>
              <span class="source-meta">${{s.outlet||''}} · ${{s.date||''}}</span></li>`).join('')}}
          </ul>
        </div>
      </div>
    </td>
  </tr>`;
}}

// ── Helpers ───────────────────────────────────────────────────────────────────
function sortByCol(a, b, col, dir) {{
  let av, bv;
  if (col === 'amount_usd') {{ av = a.amount_usd||0; bv = b.amount_usd||0; }}
  else if (col === 'date')  {{ av = a.date||''; bv = b.date||''; }}
  else if (col === 'status') {{ av = a.status||''; bv = b.status||''; }}
  else {{ av = a[col]||''; bv = b[col]||''; }}
  if (av < bv) return dir==='desc' ? 1 : -1;
  if (av > bv) return dir==='desc' ? -1 : 1;
  return 0;
}}

function sortBy(col) {{
  if (sortCol === col) sortDir = sortDir === 'desc' ? 'asc' : 'desc';
  else {{ sortCol = col; sortDir = 'desc'; }}
  expandedRow = null;
  if (currentType === 'incident') renderIncidents(currentData);
  else renderPardons(currentData);
}}

function toggleRow(id) {{
  expandedRow = expandedRow === id ? null : id;
  if (currentType === 'incident') renderIncidents(currentData);
  else renderPardons(currentData);
}}

function updateCounts(count, total, label) {{
  document.getElementById('view-count').textContent = count + ' records';
  const totalEl = document.getElementById('view-total');
  totalEl.textContent = total ? fmt(total) : '';
  document.getElementById('view-total-header').textContent = total ? fmt(total) : '';
}}

// ── Init ──────────────────────────────────────────────────────────────────────
buildSidebar();
showView('all-incidents');
</script>
</body>
</html>"""

OUTPUT.write_text(html, encoding="utf-8")
print(f"Built: {{OUTPUT}}")
print(f"Open in browser: file:///{OUTPUT.as_posix()}")
