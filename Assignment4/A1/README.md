# Assignment 4A — Task 1: Architecture Review (6 marks)

## 1.1 Diagnose the description
The generic OS description is not implementable or testable because it omits: firmware/bootloader, drivers, HAL, native libraries and framework services; kernel type/duties; distinction between kernel scheduling and CPU execution; runtime/code delivery and compilation strategy; security enforcement locations; power-management triggers/mechanisms; and app-to-OS IPC/system-call boundaries.

## 1.2 Android architecture specification
| Layer | Responsibility | Interface/dependency |
|---|---|---|
| L0 Hardware/firmware | SoC, GPU, modem, sensors, TEE, bootloader | Physical registers, interrupts, DMA |
| L1 Linux kernel | Scheduling, VM, Binder driver, drivers, SELinux, UID, cgroups, suspend/wakelocks, cpufreq | Syscalls, proc/sys, Binder device |
| L2 HAL | Vendor hardware interfaces: camera, sensor, radio, power, graphics | AIDL/HIDL |
| L3 Native libraries/daemons | bionic, SurfaceFlinger, SQLite, crypto, keystore2, init, servicemanager, Zygote | NDK APIs and services |
| L4 ART | DEX execution, interpreter/JIT/profile-guided AOT, GC, JNI; Zygote preloads/forks | Java/Kotlin execution environment |
| L5 Framework | system_server, ActivityManager, PackageManager, PowerManager, WindowManager, jobs, notifications | SDK, Binder, lifecycle |
| L6 Apps | Activity, Service, Receiver, Provider and UI/business logic | Framework APIs |

Security: kernel UID/SELinux/seccomp, PackageManager/AppOps, Keystore/TEE and verified boot. Power policy: PowerManagerService drives kernel suspend/wakelocks and CPU-frequency mechanisms.

## 1.3 Design defence
The layered specification assigns responsibilities, interfaces and dependencies; security and power mechanisms have identifiable enforcement points rather than vague claims.
