"""Split the two aggregated 'Other ... non-current' lines into footnoted components.

Every component below is a figure disclosed in a 10-K footnote; the sources are
named per line. The residual rows are plugs: the reported aggregate less the
disclosed components, so each aggregate still foots exactly.
"""
import pandas as pd
from assemble import bs as ann_bs, inc as ann_inc, cf as ann_cf
from ttm import bs, inc, cf, TTM, restated

Y = ["FY2021","FY2022","FY2023","FY2024","FY2025",TTM]

# --- disclosed components -----------------------------------------------------
# Deferred tax assets sitting inside Other non-current assets.
#   FY2022-FY2025: 'Other Non-Current Assets' footnote (FY2023/FY2024/FY2025 10-K).
#   FY2021: no such footnote that year -- proxy is 'Net deferred tax assets'
#           from the FY2021 10-K income-tax footnote.
#   TTM: the Q3 FY2026 10-Q is condensed and does not repeat the footnote,
#        so the FY2025 disclosed level is carried and the residual absorbs change.
DTA = {"FY2021": 13073.0, "FY2022": 15375.0, "FY2023": 17852.0,
       "FY2024": 19499.0, "FY2025": 20777.0, TTM: 20777.0}
# Operating lease ROU assets, inside Other non-current assets ('Leases' footnote).
OP_ROU = {"FY2021": 10087.0, "FY2022": 10417.0, "FY2023": 10661.0,
          "FY2024": 10234.0, "FY2025": 11205.0, TTM: 11205.0}
# Lease liabilities, inside Other non-current liabilities ('Leases' footnote).
OP_LL = {"FY2021": 9506.0, "FY2022": 9936.0, "FY2023": 10408.0,
         "FY2024": 10046.0, "FY2025": 10911.0, TTM: 10911.0}
FIN_LL = {"FY2021": 769.0, "FY2022": 812.0, "FY2023": 859.0,
          "FY2024": 752.0, "FY2025": 692.0, TTM: 692.0}

A_DTA  = "Deferred tax assets (in other non-current assets)"
A_ROU  = "Operating lease right-of-use assets (in other non-current assets)"
A_RES  = "Other long-term assets (in other non-current assets)"
L_OPLL = "Operating lease liabilities, non-current (in other non-current liabilities)"
L_FNLL = "Finance lease liabilities, non-current (in other non-current liabilities)"
L_RES  = "Long-term taxes payable and other (in other non-current liabilities)"

# FY2025 on the Q3-FY2026 presentation: intangibles carved out of other
# non-current assets, so the asset residual is comparable with the TTM column.
bs.loc["Intangible assets, net", "FY2025"] = restated["Intangible assets, net"]
bs.loc["Other non-current assets", "FY2025"] = restated["Other non-current assets"]

onca = bs.loc["Other non-current assets"]
oncl = bs.loc["Other non-current liabilities"]
rows = {
    A_DTA:  {y: DTA[y] for y in Y},
    A_ROU:  {y: OP_ROU[y] for y in Y},
    A_RES:  {y: onca[y] - DTA[y] - OP_ROU[y] for y in Y},
    L_OPLL: {y: OP_LL[y] for y in Y},
    L_FNLL: {y: FIN_LL[y] for y in Y},
    L_RES:  {y: oncl[y] - OP_LL[y] - FIN_LL[y] for y in Y},
}
for label, series in rows.items():
    bs.loc[label] = pd.Series(series)

order = []
for label in [l for l in bs.index if l not in rows]:
    order.append(label)
    if label == "Other non-current assets":      order += [A_DTA, A_ROU, A_RES]
    if label == "Other non-current liabilities": order += [L_OPLL, L_FNLL, L_RES]
bs = bs.reindex(order)

if __name__ == "__main__":
    with pd.ExcelWriter("financials-current.xlsx", engine="openpyxl") as xw:
        bs.to_excel(xw, sheet_name="Balance Sheet")
        inc.to_excel(xw, sheet_name="Income Statement")
        cf.to_excel(xw, sheet_name="Cash Flow Statement")
    pd.set_option("display.width", 220)
    print(bs.loc[["Other non-current assets", A_DTA, A_ROU, A_RES,
                  "Other non-current liabilities", L_OPLL, L_FNLL, L_RES]].to_string())
