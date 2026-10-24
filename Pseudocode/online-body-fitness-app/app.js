// ===================================================
// IRONPULSE — ONLINE BODY FITNESS APP JAVASCRIPT
// Strict pseudocode implementation:
// 1. Welcome -> Login or Register -> Home
// 2. Home -> Fitness Blog | Diet Planner | Fitness Videos | Subscription
// 3. Subscription -> DISPLAY Subscription Plans Screen
//                 -> DISPLAY Payment Screen
//                 -> DISPLAY Payment Confirmation Screen
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

  // 2. Login Flow (IF user selects "Login" -> DISPLAY Login Screen -> Home Screen)
  const loginForm = document.getElementById('loginForm');
  if (loginForm) {
    loginForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const email = document.getElementById('loginEmail').value.trim();
      const pass = document.getElementById('loginPassword').value.trim();

      if (!email || !pass) {
        showToast('Please enter athlete email and password');
        return;
      }

      const athlete = email.split('@')[0];
      const formatted = athlete.charAt(0).toUpperCase() + athlete.slice(1);
      const greetingEl = document.getElementById('homeAthleteName');
      if (greetingEl) greetingEl.textContent = formatted;

      showToast(`Welcome athlete ${formatted}!`);
      navigateTo('screenHome');
    });
  }

  // 3. Register Flow (ELSE IF user selects "Register" -> DISPLAY Registration Screen -> Home Screen)
  const registerForm = document.getElementById('registerForm');
  if (registerForm) {
    registerForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('regAthleteName').value.trim();
      const email = document.getElementById('regEmail').value.trim();
      const goal = document.getElementById('regFitnessGoal').value.trim();
      const pass = document.getElementById('regPassword').value.trim();

      if (!name || !email || !pass) {
        showToast('Please complete all athlete registration fields');
        return;
      }

      const greetingEl = document.getElementById('homeAthleteName');
      if (greetingEl) greetingEl.textContent = name;
      const cardHolder = document.getElementById('cardHolderName');
      if (cardHolder) cardHolder.value = name;

      showToast(`Account created: ${name} (${goal})`);
      navigateTo('screenHome');
    });
  }

  // 4. Home Screen Navigation (Fitness Blog | Diet Planner | Fitness Videos | Subscription)
  const navToFitnessBlog = document.getElementById('navToFitnessBlog');
  const navToDietPlanner = document.getElementById('navToDietPlanner');
  const navToFitnessVideos = document.getElementById('navToFitnessVideos');
  const navToSubscription = document.getElementById('navToSubscription');

  if (navToFitnessBlog) navToFitnessBlog.addEventListener('click', () => navigateTo('screenFitnessBlog'));
  if (navToDietPlanner) navToDietPlanner.addEventListener('click', () => navigateTo('screenDietPlanner'));
  if (navToFitnessVideos) navToFitnessVideos.addEventListener('click', () => navigateTo('screenFitnessVideos'));
  if (navToSubscription) navToSubscription.addEventListener('click', () => navigateTo('screenSubscription'));

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
      if (confirm('Log out and return to IronPulse Welcome screen?')) {
        showToast('Logged out');
        navigateTo('screenWelcome');
      }
    });
  }

  // 5. Subscription -> Payment -> Payment Confirmation Flow (Pseudocode logic)
  const btnSelectProPlan = document.getElementById('btnSelectProPlan');
  if (btnSelectProPlan) {
    btnSelectProPlan.addEventListener('click', () => {
      showToast('FitPulse PRO Selected &rarr; Loading Secure Checkout');
      navigateTo('screenPayment');
    });
  }

  // Payment Method Tabs
  document.querySelectorAll('.pay-method-tab').forEach(tab => {
    tab.addEventListener('click', () => {
      document.querySelectorAll('.pay-method-tab').forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      showToast(`Payment method: ${tab.textContent.trim()}`);
    });
  });

  // Payment Form Submission -> DISPLAY Payment Confirmation Screen
  const paymentForm = document.getElementById('paymentForm');
  if (paymentForm) {
    paymentForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const randomTx = '#TXN-' + Math.floor(10000000 + Math.random() * 90000000);
      const receiptTxId = document.getElementById('receiptTxId');
      if (receiptTxId) receiptTxId.textContent = randomTx;

      showToast('Processing payment with card bank...');
      setTimeout(() => {
        showToast('Payment Approved! Membership active.');
        navigateTo('screenPaymentConfirmation');
      }, 700);
    });
  }

  // Return to Home after Payment Confirmation
  const btnConfirmGoHome = document.getElementById('btnConfirmGoHome');
  if (btnConfirmGoHome) {
    btnConfirmGoHome.addEventListener('click', () => {
      showToast('PRO Athlete status unlocked! Welcome aboard.');
      navigateTo('screenHome');
    });
  }

  // Diet Planner Meal Logger
  window.logMealItem = (btn, mealName) => {
    btn.classList.add('logged');
    btn.textContent = 'Logged ✓';
    showToast(`${mealName} logged! Macros added to daily tally.`);
  };

  // Video Player Simulation
  let isVideoPlaying = false;
  let scrubberInterval = null;
  const btnToggleVideoPlay = document.getElementById('btnToggleVideoPlay');
  const videoScrubFill = document.getElementById('videoScrubFill');
  const videoCurrentTitle = document.getElementById('videoCurrentTitle');

  if (btnToggleVideoPlay) {
    btnToggleVideoPlay.addEventListener('click', () => {
      if (!isVideoPlaying) {
        isVideoPlaying = true;
        btnToggleVideoPlay.innerHTML = '<svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/></svg>';
        showToast('Workout Video Playing (Simulated HD)');
        scrubberInterval = setInterval(() => {
          let current = parseInt(videoScrubFill.style.width) || 35;
          current = (current + 2) % 100;
          videoScrubFill.style.width = current + '%';
        }, 800);
      } else {
        isVideoPlaying = false;
        btnToggleVideoPlay.innerHTML = '<svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg>';
        clearInterval(scrubberInterval);
        showToast('Workout Video Paused');
      }
    });
  }

  window.loadVideoWorkout = (title, duration, level, coach) => {
    if (videoCurrentTitle) videoCurrentTitle.textContent = `${title} (${duration})`;
    if (videoScrubFill) videoScrubFill.style.width = '5%';
    showToast(`Loaded: ${title} • ${coach}`);
    const screen = document.getElementById('videoMockScreen');
    if (screen) {
      screen.scrollIntoView({ behavior: 'smooth' });
    }
  };

  // Category Filtering
  document.querySelectorAll('.category-chips .chip').forEach(chip => {
    chip.addEventListener('click', (e) => {
      const parent = e.target.closest('.category-chips');
      parent.querySelectorAll('.chip').forEach(c => c.classList.remove('active'));
      chip.classList.add('active');
      showToast(`Filter: ${chip.textContent}`);
    });
  });

  // Blog Modal System
  window.openBlogModal = (title, category, author, content) => {
    const modal = document.getElementById('blogModal');
    document.getElementById('modalTitle').textContent = title;
    document.getElementById('modalCategory').textContent = category;
    document.getElementById('modalAuthor').textContent = author;
    document.getElementById('modalContent').textContent = content;
    modal.classList.add('active');
  };

  const closeBlogModal = () => {
    const modal = document.getElementById('blogModal');
    if (modal) modal.classList.remove('active');
  };

  const btnCloseBlogModal = document.getElementById('btnCloseBlogModal');
  const btnFinishArticle = document.getElementById('btnFinishArticle');

  if (btnCloseBlogModal) btnCloseBlogModal.addEventListener('click', closeBlogModal);
  if (btnFinishArticle) {
    btnFinishArticle.addEventListener('click', () => {
      closeBlogModal();
      showToast('Guide completed! Keep grinding.');
    });
  }
});
