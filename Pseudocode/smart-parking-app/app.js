// ===================================================
// PARKEASE — SMART PARKING APP JAVASCRIPT
// Strict pseudocode implementation:
// 1. Welcome -> Login or Register -> Home
// 2. Home -> Empty Parking Count | Free Parking Slots | Book Parking
// 3. Book Parking -> User selects a parking slot -> DISPLAY Booking Confirmation Screen
// ===================================================

document.addEventListener('DOMContentLoaded', () => {
  // Update status bar clock
  const updateClock = () => {
    const now = new Date();
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const clockEl = document.getElementById('statusTime');
    if (clockEl) clockEl.textContent = `${hours}:${minutes}`;
  };
  updateClock();
  setInterval(updateClock, 30000);

  // Screen Switcher
  const navigateTo = (screenId) => {
    const screens = document.querySelectorAll('.screen');
    screens.forEach(screen => screen.classList.remove('active'));

    const target = document.getElementById(screenId);
    if (target) {
      target.classList.add('active');
      const body = target.querySelector('.screen-body') || target.querySelector('.home-scroll-area');
      if (body) body.scrollTop = 0;
    }

    // Sync Bottom Tab active state
    document.querySelectorAll('.tab-item').forEach(tab => {
      if (tab.getAttribute('data-target') === screenId) {
        tab.classList.add('active');
      } else {
        tab.classList.remove('active');
      }
    });
  };

  // Toast Helper
  const showToast = (message) => {
    const toast = document.getElementById('appToast');
    if (!toast) return;
    toast.textContent = message;
    toast.classList.add('show');
    setTimeout(() => {
      toast.classList.remove('show');
    }, 2800);
  };

  // 1. Welcome Screen Actions
  const btnGoToLogin = document.getElementById('btnGoToLogin');
  const btnGoToRegister = document.getElementById('btnGoToRegister');

  if (btnGoToLogin) btnGoToLogin.addEventListener('click', () => navigateTo('screenLogin'));
  if (btnGoToRegister) btnGoToRegister.addEventListener('click', () => navigateTo('screenRegister'));

  // Cross links
  const linkLoginToRegister = document.getElementById('linkLoginToRegister');
  const linkRegisterToLogin = document.getElementById('linkRegisterToLogin');

  if (linkLoginToRegister) linkLoginToRegister.addEventListener('click', (e) => { e.preventDefault(); navigateTo('screenRegister'); });
  if (linkRegisterToLogin) linkRegisterToLogin.addEventListener('click', (e) => { e.preventDefault(); navigateTo('screenLogin'); });

  // Generic Back Buttons
  document.querySelectorAll('.back-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const targetScreen = btn.getAttribute('data-target') || 'screenWelcome';
      navigateTo(targetScreen);
    });
  });

  // State Management
  let currentPlate = 'KA-05-MN-2026';
  let selectedSlot = 'Slot B-03';
  let selectedLevel = 'Level 1';
  let selectedDuration = 2; // hours
  const hourlyRate = 3.50;

  // 2. Login Flow (IF user selects "Login" -> DISPLAY Login Screen -> Home Screen)
  const loginForm = document.getElementById('loginForm');
  if (loginForm) {
    loginForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const email = document.getElementById('loginEmail').value.trim();
      const pass = document.getElementById('loginPassword').value.trim();

      if (!email || !pass) {
        showToast('Please enter your email/plate and password');
        return;
      }

      const driverName = email.includes('@') ? email.split('@')[0] : email;
      const formatted = driverName.charAt(0).toUpperCase() + driverName.slice(1);
      const greetingEl = document.getElementById('homeDriverName');
      if (greetingEl) greetingEl.textContent = formatted;

      showToast(`Welcome driver ${formatted}!`);
      navigateTo('screenHome');
    });
  }

  // 3. Register Flow (ELSE IF user selects "Register" -> DISPLAY Registration Screen -> Home Screen)
  const registerForm = document.getElementById('registerForm');
  if (registerForm) {
    registerForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('regDriverName').value.trim();
      const plate = document.getElementById('regVehiclePlate').value.trim().toUpperCase();
      const pass = document.getElementById('regPassword').value.trim();

      if (!name || !plate || !pass) {
        showToast('Please fill all driver and vehicle fields');
        return;
      }

      currentPlate = plate;
      const greetingEl = document.getElementById('homeDriverName');
      if (greetingEl) greetingEl.textContent = name;
      const platePill = document.getElementById('homePlatePill');
      if (platePill) platePill.textContent = plate;

      showToast(`Vehicle registered: ${plate}!`);
      navigateTo('screenHome');
    });
  }

  // 4. Home Screen Navigation (Empty Parking Count | Free Parking Slots | Book Parking)
  const navToEmptyCount = document.getElementById('navToEmptyCount');
  const navToFreeSlots = document.getElementById('navToFreeSlots');
  const navToBookParking = document.getElementById('navToBookParking');

  if (navToEmptyCount) navToEmptyCount.addEventListener('click', () => navigateTo('screenEmptyCount'));
  if (navToFreeSlots) navToFreeSlots.addEventListener('click', () => navigateTo('screenFreeSlots'));
  if (navToBookParking) navToBookParking.addEventListener('click', () => navigateTo('screenBookParking'));

  // Empty Count Proceed Button
  const btnCountProceedToBook = document.getElementById('btnCountProceedToBook');
  if (btnCountProceedToBook) {
    btnCountProceedToBook.addEventListener('click', () => {
      navigateTo('screenBookParking');
    });
  }

  // Bottom Tab Bar
  document.querySelectorAll('.tab-item').forEach(tab => {
    tab.addEventListener('click', () => {
      const target = tab.getAttribute('data-target');
      if (target) navigateTo(target);
    });
  });

  // Logout
  const btnHomeLogout = document.getElementById('btnHomeLogout');
  if (btnHomeLogout) {
    btnHomeLogout.addEventListener('click', () => {
      if (confirm('Log out of ParkEase and return to Welcome screen?')) {
        showToast('Logged out');
        navigateTo('screenWelcome');
      }
    });
  }

  // Select Location from Free Slots Screen
  window.selectLocationToBook = (lotName, freeSlotsText, price) => {
    const bookingLotName = document.getElementById('bookingLotName');
    if (bookingLotName) bookingLotName.textContent = lotName;
    showToast(`Selected: ${lotName} (${freeSlotsText})`);
    navigateTo('screenBookParking');
  };

  // Floor Level Toggle in Slot Selection
  document.querySelectorAll('.lvl-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.lvl-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      selectedLevel = btn.getAttribute('data-level') === 'L1' ? 'Level 1' : 'Level 2';
      showToast(`Viewing ${selectedLevel} bays`);
    });
  });

  // Duration buttons
  document.querySelectorAll('.hour-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.hour-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const text = btn.textContent.trim();
      if (text.includes('1')) selectedDuration = 1;
      else if (text.includes('2')) selectedDuration = 2;
      else if (text.includes('4')) selectedDuration = 4;
      else selectedDuration = 8;
      showToast(`Selected duration: ${text}`);
    });
  });

  // 5. USER SELECTS A PARKING SLOT (Pseudocode logic)
  const availableSlots = document.querySelectorAll('.bay-slot.available');
  availableSlots.forEach(slotEl => {
    slotEl.addEventListener('click', () => {
      // Remove selected from all
      document.querySelectorAll('.bay-slot').forEach(s => s.classList.remove('selected'));
      slotEl.classList.add('selected');

      const slotCode = slotEl.getAttribute('data-slot') || 'A-03';
      const slotType = slotEl.getAttribute('data-type') || 'Standard Parking Bay';
      selectedSlot = `Slot ${slotCode}`;

      const badgeEl = document.getElementById('selectedSlotBadge');
      const typeEl = document.getElementById('selectedSlotType');
      if (badgeEl) badgeEl.textContent = selectedSlot;
      if (typeEl) typeEl.textContent = `${slotType} Bay`;

      showToast(`Selected: ${selectedSlot} (${slotType})`);
    });
  });

  // 6. Confirm Booking Action -> DISPLAY Booking Confirmation Screen (Pseudocode logic)
  const btnConfirmBooking = document.getElementById('btnConfirmBookingAction');
  if (btnConfirmBooking) {
    btnConfirmBooking.addEventListener('click', () => {
      // Generate reference code
      const randomRef = '#PRK-' + Math.floor(10000 + Math.random() * 90000);
      const ticketRef = document.getElementById('ticketRefCode');
      const confirmSlot = document.getElementById('confirmSlotCode');
      const confirmPlate = document.getElementById('confirmPlateCode');

      if (ticketRef) ticketRef.textContent = randomRef;
      if (confirmSlot) confirmSlot.textContent = `${selectedSlot} (${selectedLevel})`;
      if (confirmPlate) confirmPlate.textContent = currentPlate;

      showToast(`Booking Confirmed for ${selectedSlot}!`);
      navigateTo('screenBookingConfirmation');
    });
  }

  // Return to Home from Confirmation
  const btnBackHome = document.getElementById('btnBackToHomeFromConfirm');
  if (btnBackHome) {
    btnBackHome.addEventListener('click', () => {
      navigateTo('screenHome');
    });
  }
});
