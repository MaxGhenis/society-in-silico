import copy, json, sys
from pathlib import Path
sys.path.insert(0, "scripts")
import pe_computed_numbers as m
import policyengine as pe
h=json.load(open("scripts/results/pe-computed-numbers/households.json"))
checks=[]
for name, earnings in [("nc_two_children",38000),("nc_two_children",39000),("nc_two_children",55100),("nc_two_children",55200),("ny_one_child",30000),("ny_one_child",30100)]:
    curve=h["curves"][name]; inputs=copy.deepcopy(curve["inputs"])
    inputs["people"][0]["employment_income"]=earnings
    r=pe.us.calculate_household(**inputs,reform={m.HEALTH:False},extra_variables=m.EXTRAS)
    i=curve["earnings"].index(earnings)
    got={"net_income":r.household.household_net_income,"ssi":sum(p.ssi for p in r.person),"income_tax":r.tax_unit.income_tax,"state_income_tax":r.tax_unit.state_income_tax}
    want={"net_income":curve["outputs"]["household_net_income"][i],"ssi":curve["outputs"]["ssi"][i],"income_tax":curve["outputs"]["income_tax"][i],"state_income_tax":curve["outputs"]["state_income_tax"][i]}
    errors={k:got[k]-want[k] for k in got}
    assert all(abs(e)<0.02 for e in errors.values()),(name,earnings,errors)
    checks.append({"case":name,"earnings":earnings,"outputs":got,"receipt_errors":errors})
    print(name,earnings,got,flush=True)
for year,want in [(2020,1875),(2021,7200),(2022,1875),(2026,1875)]:
    inputs=copy.deepcopy(h["ctc"]["inputs"]);inputs["year"]=year;inputs["people"][0]["employment_income"]=15000
    r=pe.us.calculate_household(**inputs,extra_variables=["refundable_ctc","income_tax_capped_non_refundable_credits"])
    got=r.tax_unit.refundable_ctc+r.tax_unit.income_tax_capped_non_refundable_credits
    assert abs(got-want)<0.02
    checks.append({"ctc_year":year,"ctc_at_15000":got})
    print(year,got,flush=True)
for earnings in [0,15000,60000]:
    inputs=copy.deepcopy(h["ctc"]["inputs"]);inputs["people"][0]["employment_income"]=earnings
    r=pe.us.calculate_household(**inputs,reform={m.REFUNDABILITY:True},extra_variables=["refundable_ctc","income_tax_capped_non_refundable_credits"])
    got=r.tax_unit.refundable_ctc+r.tax_unit.income_tax_capped_non_refundable_credits
    assert abs(got-4400)<0.02
    checks.append({"reform_ctc_earnings":earnings,"ctc":got})
    print("refundability",earnings,got,flush=True)
rich=[]
for earnings in [30000000,30010000]:
    inputs=copy.deepcopy(h["capital_gains"]["inputs"]);inputs["people"][0]["long_term_capital_gains"]=earnings
    r=pe.us.calculate_household(**inputs,reform={m.HEALTH:False},extra_variables=["income_tax","state_income_tax","net_investment_income_tax"])
    rich.append({"gains":earnings,"net_income":r.household.household_net_income,"federal_tax":r.tax_unit.income_tax,"state_city_tax":r.tax_unit.state_income_tax})
    print("capitalgains",rich[-1],flush=True)
delta={k:rich[1][k]-rich[0][k] for k in rich[0]};mtr=1-delta["net_income"]/10000
assert abs(mtr-0.3858)<0.00001
assert delta["federal_tax"]==2380 and delta["state_city_tax"]==1478
checks.append({"capital_gains_scalar_checks":rich,"delta":delta,"combined_mtr":mtr})
Path("independent-household-results.json").write_text(json.dumps({"provenance":m.provenance(),"checks":checks},indent=2)+"\n")
print("PASS: 15 independently computed scalar household calls agree with frozen axis receipts")
