import sys; sys.path.insert(0,"/Users/kerryback/.claude/skills/two-stage-dcf")
from dcf_load import load_statements
from dcf_history import check_footing
from classification import CLASSIFICATION, ASSET_COMPONENTS, classification

bs = load_statements("financials-current.xlsx", sheet="Balance Sheet")
lines, years = bs["lines"], bs["years"]

named = {l for l, _ in CLASSIFICATION}
missing = sorted(set(lines) - named)
extra   = sorted(named - set(lines))
print("unclassified reported lines:", missing or "none")
print("classified but absent:      ", extra or "none")
assert not missing and not extra

for fy in years:
    comp = {l: (lines[l].get(fy) or 0.0) for l in ASSET_COMPONENTS}
    try:
        check_footing([{"line": l, "bucket": "x"} for l in comp], comp,
                      reported_total=lines["Total assets"][fy])
        print(f"FY{fy}: asset components foot to {lines['Total assets'][fy]:,.0f}  OK")
    except ValueError as e:
        print(f"FY{fy}: {e}")

fy = years[-1]
print(f"\nbuckets at base year FY{fy}  ($m)")
for bucket in ["net_ppe","operating_asset","operating_liability",
               "nonoperating_asset","debt_claim","equity_claim"]:
    members = [c["line"] for c in classification() if c["bucket"] == bucket]
    tot = sum(lines[m].get(fy) or 0.0 for m in members)
    print(f"  {bucket:20s} {tot:>12,.0f}")
