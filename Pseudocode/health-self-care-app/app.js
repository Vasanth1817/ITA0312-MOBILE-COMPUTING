// ===================================================
// AURA HEALTH & SELF-CARE APP — JAVASCRIPT LOGIC
// Implements screen navigation strictly matching the pseudocode:
// 1. Welcome -> Login / Register
// 2. Login -> Input Email/Pass -> Home
// 3. Register -> Input Name/Email/Pass -> Home
// 4. Home -> Health Routine Blogs / Self-Care Blogs / Meditation
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
    screens.forEach(screen => {
      screen.classList.remove('active');
    });

    const target = document.getElementById(screenId);
    if (target) {
      target.classList.add('active');
      const body = target.querySelector('.screen-body') || target.querySelector('.home-scroll-area');
      if (body) body.scrollTop = 0;
    }

    // Sync Bottom Tab active state if relevant
    const tabs = document.querySelectorAll('.tab-item');
    tabs.forEach(tab => {
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

  // 1. Welcome Screen Navigation
  const btnGoToLogin = document.getElementById('btnGoToLogin');
  const btnGoToRegister = document.getElementById('btnGoToRegister');

  if (btnGoToLogin) {
    btnGoToLogin.addEventListener('click', () => {
      navigateTo('screenLogin');
    });
  }

  if (btnGoToRegister) {
    btnGoToRegister.addEventListener('click', () => {
      navigateTo('screenRegister');
    });
  }

  // Cross-links between Login and Register
  const linkLoginToRegister = document.getElementById('linkLoginToRegister');
  const linkRegisterToLogin = document.getElementById('linkRegisterToLogin');

  if (linkLoginToRegister) {
    linkLoginToRegister.addEventListener('click', (e) => {
      e.preventDefault();
      navigateTo('screenRegister');
    });
  }

  if (linkRegisterToLogin) {
    linkRegisterToLogin.addEventListener('click', (e) => {
      e.preventDefault();
      navigateTo('screenLogin');
    });
  }

  // Generic Back Buttons
  document.querySelectorAll('.back-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const targetScreen = btn.getAttribute('data-target') || 'screenWelcome';
      navigateTo(targetScreen);
    });
  });

  // 2. Login Flow (Pseudocode: INPUT Email & Password -> NAVIGATE TO Home Screen)
  const loginForm = document.getElementById('loginForm');
  if (loginForm) {
    loginForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const email = document.getElementById('loginEmail').value.trim();
      const pass = document.getElementById('loginPassword').value.trim();

      if (!email || !pass) {
        showToast('Please enter both Email and Password');
        return;
      }

      // Extract username before @ for personalized greeting
      const username = email.split('@')[0];
      const capitalized = username.charAt(0).toUpperCase() + username.slice(1);
      const greetingEl = document.getElementById('homeUserName');
      if (greetingEl) greetingEl.textContent = capitalized;

      showToast(`Welcome back, ${capitalized}!`);
      navigateTo('screenHome');
    });
  }

  // 3. Register Flow (Pseudocode: INPUT Name, Email & Password -> NAVIGATE TO Home Screen)
  const registerForm = document.getElementById('registerForm');
  if (registerForm) {
    registerForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('regName').value.trim();
      const email = document.getElementById('regEmail').value.trim();
      const pass = document.getElementById('regPassword').value.trim();

      if (!name || !email || !pass) {
        showToast('Please fill in Name, Email and Password');
        return;
      }

      const greetingEl = document.getElementById('homeUserName');
      if (greetingEl) greetingEl.textContent = name;

      showToast(`Account created for ${name}!`);
      navigateTo('screenHome');
    });
  }

  // 4. Home Screen Navigation Cards (Health Routine Blogs / Self-Care Blogs / Meditation)
  const navToHealthBlogs = document.getElementById('navToHealthBlogs');
  const navToSelfCareBlogs = document.getElementById('navToSelfCareBlogs');
  const navToMeditation = document.getElementById('navToMeditation');

  if (navToHealthBlogs) {
    navToHealthBlogs.addEventListener('click', () => {
      navigateTo('screenHealthBlogs');
    });
  }

  if (navToSelfCareBlogs) {
    navToSelfCareBlogs.addEventListener('click', () => {
      navigateTo('screenSelfCareBlogs');
    });
  }

  if (navToMeditation) {
    navToMeditation.addEventListener('click', () => {
      navigateTo('screenMeditation');
    });
  }

  // Bottom Tab Bar navigation
  document.querySelectorAll('.tab-item').forEach(tab => {
    tab.addEventListener('click', () => {
      const target = tab.getAttribute('data-target');
      if (target) navigateTo(target);
    });
  });

  // Logout / Return to Welcome
  const btnHomeLogout = document.getElementById('btnHomeLogout');
  if (btnHomeLogout) {
    btnHomeLogout.addEventListener('click', () => {
      if (confirm('Do you want to log out and return to the Welcome screen?')) {
        showToast('Logged out successfully');
        navigateTo('screenWelcome');
      }
    });
  }

  // Mood Selector Buttons
  document.querySelectorAll('.mood-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.mood-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const mood = btn.getAttribute('data-mood');
      showToast(`Mood logged: Feeling ${mood}`);
    });
  });

  // Category Chip Filtering
  document.querySelectorAll('.category-chips .chip').forEach(chip => {
    chip.addEventListener('click', (e) => {
      const parent = e.target.closest('.category-chips');
      parent.querySelectorAll('.chip').forEach(c => c.classList.remove('active'));
      chip.classList.add('active');
      showToast(`Filtered: ${chip.textContent}`);
    });
  });

  // Interactive Breathing Exercise Engine
  let breathingInterval = null;
  let isBreathingActive = false;
  let currentPhase = 'inhale';
  let phaseTimer = 4;

  const btnToggleBreathing = document.getElementById('btnToggleBreathing');
  const breathCircle = document.getElementById('breathCircle');
  const breathPhaseText = document.getElementById('breathPhaseText');
  const breathTimerDisplay = document.getElementById('breathTimerDisplay');
  const breathBtnLabel = document.getElementById('breathBtnLabel');

  const updateBreathingCycle = () => {
    phaseTimer--;
    if (phaseTimer <= 0) {
      if (currentPhase === 'inhale') {
        currentPhase = 'hold';
        phaseTimer = 4;
        breathCircle.className = 'breathing-circle-inner hold';
        breathPhaseText.textContent = 'Hold';
      } else if (currentPhase === 'hold') {
        currentPhase = 'exhale';
        phaseTimer = 4;
        breathCircle.className = 'breathing-circle-inner exhale';
        breathPhaseText.textContent = 'Exhale';
      } else {
        currentPhase = 'inhale';
        phaseTimer = 4;
        breathCircle.className = 'breathing-circle-inner inhale';
        breathPhaseText.textContent = 'Inhale';
      }
    }
    breathTimerDisplay.textContent = `00:0${phaseTimer}`;
  };

  if (btnToggleBreathing) {
    btnToggleBreathing.addEventListener('click', () => {
      if (!isBreathingActive) {
        isBreathingActive = true;
        currentPhase = 'inhale';
        phaseTimer = 4;
        breathCircle.className = 'breathing-circle-inner inhale';
        breathPhaseText.textContent = 'Inhale';
        breathTimerDisplay.textContent = '00:04';
        breathBtnLabel.textContent = 'Pause Breathing';
        breathingInterval = setInterval(updateBreathingCycle, 1000);
        showToast('Breathing session started. Inhale slowly...');
      } else {
        isBreathingActive = false;
        clearInterval(breathingInterval);
        breathCircle.className = 'breathing-circle-inner';
        breathPhaseText.textContent = 'Inhale';
        breathTimerDisplay.textContent = '00:04';
        breathBtnLabel.textContent = 'Resume Breathing';
        showToast('Breathing paused');
      }
    });
  }

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
  const btnBookmarkArticle = document.getElementById('btnBookmarkArticle');

  if (btnCloseBlogModal) btnCloseBlogModal.addEventListener('click', closeBlogModal);
  if (btnFinishArticle) {
    btnFinishArticle.addEventListener('click', () => {
      closeBlogModal();
      showToast('Article marked as complete! +15 Mind Points');
    });
  }
  if (btnBookmarkArticle) {
    btnBookmarkArticle.addEventListener('click', () => {
      showToast('Article saved to your wellness bookmarks!');
    });
  }

  // Quick Exercise Routine Click handler
  window.startExerciseRoutine = (title, description) => {
    openBlogModal(title, 'Mind-Body Routine', 'Aura Zen Coach', description + ' Complete 3 sets of mindful repetitions while maintaining relaxed, rhythmic breathing.');
  };
});
