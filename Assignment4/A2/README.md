# Assignment 4A — Task 2: Platform comparison (8 marks)

## Requirement
Secure background messaging across Android, iOS and Windows. Compare push path, callback capability/time, secure key storage and shared vs platform-specific code. Maximise reliable confidential delivery with battery constraints and no persistent app socket/wakelock.

## Hypothesis
Framework process-lifecycle/background-execution policies dominate delivery differences more than kernel family/runtime because the framework determines whether app code may run and under what quota.

| Aspect | Android | iOS | Windows UWP |
|---|---|---|---|
| Kernel | Linux monolithic | XNU hybrid | NT hybrid |
| Runtime | ART DEX interpreter/JIT/profile AOT, GC | Swift/Obj-C native, ARC | WinRT ABI; native or .NET AOT |
| IPC | Binder | XPC/Mach ports | ALPC/COM/RPC |
| Background push | FCM/Play Services, ActivityManager and app callback | APNs/apsd; extension for mutable content | WNS and background task host, quota |
| Isolation | UID, SELinux, seccomp | sandbox, entitlements | AppContainer |

Push trace: modem/network wakes OS; system push service receives message; OS grants bounded execution; app/extension decrypts using secure-store key and posts notification; callback ends and device returns idle. If process is killed, OS may recreate Android app; iOS alert still displays and extension may run. Windows 10 Mobile is discontinued; Windows column describes relevant UWP desktop/tablet architecture.
