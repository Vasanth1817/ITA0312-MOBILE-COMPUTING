"""Illustrative lifecycle event trace."""
events=["process created","application initialized","activity onCreate","activity onStart","activity onResume","activity onPause","activity onStop","process may be cached"]
for n,e in enumerate(events,1): print(f"{n:02d}. {e}")
print("\nLifecycle callbacks depend on navigation, system policy and platform version.")
