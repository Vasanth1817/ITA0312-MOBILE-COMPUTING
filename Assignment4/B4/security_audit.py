"""Static checklist-style security audit demonstration; no app or device is scanned."""
findings=[
("Hard-coded secrets","Critical","Move secrets out of source; rotate exposed credentials"),
("Unencrypted local data","High","Use encrypted storage and minimize retention"),
("Weak transport","High","Require TLS and validate endpoints"),
("Excessive permissions","Medium","Remove unused permissions; explain required access"),
("Exported components","High","Restrict component exposure and validate intents"),
("Logging sensitive data","High","Redact sensitive fields and audit logs"),
]
print("Finding | Severity | Recommendation")
for f,s,r in findings: print(f"{f} | {s} | {r}")
