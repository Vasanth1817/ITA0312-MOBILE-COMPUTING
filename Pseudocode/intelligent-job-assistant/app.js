// ===================================================
// JOBPULSE AI — INTELLIGENT JOB ASSISTANT JAVASCRIPT
// Strict pseudocode implementation:
// 1. Welcome -> Login or Register -> Home
// 2. Home -> Subscription | Personal Details | Upload Resume | Choose Job
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

  // 1. Welcome Screen Buttons
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
        showToast('Please enter your email and password');
        return;
      }

      const candidateName = email.split('@')[0];
      const formatted = candidateName.charAt(0).toUpperCase() + candidateName.slice(1);
      const greetingEl = document.getElementById('homeCandidateName');
      if (greetingEl) greetingEl.textContent = formatted;

      showToast(`Welcome back, ${formatted}!`);
      navigateTo('screenHome');
    });
  }

  // 3. Register Flow (ELSE IF user selects "Register" -> DISPLAY Registration Screen -> Home Screen)
  const registerForm = document.getElementById('registerForm');
  if (registerForm) {
    registerForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('regFullName').value.trim();
      const email = document.getElementById('regEmail').value.trim();
      const pass = document.getElementById('regPassword').value.trim();

      if (!name || !email || !pass) {
        showToast('Please complete all registration fields');
        return;
      }

      const greetingEl = document.getElementById('homeCandidateName');
      if (greetingEl) greetingEl.textContent = name;
      const profileNameInput = document.getElementById('profileFullName');
      if (profileNameInput) profileNameInput.value = name;

      showToast(`Candidate account created for ${name}!`);
      navigateTo('screenHome');
    });
  }

  // 4. Home Screen Navigation Cards (Subscription | Personal Details | Upload Resume | Choose Job)
  const navToSubscription = document.getElementById('navToSubscription');
  const navToPersonalDetails = document.getElementById('navToPersonalDetails');
  const navToResumeUpload = document.getElementById('navToResumeUpload');
  const navToChooseJob = document.getElementById('navToChooseJob');

  if (navToSubscription) navToSubscription.addEventListener('click', () => navigateTo('screenSubscription'));
  if (navToPersonalDetails) navToPersonalDetails.addEventListener('click', () => navigateTo('screenPersonalDetails'));
  if (navToResumeUpload) navToResumeUpload.addEventListener('click', () => navigateTo('screenResumeUpload'));
  if (navToChooseJob) navToChooseJob.addEventListener('click', () => navigateTo('screenChooseJob'));

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
      if (confirm('Sign out and return to the Job Assistant Welcome screen?')) {
        showToast('Signed out of JobPulse AI');
        navigateTo('screenWelcome');
      }
    });
  }

  // Subscription plan activation
  window.activateSubscription = (tierName) => {
    showToast(`Subscribed: ${tierName} activated successfully!`);
    setTimeout(() => {
      navigateTo('screenHome');
    }, 1200);
  };

  // Personal Details: Skills Management
  const skillInputField = document.getElementById('skillInputField');
  const skillsTagContainer = document.getElementById('skillsTagContainer');

  if (skillInputField && skillsTagContainer) {
    skillInputField.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        e.preventDefault();
        const value = skillInputField.value.trim();
        if (value) {
          const newTag = document.createElement('span');
          newTag.className = 'skill-tag';
          newTag.innerHTML = `${value} <span class="remove-skill" onclick="removeSkill(this)">&times;</span>`;
          skillsTagContainer.appendChild(newTag);
          skillInputField.value = '';
          showToast(`Added skill: ${value}`);
        }
      }
    });
  }

  window.removeSkill = (btn) => {
    const tag = btn.closest('.skill-tag');
    if (tag) {
      tag.remove();
      showToast('Skill removed');
    }
  };

  // Personal Details form submit
  const detailsForm = document.getElementById('detailsForm');
  if (detailsForm) {
    detailsForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('profileFullName').value.trim();
      const qualification = document.getElementById('profileQualification').value.trim();

      const greetingEl = document.getElementById('homeCandidateName');
      if (greetingEl) greetingEl.textContent = name;

      showToast(`Profile updated: ${name} (${qualification})`);
      navigateTo('screenHome');
    });
  }

  // Resume Upload Dropzone and Pre-filler
  const dropzone = document.getElementById('resumeDropzone');
  const fileInput = document.getElementById('resumeFileInput');
  const btnPrefill = document.getElementById('btnPrefillSampleResume');
  const btnResumeDone = document.getElementById('btnResumeDone');

  const processResumeFile = (fileName, fileSize) => {
    const nameEl = document.getElementById('uploadedResumeFileName');
    const dateEl = document.getElementById('uploadedResumeDate');
    if (nameEl) nameEl.textContent = fileName;
    if (dateEl) dateEl.textContent = `Analyzed just now • ${fileSize}`;
    showToast(`Resume uploaded & parsed: ${fileName}`);
  };

  if (fileInput) {
    fileInput.addEventListener('change', (e) => {
      if (e.target.files && e.target.files[0]) {
        const file = e.target.files[0];
        const sizeKb = Math.round(file.size / 1024) + ' KB';
        processResumeFile(file.name, sizeKb);
      }
    });
  }

  if (btnPrefill) {
    btnPrefill.addEventListener('click', () => {
      processResumeFile('Alex_Chen_Staff_Engineer_CV.pdf', '320 KB');
      showToast('Sample ATS-optimized resume loaded!');
    });
  }

  if (btnResumeDone) {
    btnResumeDone.addEventListener('click', () => {
      showToast('Resume ATS Profile saved! Navigating to jobs...');
      navigateTo('screenChooseJob');
    });
  }

  // Job Search and Category Filters
  const searchInput = document.getElementById('jobSearchInput');
  const jobCards = document.querySelectorAll('.job-card');

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      const query = e.target.value.toLowerCase();
      jobCards.forEach(card => {
        const text = card.textContent.toLowerCase();
        card.style.display = text.includes(query) ? 'block' : 'none';
      });
    });
  }

  document.querySelectorAll('.category-chips .chip').forEach(chip => {
    chip.addEventListener('click', (e) => {
      const parent = e.target.closest('.category-chips');
      parent.querySelectorAll('.chip').forEach(c => c.classList.remove('active'));
      chip.classList.add('active');
      const filter = chip.getAttribute('data-filter') || 'all';

      jobCards.forEach(card => {
        if (filter === 'all') {
          card.style.display = 'block';
        } else {
          const text = card.textContent.toLowerCase();
          card.style.display = text.includes(filter) ? 'block' : 'none';
        }
      });
      showToast(`Filter applied: ${chip.textContent}`);
    });
  });

  // Job Detail Modal & 1-Click AI Apply
  window.openJobDetailModal = (title, company, location, salary, match, desc) => {
    const modal = document.getElementById('jobDetailModal');
    document.getElementById('modalJobTitle').textContent = title;
    document.getElementById('modalJobCompany').textContent = `${company} • ${location}`;
    document.getElementById('modalJobSalary').textContent = `${salary} / yr`;
    document.getElementById('modalJobMatch').textContent = match;
    document.getElementById('modalJobDesc').textContent = desc;
    modal.classList.add('active');
  };

  const closeJobModal = () => {
    const modal = document.getElementById('jobDetailModal');
    if (modal) modal.classList.remove('active');
  };

  const btnCloseJobModal = document.getElementById('btnCloseJobModal');
  const btnSubmitApp = document.getElementById('btnSubmitApplication');

  if (btnCloseJobModal) btnCloseJobModal.addEventListener('click', closeJobModal);
  if (btnSubmitApp) {
    btnSubmitApp.addEventListener('click', () => {
      closeJobModal();
      showToast('Application sent directly to Hiring Manager! 🚀');
    });
  }
});
