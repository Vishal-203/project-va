# Quick Start Guide

Run this checklist every time you open the project to get it up and running:

## ✅ Quick Startup Steps

### 1. **Navigate to Project**
```bash
cd c:\Users\ADMIN\Documents\GitHub\project-va
```

### 2. **Activate Virtual Environment** (Windows PowerShell)
```powershell
.\venv\Scripts\Activate.ps1
```
OR (Command Prompt)
```cmd
.\venv\Scripts\activate.bat
```

### 3. **Verify MongoDB is Running**
- Open **MongoDB Compass** (if installed)
- Check connection to `mongodb://localhost:27017`
- If MongoDB isn't running, check Windows Services or start MongoDB

### 4. **Start the Backend Server**
```bash
python backend/app.py
```
Watch for output:
```
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.x.x:5000
```
✅ Server is ready when you see these messages

### 5. **Open Frontend in Browser**
Open any of these URLs:
- **Local:** `http://localhost:5000`
- **Network IP:** `http://192.168.x.x:5000` (use the IP shown in terminal)

## 📋 Quick Reference

| Component | Status Check |
|-----------|-------------|
| Virtual Env | Command prompt shows `(venv)` prefix |
| MongoDB | MongoDB Compass connects successfully |
| Backend | Terminal shows `Running on http://...` |
| Frontend | Pages load in browser |

## 🔧 If Something Breaks

| Issue | Solution |
|-------|----------|
| `Module not found` errors | Run `pip install -r backend/requirements.txt` |
| MongoDB won't connect | Start MongoDB from Services or MongoDB Compass |
| Port 5000 in use | Kill process: `netstat -ano \| findstr :5000` then `taskkill /PID <PID> /F` |
| Virtual env won't activate | Try: `python -m venv venv` then activate again |
| API calls fail | Check backend is running and check browser console (F12) for errors |

## 📱 Using on College Network

The backend automatically shows all available IP addresses:
- Use the network IP (like `192.168.x.x`) to access from other devices on the same network
- No code changes needed—frontend uses relative API paths

## 💡 Pro Tips

- **Keep terminal open** while working—don't close it or the server stops
- **Check your IP address** if accessing from another device: On Windows, run `ipconfig` and look for IPv4 Address
- **Browser cache issues?** Press `Ctrl+Shift+Del` to clear cache or open in private/incognito mode
- **See MongoDB data?** Use MongoDB Compass to inspect collections: `ai_study_assistant` database

---

**That's it!** Steps 1-5 every time = your app is running. 🚀
