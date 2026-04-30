const API_URL = '/api';
const getToken = () => localStorage.getItem('token');
const setToken = (v) => localStorage.setItem('token', v);
const clearToken = () => localStorage.removeItem('token');

async function apiFetch(endpoint, method='GET', body=null){
  const opts = { method, headers: { 'Content-Type': 'application/json' } };
  const token = getToken(); if(token) opts.headers.Authorization = `Bearer ${token}`;
  if(body) opts.body = JSON.stringify(body);

  try {
    const res = await fetch(`${API_URL}${endpoint}`, opts);
    const payload = await res.json().catch(()=>null);

    if (!res.ok) {
      if (res.status === 401) {
        clearToken();
        window.location.href = 'index.html';
        return { success: false, message: 'Unauthorized. Redirecting to login.' };
      }
      return payload || { success: false, message: `Server error ${res.status}` };
    }

    return payload || { success: false, message: 'Empty response from server' };
  } catch (error) {
    return { success: false, message: `Network error: ${error.message}` };
  }
}

async function apiUpload(endpoint, formData) {
  const token = getToken();
  const opts = { method: 'POST', body: formData, headers: {} };
  if (token) opts.headers.Authorization = `Bearer ${token}`;

  try {
    const res = await fetch(`${API_URL}${endpoint}`, opts);
    const payload = await res.json().catch(()=>null);

    if (!res.ok) {
      if (res.status === 401) {
        clearToken();
        window.location.href = 'index.html';
        return { success: false, message: 'Unauthorized. Redirecting to login.' };
      }
      return payload || { success: false, message: `Server error ${res.status}` };
    }

    return payload || { success: false, message: 'Empty response from server' };
  } catch (error) {
    return { success: false, message: `Network error: ${error.message}` };
  }
}

function showMsg(el, msg, duration=4000){ 
  if(!el) return; 
  el.textContent = msg; 
  el.style.display = 'block';
  el.style.padding = '0.8rem';
  el.style.borderRadius = '6px';
  el.style.marginBottom = '1rem';
  el.style.backgroundColor = 'rgba(0, 229, 255, 0.08)';
  el.style.color = 'var(--brand)';
  el.style.border = '1px solid rgba(0, 229, 255, 0.24)';
  setTimeout(()=>{ el.textContent=''; el.style.display='none'; }, duration); 
}

function requireAuth(){ if(!getToken()){ window.location.href = 'index.html'; }}

function setData(name, data){ localStorage.setItem(name, JSON.stringify(data)); }
function getData(name){ const v = localStorage.getItem(name); return v ? JSON.parse(v) : null; }

function applyDarkMode(isDark) {
  document.documentElement.setAttribute('data-theme', isDark ? 'dark' : 'light');
  document.body.classList.toggle('dark-mode', !!isDark);
}

function initDarkMode() {
  const isDark = localStorage.getItem('darkMode') === 'true';
  applyDarkMode(isDark);
  const toggle = document.getElementById('dark-mode-toggle');
  if(toggle) {
    toggle.checked = isDark;
    toggle.onchange = () => {
      localStorage.setItem('darkMode', toggle.checked);
      applyDarkMode(toggle.checked);
    };
  }
}

function initNeuralFlow() {
  document.body.classList.toggle('focus-mode', localStorage.getItem('focusMode') === 'true');

  if (!document.querySelector('.neural-bg')) {
    const neuralBg = document.createElement('div');
    neuralBg.className = 'neural-bg';
    neuralBg.setAttribute('aria-hidden', 'true');

    for (let i = 0; i < 5; i += 1) {
      neuralBg.appendChild(document.createElement('span')).className = 'neural-bg__line';
    }
    for (let i = 0; i < 7; i += 1) {
      neuralBg.appendChild(document.createElement('span')).className = 'neural-bg__node';
    }

    document.body.prepend(neuralBg);
  }

  const currentPage = (window.location.pathname.split('/').pop() || 'index.html').toLowerCase();
  let markedActiveLink = false;
  document.querySelectorAll('.navbar a[href]').forEach((link) => {
    const href = (link.getAttribute('href') || '').split('#')[0].toLowerCase();
    if (!markedActiveLink && href && href === currentPage) {
      link.classList.add('active');
      markedActiveLink = true;
    }
  });

  const shouldReduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.body.classList.toggle('reduce-motion', shouldReduceMotion);

  window.addEventListener('mousemove', (event) => {
    if (shouldReduceMotion || document.body.classList.contains('focus-mode')) return;
    const x = ((event.clientX / window.innerWidth) - 0.5) * 12;
    const y = ((event.clientY / window.innerHeight) - 0.5) * 12;
    document.documentElement.style.setProperty('--parallax-x', `${x}px`);
    document.documentElement.style.setProperty('--parallax-y', `${y}px`);
  }, { passive: true });
}

document.addEventListener('DOMContentLoaded', initNeuralFlow);
