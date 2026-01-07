// dark mode toggle logic

const darkMode = window.matchMedia('(prefers-color-scheme: dark)');

function setHljsTheme(theme) {
    const link = document.getElementById('hljs-theme');
    if (!link) return;
    link.href = `/static/css/highlight/${theme}.css`;
}

function enableDarkMode(isDark) {
    if (isDark) {
        document.body.classList.add('dark');
        setHljsTheme('github-dark');
    } else {
        document.body.classList.remove('dark');
        setHljsTheme('github');
    }
    localStorage.setItem('darkMode', isDark ? 'true' : 'false');
}

function toggleDarkModeButton() {
    const isDark = document.body.classList.contains('dark');
    enableDarkMode(!isDark);
}

// watch for system dark mode changes
darkMode.addEventListener('change', (event) => {
    if (!localStorage.getItem('darkMode')) {
        enableDarkMode(event.matches);
    }
});

// initial theme based on system preference
const savedPreference = localStorage.getItem('darkMode');
if (savedPreference !== null) {
    enableDarkMode(savedPreference === 'true');
} else {
    enableDarkMode(darkMode.matches);
}

// toggle button (make sure this exists in HTML)
const toggleButton = document.getElementById('dark-mode-toggle');
if (toggleButton) {
    toggleButton.addEventListener('click', toggleDarkModeButton);
}