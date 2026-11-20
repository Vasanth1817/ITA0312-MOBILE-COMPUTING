"""Compare predicted app behaviour to observable test points."""
checks={"launch path":["cold start","warm start"],"memory":["low-memory trim","allocation pressure"],"background":["defer","resume"],"permission":["granted","revoked"]}
print("Probe plan and expected observations")
for area,tests in checks.items():
 print(f"\n{area}:")
 for t in tests: print(f" - {t}: record timestamp, state, result and resource use")
print("\nUse Android Studio profiler / Xcode instruments for real measurements.")
