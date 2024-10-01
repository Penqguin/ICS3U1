d, w = int(input("day minutes: ")), int(input("weekend minutes: "))

if d <= 500:
    planA = 50 / 30 
    print("Daily cost of plan A ", round(planA, 2))
else:
    planA = 65 / 30
    print("Daily cost of plan A ", round(planA, 2))

planB = (d * 0.1) + (w * 0.05)
print("Daily cost of plan B", round(planB, 2))

if planA > planB:
    print(f"Plan B is cheaper at a rate of {round(planB, 2)}")
elif planA < planB:
    print(f"Plan A is cheaper at a rate of {round(planA, 2)}")
elif planA == planB:
    print(f"Both plans cost the same at a rate of {round(planA, 2)}")