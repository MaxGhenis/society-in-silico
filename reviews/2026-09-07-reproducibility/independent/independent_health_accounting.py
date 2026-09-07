import gc,json,sys
from pathlib import Path
sys.path.insert(0,"scripts")
import pe_computed_numbers as m
import policyengine as pe
from microdf import MicroSeries
receipt=m.provenance();run_dir=Path("output/pe-reproduction").resolve();m.stage_cached_dataset(receipt,run_dir)
results={};keep={}
with m.working_directory(run_dir):
 for label,full in [("baseline",False),("reform",True)]:
    print("Construct",label,flush=True)
    sim=pe.us.managed_microsimulation(reform={m.REFUNDABILITY:{"2026-01-01.2026-12-31":full},m.HEALTH:{"2026-01-01.2026-12-31":False}})
    snap={}
    for variable in ["aca_ptc","assigned_aca_ptc","premium_tax_credit","basic_health_program"]:
        print(label,variable,flush=True)
        snap[variable]=sim.calc(variable,period=2026,map_to="household")
        assert isinstance(snap[variable],MicroSeries)
    results[label]={"provenance":sim.policyengine_bundle,"aggregates":{k:float(v.sum()) for k,v in snap.items()}}
    keep[label]=snap
    Path(label+"-independent-health.json").write_text(json.dumps(results[label],indent=2)+"\n")
    del sim;gc.collect()
changes={k:float((keep["reform"][k]-keep["baseline"][k]).sum()) for k in keep["baseline"]}
results["changes"]=changes
Path("independent-health-accounting-results.json").write_text(json.dumps(results,indent=2)+"\n")
print(json.dumps(changes,indent=2),flush=True)
