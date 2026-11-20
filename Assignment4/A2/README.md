# Assignment 4A — Task 2: Platform requirement comparison (8 marks)

## Requirement
Secure background messaging across Android, iOS and Windows. Compare push path, callback capability/time, secure key storage and shared vs platform-specific code. Objective: reliable confidential delivery with battery constraints and no persistent app socket/wakelock.

## Hypothesis
Framework process-lifecycle and background-execution policies dominate delivery differences more than kernel family/runtime because the framework determines whether app code may run and under what quota.

## Comparison
| Aspect | Android | iOS | Windows UWP |
|---|---|---|---|
| Kernel | Linux monolithic | XNU hybrid | NT hybrid |
| Runtime | ART DEX interpreter/JIT/profile-guided AOT, GC | Swift/Obj-C native, ARC | WinRT ABI; native or .NET AOT |
| IPC | Binder | XPC/Mach ports | ALPC/COM/RPC |
| Background push | FCM/Play Services, ActivityManager and app callback | APNs/apsd; notification service extension for mutable content | WNS and background task host, quota |
| Isolation | UID, SELinux, seccomp | sandbox, entitlements | AppContainer |

## Push trace
Screen-off message: modem/network event wakes the OS; system push service receives it; OS grants a bounded execution opportunity; app/extension decrypts with secure-store key and posts notification; callback ends and system returns to idle.

If OS kills process, push path can recreate Android app process; iOS alert still displays and extension may run. Force-stop/force-quit behaviour differs. Windows 10 Mobile is discontinued; Windows UWP column describes relevant desktop/tablet architecture.
