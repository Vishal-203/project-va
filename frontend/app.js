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
  el.style.backgroundColor = '#e8f5e9';
  el.style.color = '#2e7d32';
  el.style.border = '1px solid #c8e6c9';
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
