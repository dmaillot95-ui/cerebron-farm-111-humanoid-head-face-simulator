import json,math,pathlib
# Reduced ocular/head kinematic canary, not a physical robot model.
targets=[(-20,-10),(0,0),(20,10),(35,-15)]
rows=[]
for yaw,pitch in targets:
 cy=max(-40,min(40,yaw));cp=max(-25,min(25,pitch));err=math.hypot(cy-yaw,cp-pitch);rows.append({"target_deg":[yaw,pitch],"command_deg":[cy,cp],"clamped":err>0,"error_deg":round(err,6)})
checks={"bounded_yaw":all(abs(x["command_deg"][0])<=40 for x in rows),"bounded_pitch":all(abs(x["command_deg"][1])<=25 for x in rows),"finite":all(math.isfinite(x["error_deg"]) for x in rows)}
out={"farm":111,"status":"PASS" if all(checks.values()) else "FAIL","checks":checks,"samples":rows,"epistemic":"REDUCED_OCULAR_KINEMATIC_CANARY_NOT_GALIKA_RECONSTRUCTION_NOT_PHYSICAL_VALIDATION"}
pathlib.Path("artifacts").mkdir(exist_ok=True);pathlib.Path("artifacts/result.json").write_text(json.dumps(out,indent=2)+"\\n");print(json.dumps(out));raise SystemExit(0 if out["status"]=="PASS" else 1)
