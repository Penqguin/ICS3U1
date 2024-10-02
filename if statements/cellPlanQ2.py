d, e, w = float(input("day minutes: ")), float(input("evening minutes: ")), float(input("weekend minutes: "))
planA, planB = 0.0, 0.0

if d > 100:
    planA += ((d - 100) * 0.25) + (0.15 * e) + (0.20 * w)
    print("cost of plan A ", "%.2f"%planA)
else:
    planA += (0.15 * e) + (0.20 * w)
if d > 250:
    planB += ((d - 250) * 0.45) + (0.35 * e) + (0.25 * w)
    print("cost of plan B ", "%.2f"%planB)
else:
    planB += (0.35 * e) + (0.25 * w)

if planA > planB:
    print("Plan B is cheaper at a rate of ", "%.2f"%planB)
elif planA < planB:
    print("Plan A is cheaper at a rate of ", "%.2f"%planA)
elif planA == planB:
    print("Both plans cost the same at a rate of ", "%.2f"%planA)