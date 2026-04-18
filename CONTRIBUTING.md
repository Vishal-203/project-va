# Contributing to AI Study Assistant

Thank you for contributing! Please follow these guidelines to ensure code quality and consistency.

## 📋 Before You Start

1. Read [STRUCTURE.md](STRUCTURE.md) - Understand project organization
2. Read [DEV_GUIDE.md](DEV_GUIDE.md) - Development setup & conventions
3. Check existing issues & PRs to avoid duplicates

## 🎯 Types of Contributions

### 🐛 Bug Reports
- Use existing issues or create new one
- Include: description, steps to reproduce, expected vs actual behavior
- Add screenshots if relevant

### ✨ Feature Requests
- Discuss in issues first
- Explain use case and benefit
- Consider impact on existing features

### 🔧 Code Changes
- Follow the workflow below
- Write clear, descriptive commit messages
- Test thoroughly before submitting

## 🚀 Contribution Workflow

### 1. Fork & Clone
```bash
git clone <your-fork-url>
cd project-va
```

### 2. Create Feature Branch
```bash
git checkout -b feature/your-feature-name
```

### 3. Make Changes

**Follow code style:**
- Python: PEP 8 (see DEV_GUIDE.md)
- JavaScript: ES6+ (see DEV_GUIDE.md)
- HTML/CSS: Semantic & accessible

**Keep changes focused:**
- One feature per branch
- One commit per logical change
- Write descriptive commit messages

### 4. Test Your Changes

```bash
# Start backend
python backend/app.py

# Test in browser
# - Register new account
# - Test all features
# - Check console for errors
# - Test on mobile size
```

### 5. Commit & Push

```bash
# Stage changes
git add .

# Commit with message
git commit -m "feat: Add feature description"

# Push to your fork
git push origin feature/your-feature-name
```

### 6. Create Pull Request

- Title: Clear description of change
- Description: Explain what & why
- Reference related issues: "Fixes #123"

## ✅ Pull Request Checklist

- [ ] Changes follow code style conventions
- [ ] No console errors in browser
- [ ] Feature tested manually (all flows)
- [ ] Responsive design tested (mobile)
- [ ] No breaking changes to existing features
- [ ] Commit messages are clear
- [ ] Documentation updated if needed
- [ ] .env files not included

## 📝 Commit Message Examples

```
feat: Add dark mode toggle to all pages
- Implement global dark mode utility in app.js
- Add theme toggle to profile page
- Persist preference in localStorage
- Update all components for dark mode

fix: Dark mode not applying to navbar text
- Update navbar text color in dark mode handler
- Ensure contrast ratio meets accessibility standards

docs: Add development guide with setup instructions

refactor: Move API utilities from individual files to app.js
- Centralize fetch logic for consistency
- Reduce code duplication
- Improve maintainability
```

## 🎨 Code Review Process

- Maintainers will review PRs
- Provide feedback and suggestions
- Request changes if needed
- Approval → Merge to main

## 🤝 Community Guidelines

- Be respectful and constructive
- Help others when possible
- Ask questions if unclear
- Provide context in discussions
- Give credit where due

## 📚 Documentation

When making changes, update:

- **README.md** - If setup/usage changes
- **STRUCTURE.md** - If folder structure changes
- **DEV_GUIDE.md** - If process/conventions change
- **Code comments** - Complex logic explanation
- **Docstrings** - All functions & classes

## 🚫 Things to Avoid

❌ Committing .env files
❌ Large unrelated changes in one PR
❌ Hardcoded values (use environment variables)
❌ Breaking existing functionality
❌ Ignoring test failures
❌ Complex nested conditionals (refactor to functions)
❌ Console logs in production code

## 📦 Release Process

1. Update version in relevant files
2. Update CHANGELOG if needed
3. Create release branch
4. Tag release: `git tag v1.0.0`
5. Merge to main
6. Deploy to production

## 🆘 Need Help?

- Check [DEV_GUIDE.md](DEV_GUIDE.md) for setup issues
- Review [STRUCTURE.md](STRUCTURE.md) for architecture questions
- Search existing issues for solutions
- Ask in PR/issue discussions

## 📞 Contact

For questions:
- Open an issue with "question" label
- Discuss in PR comments
- Contact maintainers

---

## 🎯 Areas We're Looking For Help

### Backend
- [ ] Database query optimization
- [ ] Error handling improvements
- [ ] API validation enhancements
- [ ] Performance profiling

### Frontend
- [ ] Accessibility improvements (WCAG)
- [ ] Mobile responsiveness refinement
- [ ] Animation optimization
- [ ] Cross-browser testing

### Documentation
- [ ] Better API documentation
- [ ] Video tutorials
- [ ] Deployment guides
- [ ] Troubleshooting docs

### Testing
- [ ] Unit tests
- [ ] Integration tests
- [ ] E2E tests
- [ ] Load testing

---

**Thank you for contributing! 🌟**

Last Updated: March 31, 2026
